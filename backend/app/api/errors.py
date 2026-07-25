from http import HTTPStatus

from fastapi import FastAPI, HTTPException, Request
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse


def _code_for_status(status_code: int) -> str:
    try:
        return HTTPStatus(status_code).phrase.lower().replace(" ", "_")
    except ValueError:
        return "error"


async def http_exception_handler(request: Request, exc: Exception) -> JSONResponse:
    # Starlette's handler registry is keyed by exception type, so `exc` is
    # guaranteed to be an HTTPException here - narrow the type for mypy.
    assert isinstance(exc, HTTPException)
    return JSONResponse(
        status_code=exc.status_code,
        content={"error": {"code": _code_for_status(exc.status_code), "message": exc.detail}},
    )


async def validation_exception_handler(request: Request, exc: Exception) -> JSONResponse:
    assert isinstance(exc, RequestValidationError)
    return JSONResponse(
        status_code=422,
        content={
            "error": {
                "code": "validation_error",
                "message": "Invalid request",
                "details": jsonable_encoder(exc.errors()),
            }
        },
    )


def register_exception_handlers(app: FastAPI) -> None:
    app.add_exception_handler(HTTPException, http_exception_handler)
    app.add_exception_handler(RequestValidationError, validation_exception_handler)
