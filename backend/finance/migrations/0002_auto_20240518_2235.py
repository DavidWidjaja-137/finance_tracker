import json
import os

from django.db import migrations


def create_default_accounts(apps, schema_editor):

    Account = apps.get_model("finance", "Account")

    Account.objects.get_or_create(name="CTFS_CREDIT", description="Canadian Tire Financial Services Credit Card")
    Account.objects.get_or_create(name="SCOTIABANK_CHEQUING", description="Scotiabank Chequing Account")
    Account.objects.get_or_create(name="SCOTIABANK_CREDIT", description="Scotiabank Credit Card Account")
    Account.objects.get_or_create(name="SCOTIABANK_SAVINGS", description="Scotiabank Savings Account")
    Account.objects.get_or_create(name="VANCITY_CHEQUING", description="Vancity Chequing Account")
    Account.objects.get_or_create(name="VANCITY_CREDIT", description="Vancity Credit Card Account")
    Account.objects.get_or_create(name="VANCITY_SAVINGS", description="Vancity Savings Account")
    Account.objects.get_or_create(name="CREDENTIAL_ASSET_MANAGEMENT", description="Credential Asset Management Account")


def create_default_transaction_categories(apps, schema_editor):

    TransactionCategory = apps.get_model("finance", "TransactionCategory")

    TransactionCategory.objects.get_or_create(name="UNRECONCILED", description="Unreconciled Transactions")
    TransactionCategory.objects.get_or_create(name="SALARY", description="Income from salary")
    TransactionCategory.objects.get_or_create(name="TAX_RETURN", description="Income and deductions from tax returns")
    TransactionCategory.objects.get_or_create(name="RENT", description="Support your local landlord")
    TransactionCategory.objects.get_or_create(name="GROCERY", description="Payments for groceries")
    TransactionCategory.objects.get_or_create(name="UTILITY", description="Payments for groceries")
    TransactionCategory.objects.get_or_create(name="SOCIAL", description="Expenses from social activities")
    TransactionCategory.objects.get_or_create(
        name="SUBSCRIPTION", description="Subscriptions to various digital and print services"
    )
    TransactionCategory.objects.get_or_create(name="LEARNING", description="Expenses to learn new things")
    TransactionCategory.objects.get_or_create(name="LUXURY", description="Expenses on luxury and quality-of-life items")
    TransactionCategory.objects.get_or_create(
        name="CHARITY", description="Donations to charitable organizations, activism, and mutual aid"
    )
    TransactionCategory.objects.get_or_create(
        name="BANKING", description="Banking expenses, fees and internal transfers"
    )
    TransactionCategory.objects.get_or_create(name="INVESTMENT", description="Investment income and losses")
    TransactionCategory.objects.get_or_create(
        name="FAMILY", description="Financial Transactions made by or behalf of family"
    )


