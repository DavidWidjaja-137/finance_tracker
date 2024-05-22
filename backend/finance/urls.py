from django.urls import path

from finance import views
from finance.views import (
    AccountView,
    TransactionTypeView,
    TransactionCategoryView,
    UpdateTransactionMapView,
    TransactionMapView,
    UpdateTransactionView,
    ImportTransactionView,
    TransactionView,
    TransactionFileView,
)

urlpatterns = [
    path("", views.index, name="index"),
    path("account/", AccountView.as_view(), name="account"),
    path("transaction_type/", TransactionTypeView.as_view(), name="transaction_type"),
    path("transaction_category/", TransactionCategoryView.as_view(), name="transaction_category"),
    path("update_transaction_map/", UpdateTransactionMapView.as_view(), name="update_transaction_map"),
    path("transaction_map/", TransactionMapView.as_view(), name="transaction_map"),
    path("update_transaction/", UpdateTransactionView.as_view(), name="update_transaction"),
    path("import_transaction/", ImportTransactionView.as_view(), name="import_transaction"),
    path("transaction/", TransactionView.as_view(), name="transaction"),
    path("transaction_file_downloader/", TransactionFileView.as_view(), name="transaction_file_downloader"),
]
