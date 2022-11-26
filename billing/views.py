# from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, billing index.")


# Create your views here.
class Index(TemplateView):
    template_name = "billing/index.html"