def create_default_transaction_types(apps, schema_editor):

    TransactionCategory = apps.get_model("finance", "TransactionCategory")
    TransactionType = apps.get_model("finance", "TransactionType")

    # unreconciled
    TransactionType.objects.get_or_create(
        name="UNRECONCILED",
        description="Unreconciled transactions",
        category=TransactionCategory.objects.get(name="UNRECONCILED"),
    )

    # salary
    TransactionType.objects.get_or_create(
        name="SALARY_JOB",
        description="Income transactions from a job",
        category=TransactionCategory.objects.get(name="SALARY"),
    )

    # investment
    TransactionType.objects.get_or_create(
        name="INVESTMENT",
        description="Money obtained from by sitting on money",
        category=TransactionCategory.objects.get(name="INVESTMENT"),
    )

    # tax return
    TransactionType.objects.get_or_create(
        name="TAX_RETURN",
        description="Net amount from a tax return",
        category=TransactionCategory.objects.get(name="TAX_RETURN"),
    )

    # rent
    TransactionType.objects.get_or_create(
        name="RENT", description="Support your local landlord", category=TransactionCategory.objects.get(name="RENT")
    )
    TransactionType.objects.get_or_create(
        name="RENT_FIRST_NATIONS",
        description="Voluntary rent payments for living on unceded, traditional territory",
        category=TransactionCategory.objects.get(name="RENT"),
    )

    # grocery
    TransactionType.objects.get_or_create(
        name="GROCERY",
        description="Expenditures on getting the bread",
        category=TransactionCategory.objects.get(name="GROCERY"),
    )

    # utility
    TransactionType.objects.get_or_create(
        name="UTILITY_TRANSPORT",
        description="Expenses for everyday personal transit",
        category=TransactionCategory.objects.get(name="UTILITY"),
    )
    TransactionType.objects.get_or_create(
        name="UTILITY_INTERNET",
        description="Expenses for internet services",
        category=TransactionCategory.objects.get(name="UTILITY"),
    )
    TransactionType.objects.get_or_create(
        name="UTILITY_CELLULAR",
        description="Expenses for cellular services",
        category=TransactionCategory.objects.get(name="UTILITY"),
    )
    TransactionType.objects.get_or_create(
        name="UTILITY_WATER", description="Expenses for water", category=TransactionCategory.objects.get(name="UTILITY")
    )
    TransactionType.objects.get_or_create(
        name="UTILITY_ELECTRICITY",
        description="Expenses for electricity",
        category=TransactionCategory.objects.get(name="UTILITY"),
    )
    TransactionType.objects.get_or_create(
        name="UTILITY_MAINTENANCE",
        description="Expenses to do home maintenance",
        category=TransactionCategory.objects.get(name="UTILITY"),
    )

    # subscription
    TransactionType.objects.get_or_create(
        name="SUBSCRIPTION_ENTERTAINMENT",
        description="Subscriptions for entertainment",
        category=TransactionCategory.objects.get(name="SUBSCRIPTION"),
    )
    TransactionType.objects.get_or_create(
        name="SUBSCRIPTION_NEWS",
        description="Subscriptions for news",
        category=TransactionCategory.objects.get(name="SUBSCRIPTION"),
    )
    TransactionType.objects.get_or_create(
        name="SUBSCRIPTION_UTILITY",
        description="Subscriptions for digital utilities",
        category=TransactionCategory.objects.get(name="SUBSCRIPTION"),
    )

    # learning
    TransactionType.objects.get_or_create(
        name="LEARNING_BOOKS",
        description="Money spent on buying books",
        category=TransactionCategory.objects.get(name="LEARNING"),
    )
    TransactionType.objects.get_or_create(
        name="LEARNING_LESSONS", description="Lesson fees", category=TransactionCategory.objects.get(name="LEARNING")
    )
    TransactionType.objects.get_or_create(
        name="LEARNING_EQUIPMENT",
        description="Expenses for equipment necessary to learning",
        category=TransactionCategory.objects.get(name="LEARNING"),
    )
    TransactionType.objects.get_or_create(
        name="LEARNING_CERTIFICATIONS",
        description="Fees to get certified",
        category=TransactionCategory.objects.get(name="LEARNING"),
    )

    # charity
    TransactionType.objects.get_or_create(
        name="CHARITY_HUMANITARIAN",
        description="Global humanitarian aid",
        category=TransactionCategory.objects.get(name="CHARITY"),
    )
    TransactionType.objects.get_or_create(
        name="CHARITY_ENVIRONMENT",
        description="Environmental conservation and activism",
        category=TransactionCategory.objects.get(name="CHARITY"),
    )
    TransactionType.objects.get_or_create(
        name="CHARITY_LOCAL",
        description="Local charities and local issues",
        category=TransactionCategory.objects.get(name="CHARITY"),
    )
    TransactionType.objects.get_or_create(
        name="CHARITY_MUTUAL",
        description="Mutual aid around the world",
        category=TransactionCategory.objects.get(name="CHARITY"),
    )
    TransactionType.objects.get_or_create(
        name="CHARITY_INTERNET",
        description="Donations for open source and a free internet",
        category=TransactionCategory.objects.get(name="CHARITY"),
    )

    # social
    TransactionType.objects.get_or_create(
        name="SOCIAL_FOOD",
        description="Getting food and drink for social and recreational purposes",
        category=TransactionCategory.objects.get(name="SOCIAL"),
    )
    TransactionType.objects.get_or_create(
        name="SOCIAL_OTHER",
        description="Other expenditures for social purposes",
        category=TransactionCategory.objects.get(name="SOCIAL"),
    )

    # luxury
    TransactionType.objects.get_or_create(
        name="LUXURY",
        description="Stuff I don't need but I want",
        category=TransactionCategory.objects.get(name="LUXURY"),
    )

    # banking
    TransactionType.objects.get_or_create(
        name="BANKING_INTERNAL_TRANSFERS",
        description="Internal transfers from one bank account to another",
        category=TransactionCategory.objects.get(name="BANKING"),
    )
    TransactionType.objects.get_or_create(
        name="BANKING_WITHDRAWALS",
        description="Withdrawing money from an ATM machine",
        category=TransactionCategory.objects.get(name="BANKING"),
    )
    TransactionType.objects.get_or_create(
        name="BANKING_SERVICE_CHARGES",
        description="Service charges for banking",
        category=TransactionCategory.objects.get(name="BANKING"),
    )
    TransactionType.objects.get_or_create(
        name="BANKING_CREDIT_CARD_INTEREST",
        description="Credit card interest",
        category=TransactionCategory.objects.get(name="BANKING"),
    )

    # family
    TransactionType.objects.get_or_create(
        name="FAMILY_UNRECONCILED",
        description="Any unreconciled family stuff",
        category=TransactionCategory.objects.get(name="FAMILY"),
    )
    TransactionType.objects.get_or_create(
        name="FAMILY_HOLIDAY",
        description="Stuff I buy for a family holiday",
        category=TransactionCategory.objects.get(name="FAMILY"),
    )
    TransactionType.objects.get_or_create(
        name="FAMILY_GIFT",
        description="Stuff I buy for families",
        category=TransactionCategory.objects.get(name="FAMILY"),
    )
    TransactionType.objects.get_or_create(
        name="FAMILY_SUPPORT",
        description="Mutual support and equalization fees",
        category=TransactionCategory.objects.get(name="FAMILY"),
    )


def create_initial_transaction_mappings(apps, schema_editor):

    TransactionCategory = apps.get_model("finance", "TransactionMap")
    TransactionType = apps.get_model("finance", "TransactionType")

    with open(os.path.join(os.path.dirname(__file__), "initial_transaction_mappings.json"), "r") as f:

        initial_mappings = json.load(f)

        for category, types in initial_mappings.items():
            for type, names in types.items():
                for name in names:
                    TransactionCategory.objects.get_or_create(
                        name=name,
                        description="Initial transaction mapping set",
                        type=TransactionType.objects.get(name=type),
                    )


class Migration(migrations.Migration):

    dependencies = [
        ("finance", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(create_default_accounts),
        migrations.RunPython(create_default_transaction_categories),
        migrations.RunPython(create_default_transaction_types),
        migrations.RunPython(create_initial_transaction_mappings),
    ]
