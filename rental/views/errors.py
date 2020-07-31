from django.shortcuts import render


def handler404(request, _):
    """handle 404 errors. Requires a request and an exception."""
    return render(request, 'rental/404.html', status=404)


def handler500(request):
    """handle 500 errors."""
    return render(request, 'rental/500.html', status=500)
