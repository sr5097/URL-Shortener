from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.

def shortener_redirect_views(request, *args, **kwargs):
    return HttpResponse("hello")

class ShortenerRedirectView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("hello again")