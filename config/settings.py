# settings.py

"""
Atzee Backend - Django Settings (White-Label Ready)
===================================================

This configuration is designed for:
- Multi-tenant deployments
- Multi-vertical architecture
- Environment-driven configuration (12-factor compliant)

All environment-specific values MUST be defined in `.env`.

Author: Atzee Platform
"""


# ================================================================
# 🔹 CORE IMPORTS
# ================================================================
from pathlib import Path
from datetime import timedelta
import os

from dotenv import load_dotenv
from corsheaders.defaults import default_headers


# ================================================================
# 🔹 BASE CONFIGURATION
# ================================================================
BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(os.path.join(BASE_DIR, ".env"))


# ================================================================
# 🔐 SECURITY
# ================================================================
SECRET_KEY = os.getenv("SECRET_KEY", "unsafe-default")
DEBUG = os.getenv("DEBUG", "False") == "True"
ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "").split(",")


# ================================================================
# 📦 DJANGO CORE APPS
# ================================================================
DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]


# ================================================================
# 🧠 CORE PLATFORM APPS
# ================================================================
CORE_APPS = [
    "core.account.apps.AccountConfig",
    "core.apps.CoreConfig",
    "core.audit_logs.apps.AuditLogsConfig",
    "core.chat.apps.ChatConfig",
    "core.classifications.categories.apps.CategoriesConfig",
    "core.classifications.tags.apps.TagsConfig",
    "core.classifications.labels.apps.LabelsConfig",
    "core.classifications.attributes.apps.AttributesConfig",
    "core.dashboard.apps.DashboardConfig",
    "core.geo.countries.apps.CountriesConfig",
    "core.geo.regions.apps.RegionsConfig",
    "core.geo.cities.apps.CitiesConfig",
    "core.geo.districts.apps.DistrictsConfig",
    "core.geo.villages.apps.VillagesConfig",
    "core.geo.spatial.apps.SpatialConfig",
    "core.geo.timezones.apps.TimezonesConfig",
    "core.legal.apps.LegalConfig",
    "core.master.banks.apps.BanksConfig",
    "core.master.uom.apps.UOMConfig",
    "core.master.locations.apps.LocationsConfig",
    "core.master.currencies.apps.CurrenciesConfig",
    "core.users.apps.UsersConfig",
    "core.tenants.apps.TenantsConfig",
    "core.roles.apps.RolesConfig",
    "core.permissions.apps.PermissionsConfig",
    "core.ui.apps.UIConfig",
    "core.settings.apps.SettingsConfig",
    "core.notifications.apps.NotificationsConfig",
    "core.entities.apps.EntitiesConfig",
    "core.widgets.apps.WidgetsConfig",
    "core.org.departments.apps.DepartmentsConfig",
    "core.org.branches.apps.BranchesConfig",
    "core.otp.apps.OTPConfig",
    "core.files.apps.FilesConfig",
    "core.schedule.events.apps.EventsConfig",
    "core.schedule.holidays.apps.HolidaysConfig",
    "core.schedule.shifts.apps.ShiftsConfig",
    "core.schedule.reminders.apps.RemindersConfig",
    "core.schedule.recurrings.apps.RecurringsConfig",
    "core.wallet.apps.WalletConfig",
    "core.wallet_withdrawal.apps.WalletWithdrawalConfig",
    "core.fees.apps.FeesConfig",
    "core.realtime.apps.RealtimeConfig",
]


# ================================================================
# 💼 BUSINESS LAYER
# ================================================================
BUSINESS_APPS = [
    "business.users.apps.UsersConfig",
    "business.customers.apps.CustomersConfig",
    "business.products.apps.ProductsConfig",
    "business.inventory.apps.InventoryConfig",
    "business.partners.apps.PartnersConfig",
    "business.transactions.apps.TransactionsConfig",
    "business.documents.apps.DocumentsConfig",
    "business.payments.apps.PaymentsConfig",
    "business.payment_gateway.apps.PaymentGatewayConfig",
    "business.booking.apps.BookingConfig",
    "business.tracking.apps.TrackingConfig",
    "business.reviews.apps.ReviewsConfig",
]


# ================================================================
# 🧾 ACCOUNTING LAYER
# ================================================================
ACCOUNTING_APPS = [
    "accounting.apps.AccountingConfig",
]


# ================================================================
# 👥 HR LAYER
# ================================================================
HR_APPS = [
    "hr.employees.apps.EmployeesConfig",
    "hr.attendance.apps.AttendanceConfig",
    "hr.payroll.apps.PayrollConfig",
]


# ================================================================
# 🏪 MARKETPLACE
# ================================================================
MARKETPLACE_APPS = [
    "marketplace.apps.MarketplaceConfig",
]


# ================================================================
# 🧩 VERTICAL LOADER (ENV-DRIVEN)
# ================================================================
VERTICALS = [
    v.strip()
    for v in os.getenv("VERTICAL", "").split(",")
    if v.strip()
]

VERTICAL_APPS = [
    f"verticals.{v}.apps.{v.capitalize()}Config"
    for v in VERTICALS
]


