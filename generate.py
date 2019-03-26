import random
from account import Account, db
from faker import Faker



def fake_account_number():
    account_number = random.randint(100000, 999999)
    while Account.query.filter_by(account_number=account_number).first() != None:
        account_number = random.randint(100000, 999999)
    return account_number


def fake_pin():
    # This will give me a 3 digits random number.
    return random.randint(100, 999)

def fake_balance():
   
    return random.randint(0, 1000)


def fake_account():
    return Account(account_number=fake_account_number(),
        pin = fake_pin(),
        balance = fake_balance()
    )


# This will generate so many accounts you want. By saying the max_n
def generate_accounts(max_n):
    for n in range(max_n):
        account = fake_account()
        db.session.add(account)

    db.session.commit()



def add_name():
    # We call the built in function Faker That creates fake info.
    fake = Faker()
    # Fetching the data and storing it.
    accounts = Account.query.all():
    # Loop thru the list.
    for account in accounts
        # Adding in the names to Sql.
        account.name = fake.name()
        # account.ccexp = fake.credit_card_expire(start='now', end='+10y',date_format="%m/%y")
       # account.cvv = fake.credit_card_security_code()
    db.session.commit()



def add_cc():
    fake = Faker()
    for account in Account.query.all():
        # Adding the credit card details.
        account.credit_card = fake.credit_card_number()
    db.session.commit()



# generate_accounts(1000)
# add_name()
# add_cc()





# Create a script to generate 1,000 accounts -- Done
# Each account has a 6 digits account number -- Done
# 3 digits PIN  -- Done
# a balance between 0 and 10,000 -- Done
#https://faker.readthedocs.io/en/master/
# For tomorrow
# Using Faker (https://faker.readthedocs.io/en/master/)
# Add a name to each of your accounts in the database -- DONE
# NB: do not create new accounts, just add a name to the existing ones -- DONE
# BONUS: add credit card numbers with those accounts -- DONE
