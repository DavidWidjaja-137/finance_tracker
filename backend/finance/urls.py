from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("account/", views.account, name="account"),
    path("transaction_type/", views.transaction_type, name="transaction_type"),
    path("transaction_category/", views.transaction_category, name="transaction_category"),
    path("insert_transaction_map/", views.insert_transaction_map, name="insert_transaction_map"),
    path("update_transaction_map/", views.update_transaction_map, name="update_transaction_map"),
    path("transaction_map/", views.transaction_map, name="transaction_map"),
    path("import_transaction/", views.import_transaction, name="import_transaction"),
    path("update_transaction/", views.update_transaction, name="update_transaction"),
    path("transaction/", views.transaction, name="transaction"),
    path("transaction_file_downloader/", views.transaction_file_downloader, name="transaction_file_downloader"),
    path("download_transaction_file/", views.download_transaction_file, name="download_transaction_file"),
]
