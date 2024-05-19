from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("account/", views.account, name="account"),
    path("transaction_type/", views.transaction_type, name="transaction_type"),
    path("transaction_category/", views.transaction_category, name="transaction_category"),
    path("transaction_map/", views.transaction_map, name="transaction_map"),
    path("transaction/", views.transaction, name="transaction"),
]
