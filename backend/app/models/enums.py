from enum import StrEnum


class EntityStatus(StrEnum):
    ACTIVE = "active"
    INACTIVE = "inactive"
    SUSPENDED = "suspended"
    DEACTIVATED = "deactivated"


class UserRole(StrEnum):
    PLATFORM_ADMIN = "platform_admin"
    FRANCHISOR_ADMIN = "franchisor_admin"
    REGIONAL_ADMIN = "regional_admin"
    TENANT_ADMIN = "tenant_admin"
    TENANT_USER = "tenant_user"


class AccessLevel(StrEnum):
    READ = "read"
    WRITE = "write"
    APPROVE = "approve"


class LeadSource(StrEnum):
    FB_ADS = "fb_ads"
    IG_ADS = "ig_ads"
    GOOGLE_ADS = "google_ads"
    WHATSAPP = "whatsapp"
    WEBSITE_FORM = "website_form"
    WALK_IN = "walk_in"
    REFERRAL = "referral"


class LeadStatus(StrEnum):
    NEW = "new"
    CONTACTED = "contacted"
    QUALIFIED = "qualified"
    FOLLOW_UP_REQUIRED = "follow_up_required"
    CONVERTED = "converted"
    CLOSED = "closed"
