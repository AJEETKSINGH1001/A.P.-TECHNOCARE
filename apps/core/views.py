from django.shortcuts import render


def home(request):
    return render(
        request,
        "core/home.html",
    )


def products_placeholder(request):
    return render(
        request,
        "core/placeholder.html",
        {
            "page_title": "Products",
            "page_description": (
                "Our product catalogue is being prepared."
            ),
        },
    )


def about_placeholder(request):
    return render(
        request,
        "core/placeholder.html",
        {
            "page_title": "About Us",
            "page_description": (
                "Company information will be connected to "
                "the content system in the next phase."
            ),
        },
    )


def contact_placeholder(request):
    return render(
        request,
        "core/placeholder.html",
        {
            "page_title": "Contact Us",
            "page_description": (
                "The enquiry and contact workflow will be "
                "implemented in the next phase."
            ),
        },
    )


def search_placeholder(request):
    query = request.GET.get("q", "").strip()

    return render(
        request,
        "core/placeholder.html",
        {
            "page_title": "Search",
            "page_description": (
                f'Search results for "{query}"'
                if query
                else "Search products and services."
            ),
        },
    )