from django.conf import settings
from django.contrib import admin
from django.urls import include, path, re_path
from django.http import HttpResponse
from django.views.static import serve


def render_test(request):
    return HttpResponse(
        "Django is running | ROOT_URLCONF=config.urls | Production settings loaded"
    )


urlpatterns = [
    path(
        "render-test/",
        render_test,
    ),

    path(
        "admin/",
        admin.site.urls,
    ),

    path(
        "",
        include("apps.catalog.urls"),
    ),

    path(
        "",
        include("apps.core.urls"),
    ),

    path(
        "",
        include("apps.enquiries.urls"),
    ),
]


# Serve media files on Render
urlpatterns += [
    re_path(
        r"^media/(?P<path>.*)$",
        serve,
        {
            "document_root": settings.MEDIA_ROOT,
        },
    ),
]