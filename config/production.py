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
# If Render does not provide the variable, base.py falls back to:
# .onrender.com
#
# Therefore no additional ALLOWED_HOSTS configuration is required here.


# =============================================================================
# CSRF
# =============================================================================

# base.py already configures:
#
# https://*.onrender.com
#
# This allows Render's HTTPS domain.


# =============================================================================
# HTTPS / SECURITY
# =============================================================================

SECURE_PROXY_SSL_HEADER = (
    "HTTP_X_FORWARDED_PROTO",
    "https",
)

SESSION_COOKIE_SECURE = True

CSRF_COOKIE_SECURE = True


# =============================================================================
# STATIC FILES
# =============================================================================

STATIC_ROOT = BASE_DIR / "staticfiles"