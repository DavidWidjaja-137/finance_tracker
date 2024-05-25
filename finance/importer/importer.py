import os
import csv
from datetime import date, datetime

from dateutil.relativedelta import relativedelta
from django.contrib.auth.models import User

from finance.models import Transaction, Account, TransactionMap, TransactionType

INFLOW = "INFLOW"
OUTFLOW = "OUTFLOW"


def create_transaction(
    d: date,
    month_start: date,
    month_end: date,
    transaction_name: str,
    account_name: str,
    amount: float,
    flow: str,
    user: User,
):

    if month_start <= d < month_end:

        # check if a mapping exists.
        # in the edge case that multiple transaction maps are available, just assign to the first one.
        if TransactionMap.objects.filter(name=transaction_name).exists():
            map = TransactionMap.objects.filter(name=transaction_name).first()
        else:
            map = TransactionMap.objects.create(
                name=transaction_name,
                description="Temporarily Unreconciled",
                type=TransactionType.objects.get(name="UNRECONCILED"),
            )

        Transaction.objects.get_or_create(
            date=d,
            account=Account.objects.get(name=account_name),
            mapping=map,
            amount=abs(amount),
            flow=flow,
            user=user,
        )


def import_transaction_from_vancity_credit(row: list[str], month_start: date, month_end: date, user: User):
    date = datetime.fromisoformat(row[2].strip()).date()
    transaction_name = str(row[4].strip())

    if row[6] != "":
        amount = float(row[6])
        transaction_flow = OUTFLOW
    else:
        amount = float(row[7])
        transaction_flow = INFLOW

    create_transaction(date, month_start, month_end, transaction_name, "VANCITY_CREDIT", amount, transaction_flow, user)


def import_transaction_from_vancity_chequing(row: list[str], month_start: date, month_end: date, user: User):
    date = datetime.strptime(row[1], "%d-%b-%Y").date()
    transaction_name = str(row[2].strip())

    if row[4] != "":
        amount = float(row[4])
        transaction_flow = OUTFLOW
    else:
        amount = float(row[5])
        transaction_flow = INFLOW

    create_transaction(
        date, month_start, month_end, transaction_name, "VANCITY_CHEQUING", amount, transaction_flow, user
    )


def import_transaction_from_vancity_savings(row: list[str], month_start: date, month_end: date, user: User):

    date = datetime.strptime(row[1], "%d-%b-%Y").date()
    transaction_name = str(row[2].strip())

    if row[4] != "":
        amount = float(row[4])
        transaction_flow = OUTFLOW
    elif row[5] != "":
        amount = float(row[5])
        transaction_flow = INFLOW
    else:
        amount = 0.0
        transaction_flow = INFLOW

    create_transaction(
        date, month_start, month_end, transaction_name, "VANCITY_SAVINGS", amount, transaction_flow, user
    )


def import_transaction_from_scotiabank_credit(row: list[str], month_start: date, month_end: date, user: User):
    month, day, year = row[0].split("/")
    date = datetime(int(year), int(month), int(day)).date()
    transaction_name = str(row[1].strip())
    amount = float(row[2])

    transaction_flow = OUTFLOW if amount < 0 else INFLOW

    create_transaction(
        date, month_start, month_end, transaction_name, "SCOTIABANK_CREDIT", amount, transaction_flow, user
    )


def import_transaction_from_scotiabank_chequing(row: list[str], month_start: date, month_end: date, user: User):
    month, day, year = row[0].split("/")
    date = datetime(int(year), int(month), int(day)).date()
    transaction_name = str(row[3].strip()) + " " + str(row[4].strip())
    amount = float(row[1])

    transaction_flow = OUTFLOW if amount < 0 else INFLOW

    create_transaction(
        date, month_start, month_end, transaction_name, "SCOTIABANK_CHEQUING", amount, transaction_flow, user
    )


