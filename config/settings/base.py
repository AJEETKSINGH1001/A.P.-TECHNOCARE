
from pathlib import Path

import environ


BASE_DIR = Path(__file__).resolve().parent.parent.parent

env = environ.Env(
    DEBUG=(bool, False),
)


# -----------------------------------------------------------------------------
# Core
# -----------------------------------------------------------------------------

SECRET_KEY = env(
    "SECRET_KEY",
    default="django-insecure-development-only-change-me",
)

DEBUG = env("DEBUG", default=False)

ALLOWED_HOSTS = env.list(
    "ALLOWED_HOSTS",
    default=["127.0.0.1", "localhost"],
)


# -----------------------------------------------------------------------------
# Applications
# -----------------------------------------------------------------------------

INSTALLED_APPS = [
    # Third-party - Jazzmin must be before Django admin
    "jazzmin",

    # Django
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # Third-party
    "rest_framework",
    "django_filters",
    "django_htmx",

    # Local
    "apps.core",
    "apps.catalog",
    "apps.enquiries",
    "apps.content",
    "apps.seo",
    "apps.analytics",
]


# -----------------------------------------------------------------------------
# Jazzmin Admin Configuration
# -----------------------------------------------------------------------------

JAZZMIN_SETTINGS = {
    "site_title": "A.P. TECHNOCARE Admin",
    "site_header": "A.P. TECHNOCARE",
    "site_brand": "A.P. TECHNOCARE",
    "site_logo": None,
    "login_logo": None,
    "site_icon": None,

    "welcome_sign": "Welcome to A.P. TECHNOCARE Administration",
    "copyright": "A.P. TECHNOCARE",

    "search_model": [],

    "user_avatar": None,

    "topmenu_links": [
        {
            "name": "View Website",
            "url": "/",
            "new_window": True,
        },
        {
            "model": "auth.User",
        },
    ],

    "usermenu_links": [
        {
            "name": "View Website",
            "url": "/",
            "new_window": True,
        },
    ],

    "show_sidebar": True,
    "navigation_expanded": True,
    "hide_apps": [],
    "hide_models": [],

    "order_with_respect_to": [
        "apps.catalog",
        "apps.enquiries",
        "apps.content",
        "apps.core",
        "apps.seo",
        "apps.analytics",
        "auth",
    ],

    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.group": "fas fa-users",

        "apps.catalog": "fas fa-boxes",
        "apps.catalog.product": "fas fa-box",
        "apps.catalog.category": "fas fa-layer-group",
        "apps.catalog.brand": "fas fa-tags",

        "apps.enquiries": "fas fa-envelope",
        "apps.content": "fas fa-file-alt",
        "apps.core": "fas fa-building",
        "apps.seo": "fas fa-search",
        "apps.analytics": "fas fa-chart-line",
    },

    "default_icon_parents": "fas fa-folder",
    "default_icon_children": "fas fa-circle",

    "related_modal_active": True,
    "show_ui_builder": False,
    "changeform_format": "horizontal_tabs",
    "language_chooser": False,
}


# -----------------------------------------------------------------------------
# Jazzmin UI Tweaks
# -----------------------------------------------------------------------------

JAZZMIN_UI_TWEAKS = {
    "theme": "flatly",

    "navbar": "navbar-dark",
    "navbar_fixed": True,
    "navbar_small_text": False,

    "brand_colour": "navbar-dark",

    "sidebar": "sidebar-dark-primary",
    "sidebar_fixed": True,
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": True,
    "sidebar_nav_compact_style": False,
    "sidebar_nav_legacy_style": False,

    "footer_fixed": False,

    "actions_sticky_top": True,

    "button_classes": {
        "primary": "btn-primary",
        "secondary": "btn-secondary",
        "info": "btn-info",
        "success": "btn-success",
        "warning": "btn-warning",
        "danger": "btn-danger",
    },
}


# -----------------------------------------------------------------------------
# Middleware
# -----------------------------------------------------------------------------

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


ROOT_URLCONF = "config.urls"


# -----------------------------------------------------------------------------
# Templates
# -----------------------------------------------------------------------------

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            BASE_DIR / "templates",
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "apps.core.context_processors.site_context",
                "apps.core.context_processors.admin_dashboard",
            ],
        },
    },
]


WSGI_APPLICATION = "config.wsgi.application"
ASGI_APPLICATION = "config.asgi.application"


# -----------------------------------------------------------------------------
# Database
# -----------------------------------------------------------------------------

DATABASES = {
    "default": env.db(
        "DATABASE_URL",
        default=f"sqlite:///{BASE_DIR / 'db.sqlite3'}",
    )
}


# -----------------------------------------------------------------------------
# Password validation
# -----------------------------------------------------------------------------

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "UserAttributeSimilarityValidator"
        ),
    },
    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "MinimumLengthValidator"
        ),
    },
    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "CommonPasswordValidator"
        ),
    },
    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "CommonPasswordValidator"
        ),
    },
    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "NumericPasswordValidator"
        ),
    },
]


# -----------------------------------------------------------------------------
# Internationalization
# -----------------------------------------------------------------------------

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Asia/Kolkata"

USE_I18N = True

USE_TZ = True


# -----------------------------------------------------------------------------
# Static files
# -----------------------------------------------------------------------------

STATIC_URL = "/static/"

STATIC_ROOT = BASE_DIR / "staticfiles"

STATICFILES_DIRS = [
    BASE_DIR / "static",
]


# -----------------------------------------------------------------------------
# Media files
# -----------------------------------------------------------------------------

MEDIA_URL = "/media/"

MEDIA_ROOT = BASE_DIR / "media"


# -----------------------------------------------------------------------------
# Default primary key
# -----------------------------------------------------------------------------

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# -----------------------------------------------------------------------------
# Security defaults
# -----------------------------------------------------------------------------

SESSION_COOKIE_HTTPONLY = True

CSRF_COOKIE_HTTPONLY = True

X_FRAME_OPTIONS = "DENY"


# -----------------------------------------------------------------------------
# Email
# -----------------------------------------------------------------------------

EMAIL_BACKEND = env(
    "EMAIL_BACKEND",
    default="django.core.mail.backends.console.EmailBackend",
)

DEFAULT_FROM_EMAIL = env(
    "DEFAULT_FROM_EMAIL",
    default="webmaster@localhost",
)