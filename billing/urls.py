from django.urls import path
# from django.views.generic import TemplateView
from . import views
# from .views import Index


app_name = "billing"

urlpatterns = [
    path("", views.Index.as_view(), name="index")
    # path("", TemplateView.as_view(template_name="billing/index.html"))
    # path('', views.index, name='index'),
]
