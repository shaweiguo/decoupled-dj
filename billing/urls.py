from django.urls import path
# from django.views.generic import TemplateView
from . import views
from .api import views as api


app_name = "billing"

urlpatterns = [
    path("", views.Index.as_view(), name="index"),
    # path("", TemplateView.as_view(template_name="billing/index.html"))
    # path('', views.index, name='index'),
    path("api/clients/", api.ClientList.as_view(), name="client-list"),
    path("api/invoices/", api.InvoiceCreate.as_view(), name="invoice-create"),
]
