"""
Django settings for config project.

Base settings shared between development and production.
"""

import os
from pathlib import Path

import dj_database_url


# =============================================================================
# BASE DIRECTORY
# =============================================================================

BASE_DIR = Path(__file__).resolve().parent.parent


# =============================================================================
# SECURITY
# =============================================================================

SECRET_KEY = os.environ.get(
    "SECRET_KEY",
    "django-insecure-local-development-key",
)

DEBUG = os.environ.get("DEBUG", "False") == "True"

# ALLOWED_HOSTS
# Can be overridden from Render/environment using:
# ALLOWED_HOSTS=your-site.onrender.com
allowed_hosts_env = os.environ.get("ALLOWED_HOSTS")

if allowed_hosts_env:
    ALLOWED_HOSTS = [
        host.strip()
        for host in allowed_hosts_env.split(",")
        if host.strip()
    ]
else:
    ALLOWED_HOSTS = [
        "localhost",
        "127.0.0.1",
        ".onrender.com",
    ]


# CSRF trusted origins
csrf_origins_env = os.environ.get("CSRF_TRUSTED_ORIGINS")

if csrf_origins_env:
    CSRF_TRUSTED_ORIGINS = [
        origin.strip()
        for origin in csrf_origins_env.split(",")
        if origin.strip()
    ]
else:
    CSRF_TRUSTED_ORIGINS = [
        "https://*.onrender.com",
    ]


# =============================================================================
# APPLICATION DEFINITION
# =============================================================================

INSTALLED_APPS = [

    # -------------------------------------------------------------------------
    # Third-party apps
    # -------------------------------------------------------------------------
    "jazzmin",

    # -------------------------------------------------------------------------
    # Django built-in apps
    # -------------------------------------------------------------------------
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # -------------------------------------------------------------------------
    # Your project applications
    # -------------------------------------------------------------------------
    # IMPORTANT:
    # Add your actual apps here.
    #
    # Example:
    # "apps.core",
    # "apps.catalog",
    # "apps.enquiries",
    # "apps.content",
    # "apps.analytics",
]


# =============================================================================
# JAZZMIN ADMIN CONFIGURATION
# A.P. TECHNOCARE
# =============================================================================

JAZZMIN_SETTINGS = {

    # Site identity
    "site_title": "A.P. TECHNOCARE Admin",
    "site_header": "A.P. TECHNOCARE",
    "site_brand": "A.P. TECHNOCARE",

    "welcome_sign": "Welcome to A.P. TECHNOCARE Administration",
    "copyright": "A.P. TECHNOCARE",

    # Sidebar
    "show_sidebar": True,
    "navigation_expanded": True,

    # Sidebar app ordering
    "order_with_respect_to": [
        "catalog",
        "enquiries",
        "content",
        "core",
        "analytics",
        "auth",
    ],

    # Icons
    "icons": {
        "catalog": "fas fa-boxes",
        "catalog.product": "fas fa-box",
        "catalog.category": "fas fa-sitemap",
        "catalog.brand": "fas fa-tags",

        "content": "fas fa-file-alt",

        "enquiries": "fas fa-envelope",

        "core": "fas fa-building",

        "analytics": "fas fa-chart-line",

        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.group": "fas fa-users",
    },

    # Interface options
    "show_ui_builder": False,
    "show_theme_chooser": True,
    "related_modal_active": True,

    # Form layout
    "changeform_format": "horizontal_tabs",

    # Search
    "search_model": [],

    # User menu
    "usermenu_links": [
        {
            "name": "View Website",
            "url": "/",
            "new_window": True,
        },
    ],
}


# =============================================================================
# JAZZMIN UI TWEAKS
# =============================================================================

JAZZMIN_UI_TWEAKS = {

    # Main theme
    "theme": "flatly",

    # Navbar
    "navbar": "navbar-dark",
    "navbar_classes": "navbar-dark",

    # Sidebar
    "sidebar": "sidebar-dark-primary",
    "sidebar_nav_small_text": False,
    "sidebar_nav_child_indent": True,
    "sidebar_nav_compact_style": True,
    "sidebar_nav_legacy_style": False,

    # Brand
    "brand_colour": "navbar-primary",

    # Layout
    "accent": "accent-primary",
    "body_small_text": False,
    "footer_small_text": False,
    "sidebar_small_text": False,

    # Buttons
    "button_classes": {
        "primary": "btn-primary",
        "secondary": "btn-secondary",
        "info": "btn-info",
        "success": "btn-success",
        "warning": "btn-warning",
        "danger": "btn-danger",
    },
}


# =============================================================================
# MIDDLEWARE
# =============================================================================

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


# =============================================================================
# URL CONFIGURATION
# =============================================================================

ROOT_URLCONF = "config.urls"


# =============================================================================
# TEMPLATES
# =============================================================================

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

                # Your custom context processors
                "apps.core.context_processors.site_context",
                "apps.core.context_processors.admin_dashboard",
            ],
        },
    },
]


# =============================================================================
# WSGI
# =============================================================================

WSGI_APPLICATION = "config.wsgi.application"


# =============================================================================
# DATABASE
# =============================================================================

DATABASES = {
    "default": dj_database_url.config(
        default=f"sqlite:///{BASE_DIR / 'db.sqlite3'}",
        conn_max_age=600,
    )
}


# =============================================================================
# SECURITY / HTTPS
# =============================================================================

SECURE_PROXY_SSL_HEADER = (
    "HTTP_X_FORWARDED_PROTO",
    "https",
)

SESSION_COOKIE_SECURE = not DEBUG

CSRF_COOKIE_SECURE = not DEBUG


# =============================================================================
# PASSWORD VALIDATION
# =============================================================================

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
            "NumericPasswordValidator"
        ),
    },
]


# =============================================================================
# INTERNATIONALIZATION
# =============================================================================

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# =============================================================================
# STATIC FILES
# =============================================================================

STATIC_URL = "static/"

STATIC_ROOT = BASE_DIR / "staticfiles"


# Django 5.x storage configuration
STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": (
            "whitenoise.storage."
            "CompressedManifestStaticFilesStorage"
        ),
    },
}


# =============================================================================
# DEFAULT PRIMARY KEY
# =============================================================================

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"