# ================================================================
# 🚀 INSTALLED APPS
# ================================================================
INSTALLED_APPS = (
    ["daphne", "corsheaders", "django_celery_beat"]
    +
    DJANGO_APPS 
    + [
        "rest_framework",
        "rest_framework.authtoken",
        "rest_framework_simplejwt.token_blacklist",
    ]
    + CORE_APPS 
    + BUSINESS_APPS 
    + ACCOUNTING_APPS 
    + HR_APPS
    + MARKETPLACE_APPS
    + VERTICAL_APPS
    + ["setup"]
)


# ================================================================
# 🔗 MIDDLEWARE
# ================================================================
MIDDLEWARE = [
    # CORS & SECURITY
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",

    # SESSION & REQUEST
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",

    # AUTH DJANGO (WAJIB sebelum custom middleware)
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",

    # CORE CONTEXT (SETELAH USER TER-RESOLVE)
    "core.tenants.middleware.TenantContextMiddleware",
    "core.roles.middleware.RoleContextMiddleware",
    "core.permissions.middleware.PermissionGuardMiddleware",

    # AUDIT PALING AKHIR
    "core.audit_logs.middleware.AuditMiddleware"
]


# ================================================================
# 🌐 API / REST
# ================================================================
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
    ],
    "EXCEPTION_HANDLER": "shared.api.handlers.custom_exception_handler",
}


# ================================================================
# 🔌 CHANNELS (WEBSOCKET)
# ================================================================
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [("127.0.0.1", 6379)],
        },
    }
}


# ================================================================
# 🗄 DATABASE
# ================================================================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv("DB_NAME"),
        'USER': os.getenv("DB_USER"),
        'PASSWORD': os.getenv("DB_PASSWORD"),
        'HOST': os.getenv("DB_HOST", "localhost"),
        'PORT': os.getenv("DB_PORT", "5432"),
    }
}


# ================================================================
# 🌍 INTERNATIONALIZATION
# ================================================================
LANGUAGE_CODE = "en-us"
TIME_ZONE = os.getenv("TIME_ZONE", "UTC")
USE_I18N = True
USE_TZ = True


# ================================================================
# 📁 STATIC & MEDIA
# ================================================================
STATIC_URL = "static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static")

MEDIA_URL = "/media/"
# MEDIA_ROOT = os.path.join(BASE_DIR, "media")


# ================================================================
# 🔐 JWT AUTH
# ================================================================
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(
        minutes=int(os.getenv("ACCESS_TOKEN_LIFETIME", 30))
    ),
    "REFRESH_TOKEN_LIFETIME": timedelta(
        days=int(os.getenv("REFRESH_TOKEN_LIFETIME", 30))
    ),

    "ROTATE_REFRESH_TOKENS": True,
    "BLACKLIST_AFTER_ROTATION": True,
}


# ================================================================
# 🌐 CORS & CSRF
# ================================================================
CORS_ALLOW_HEADERS = list(default_headers) + [
    "content-type",
    "x-tenant-code",
    "x-role-id",
]

CORS_ALLOWED_ORIGINS = os.getenv("CORS_ALLOWED_ORIGINS", "").split(",")
CSRF_TRUSTED_ORIGINS = os.getenv("CSRF_TRUSTED_ORIGINS", "").split(",")

CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_ALL_ORIGINS = False


# ================================================================
# ⚡ CACHE (ENV-DRIVEN)
# ================================================================
CACHE_BACKEND = os.getenv("CACHE_BACKEND", "locmem")

if CACHE_BACKEND == "redis":
    CACHES = {
        "default": {
            "BACKEND": "django_redis.cache.RedisCache",
            "LOCATION": os.getenv("REDIS_URL", "redis://127.0.0.1:6379/1"),
            "OPTIONS": {
                "CLIENT_CLASS": "django_redis.client.DefaultClient",
            }
        }
    }
else:
    CACHES = {
        "default": {
            "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        }
    }


# ================================================================
# 🔗 BASE URL
# ================================================================
BASE_BACKEND_URL = os.getenv("BASE_BACKEND_URL", "http://localhost:8000")


# ================================================================
# 📱 INTEGRATIONS
# ================================================================
FONNTE_API_KEY = os.getenv("FONNTE_API_KEY")


# ================================================================
# 🔐 AUTH CONFIG
# ================================================================
AUTH_METHODS = os.getenv("AUTH_METHODS", "password").split(",")
AUTH_DEFAULT_METHOD = os.getenv("AUTH_DEFAULT_METHOD", "password")


# ================================================================
# 🧵 CELERY
# ================================================================
CELERY_BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
CELERY_TIMEZONE = TIME_ZONE


# ================================================================
# 🔧 DJANGO DEFAULTS
# ================================================================
ROOT_URLCONF = "config.urls"
WSGI_APPLICATION = "config.wsgi.application"
ASGI_APPLICATION = "config.asgi.application"

AUTH_USER_MODEL = "core_users.User"
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# ================================================================
# 🔧 DJANGO TEMPLATES
# ================================================================
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]


# ================================================================
# 🔧 PASSWORD VALIDATORS
# ================================================================
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
        "OPTIONS": {
            "max_similarity": 0.9,  # default 0.7 (lebih ketat)
        }
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
        "OPTIONS": {
            "min_length": 6,
        }
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]















