# Finance Tracker

A simple finance tracker for personal savings, investments, and expenditures.

## Features in Development
- I want to only display a filtered selection of transactions and transaction mappings. When a page
is loaded, no transactions or mappings should be loaded. There should be a form to select appropriate
filters. When the form is submitted, a GET request reloads the page with search parameters to load the
appropriate records.
- A single transaction mapping, when first created by a transaction, can be in an unreconciled state.
Have a filtered list of all unreconciled parameters, which can be selected in a form. When the form is
submitted, display all the transactions associated with that mapping. Another form allows the transaction
mapping to be associated with a different transaction type, thus changing the categorization of all 
associated transactions
- Have a way to disentangle a transaction from a transaction mapping. For example, a restaurant can be 
visited as both a social transaction and a family transaction. First, loosen the uniqueness constraint
on the transaction mapping so that only the combination of (name, type) must be unique. Then, allow additional
types to be associated to the same name. Create a form to filter for transactions from a combination of 
account, date range, and type. Then, create a form to select a transaction and assign it to a new transaction 
type. This creates an additional transaction mapping with the same name, but a different type.
- Add the ability to upload transaction files, with validation.

## Potential Features
- Use Django's authentication system.
- Replace the SQLite database with a local postgres database
- Replace the local postgres database with a managed postgres database
- Deploy the site using AWS Elastic Beanstalk.
- Make the UI beautiful using a SPA framework like Vue
- Create a mobile frontend for Android using the Android SDK.

## Thoughts
It isn't great that I can only get feedback on my finances at month's end. I want to check how my finances are
on a day-to-day basis. I get receipts for my purchases, and insert them into the app as a kind of 
'intermediate transaction', which are also associated with transaction types.

I want to be able to see if I am definitely overbudget by the end of the month, or probably overbudget within the 
month. THat means I need to set budgets. A 'default budget' is the one set on a category or subcategory when there is no
appropriate monthly target. A 'time budget' is one set for a specific year or month. More specific budgets override less
specific budgets.

Other questions I would like to answer:
- If I had x kids, or have a mortgage for a house, or a savings or philantrophic goal, how much money will I need
to earn to fulfil my combined obligations and goals?
- If I was laid off or had to do a job with reduced pay, how much time do I have?
- How is the regular person living, with their salary and expenditures? What can they possibly buy
over the month or save up over a period of time?

It might be a good idea to integrate the personal-data-dashboard into this finance tracker. 

