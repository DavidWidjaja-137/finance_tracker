# Finance Tracker

A simple finance tracker for personal savings, investments, and expenditures.

## Features In Progress
- Replace the local postgres database with a managed postgres database
- Deploy the site using AWS Elastic Beanstalk.

## Features in Discovery

### Develop flashy new UI using React/React Native

Make the UI beautiful using a SPA framework like Vue and create a mobile frontend for Android using the Android SDK, 
or do it in React/React Native.

### Add budgeting capability

It isn't great that I can only get feedback on my finances at month's end. I want to check how my finances are
on a day-to-day basis. I get receipts for my purchases, and insert them into the app as a kind of 
'intermediate transaction', which are also associated with transaction types.

I want to be able to see if I am definitely overbudget by the end of the month, or probably overbudget within the 
month. That means I need to set budgets. A 'default budget' is the one set on a category or subcategory when there is no
appropriate monthly target. A 'time budget' is one set for a specific year or month. More specific budgets override less
specific budgets.

Create a budget model and a budget view. The budget has the fields:
- name: what the budget is meant to do
- description: what the budget is for
- category: what category of spending does this budget go into?
- amount: how much is this budget?
- budget_type: what type of budget is this?
- start_date
- end_date
- user: whose budget is this?

For each user, create an 'intermediate transaction' view. Users can log and categorize intermediate purchases throughout
the month, without the rigour of full transactions. 

Create an IntermediateTransaction model and view, with the following fields:
- name: what is this intermediate transaction?
- date: when did this transaction happen?
- type: what type is this transaction?
- user: whose intermediate transaction is this?

Then, whenever the budgeting page is get by a user, compare intermediate and full transactions with the budget model, for
the time period, and display budgeted-vs-actual statistics.

### Add capabiity to create virtual users with simulated financial scenarios.

This will help me answer several questions, like:
- If I had x kids, or have a mortgage for a house, or a savings or philantrophic goal, how much money will I need
to earn to fulfil my combined obligations and goals?
- If I was laid off or had to do a job with reduced pay, how much time do I have?
- How is the regular person living, with their salary and expenditures? What can they possibly buy
over the month or save up over a period of time?

It might be a good idea to integrate the personal-data-dashboard into this finance tracker. 

