"""
Production settings for A.P. TECHNOCARE.

Used when deploying the Django application to Render.
"""

from .base import *


# =============================================================================
# PRODUCTION
# =============================================================================

DEBUG = False


# =============================================================================
# ALLOWED HOSTS
# =============================================================================

# base.py already reads ALLOWED_HOSTS from the environment.
#
# If ALLOWED_HOSTS is not set in Render, base.py uses:
# localhost
# 127.0.0.1
# .onrender.com
#
# Therefore we do not need env.list() here.


# =============================================================================
# CSRF TRUSTED ORIGINS
# =============================================================================

# base.py already reads CSRF_TRUSTED_ORIGINS from the environment.
#
# Default:
# https://*.onrender.com


# =============================================================================
# HTTPS / SECURITY
# =============================================================================

SECURE_PROXY_SSL_HEADER = (
    "HTTP_X_FORWARDED_PROTO",
    "https",
)

# Redirect HTTP requests to HTTPS.
SECURE_SSL_REDIRECT = True

# Secure cookies
SESSION_COOKIE_SECURE = True

CSRF_COOKIE_SECURE = True


# =============================================================================
# HTTP SECURITY HEADERS
# =============================================================================

# HTTP Strict Transport Security
SECURE_HSTS_SECONDS = 31536000

SECURE_HSTS_INCLUDE_SUBDOMAINS = True

SECURE_HSTS_PRELOAD = True

# Prevent MIME-type sniffing
SECURE_CONTENT_TYPE_NOSNIFF = True

# Referrer policy
SECURE_REFERRER_POLICY = "strict-origin-when-cross-origin"


# =============================================================================
# STATIC FILES
# =============================================================================

STATIC_ROOT = BASE_DIR / "staticfiles"