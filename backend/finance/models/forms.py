from django.forms import ModelForm, SelectDateWidget

from finance.models import Account, TransactionType, TransactionCategory, TransactionMap, Transaction


class AccountForm(ModelForm):
    class Meta:
        model = Account
        fields = ["name", "description"]


class TransactionTypeForm(ModelForm):
    class Meta:
        model = TransactionType
        fields = ["name", "description", "category"]


class TransactionCategoryForm(ModelForm):
    class Meta:
        model = TransactionCategory
        fields = ["name", "description"]


class TransactionMapForm(ModelForm):
    class Meta:
        model = TransactionMap
        fields = ["name", "description", "type"]


class TransactionForm(ModelForm):
    class Meta:
        model = Transaction
        fields = ["date", "account", "mapping", "amount", "flow"]
        widgets = {
            "date": SelectDateWidget(),
        }