def import_transaction_from_scotiabank_savings(row: list[str], month_start: date, month_end: date, user: User):
    date = datetime.fromisoformat(row[0].strip()).date()
    transaction_name = str(row[1].strip())
    amount = float(row[2].replace(",", ""))

    transaction_flow = INFLOW if amount > 0 else OUTFLOW

    create_transaction(
        date, month_start, month_end, transaction_name, "SCOTIABANK_CREDIT", amount, transaction_flow, user
    )


def import_transaction_from_credential_asset_management(row: list[str], month_start: date, month_end: date, user: User):
    date = datetime.fromisoformat(row[0].strip()).date()
    transaction_name = str(row[1].strip())
    amount = float(row[2].replace(",", ""))

    transaction_flow = INFLOW if amount > 0 else OUTFLOW

    create_transaction(
        date, month_start, month_end, transaction_name, "CREDENTIAL_ASSET_MANAGEMENT", amount, transaction_flow, user
    )


def import_transaction_from_ctfs_credit(row: list[str], month_start: date, month_end: date, user: User):
    date = datetime.fromisoformat(row[0].strip()).date()
    transaction_name = str(row[1].strip())
    amount = float(row[2].replace(",", ""))

    transaction_flow = OUTFLOW if amount > 0 else INFLOW

    create_transaction(date, month_start, month_end, transaction_name, "CTFS_CREDIT", amount, transaction_flow, user)


def import_transaction_from_account(
    row: list[str], statement_source: str, month_start: date, month_end: date, user: User
):
    if statement_source == "CTFS_CREDIT":
        return import_transaction_from_ctfs_credit(row, month_start, month_end, user)
    elif statement_source == "SCOTIABANK_CHEQUING":
        return import_transaction_from_scotiabank_chequing(row, month_start, month_end, user)
    elif statement_source == "SCOTIABANK_CREDIT":
        return import_transaction_from_scotiabank_credit(row, month_start, month_end, user)
    elif statement_source == "SCOTIABANK_SAVINGS":
        return import_transaction_from_scotiabank_savings(row, month_start, month_end, user)
    elif statement_source == "VANCITY_CHEQUING":
        return import_transaction_from_vancity_chequing(row, month_start, month_end, user)
    elif statement_source == "VANCITY_CREDIT":
        return import_transaction_from_vancity_credit(row, month_start, month_end, user)
    elif statement_source == "VANCITY_SAVINGS":
        return import_transaction_from_vancity_savings(row, month_start, month_end, user)
    elif statement_source == "CREDENTIAL_ASSET_MANAGEMENT":
        return import_transaction_from_credential_asset_management(row, month_start, month_end, user)
    else:
        raise ValueError(f"{statement_source} does not exist")


def import_transactions_from_local_file(
    statement_source: str, file_month: date, month_start: date, month_end: date, user: User
):

    prefix = os.path.join(os.path.dirname(__file__), "..", "..", "..", "data")
    suffix = f"{statement_source}/{file_month.isoformat()}.csv"
    key = os.path.join(prefix, suffix)

    if os.path.exists(key) is False:
        return None

    with open(key, newline="") as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        for row in reader:
            import_transaction_from_account(row, statement_source, month_start, month_end, user)


def import_transactions_from_source(statement_source: str, start: date, end: date, user: User):

    # delete all transactions for the month first
    deleted, _ = Transaction.objects.filter(
        user=user, account__name=statement_source, date__range=(start, end)
    ).delete()

    print(f"Deleted from {statement_source}: {deleted}")

    import_transactions_from_local_file(statement_source, start - relativedelta(months=1), start, end, user)

    loop_start = start
    while loop_start < end:
        import_transactions_from_local_file(
            statement_source, loop_start, loop_start, loop_start + relativedelta(months=1), user
        )
        loop_start += relativedelta(months=1)

    import_transactions_from_local_file(statement_source, end, start, end, user)


def import_transactions(start: date, end: date, user: User):

    for account in Account.objects.all():
        import_transactions_from_source(account.name, start, end, user)
