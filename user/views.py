from django.shortcuts import render
from django.contrib.staticfiles.storage import staticfiles_storage

# Create your views here.


def index(request):
    return render(
        request, "index.html", {"index_url": staticfiles_storage.url("index.html")}
    )
