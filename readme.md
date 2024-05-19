# Finance Tracker

A simple finance tracker for personal savings, investments, and expenditures

Next todos:
- create an importer and django interface to fill in old transactions

an importer script that takes in an account and a month-year.
it retrieves the file from s3 according to the parameters, parses it, and writes the transaction
if the transaction is unreconciled, just import it as unreconciled.
