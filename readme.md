# Finance Tracker

A simple finance tracker for personal savings, investments, and expenditures.

## Features in Development
- generalize the logic for multiple users wooooooooo


each user should have a different set of everything. accounts, transactions, categories, types, maps.
however, the transactions, categories, types and maps should be shared among


## Potential Features
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

