import requests

print('This program converts currencies on your date of choice.')


def currency_conversion():
    from_currency = str(input("Currency you'd like to convert from:")).upper().strip()
    to_currency   = str(input("Currency you'd like to convert to:")).upper().strip()
    amount = int(input("Amount you'd like to convert:"))

    date = None
    today = str(input("Would you like to use today's conversion rate?")).lower().strip()

    if today == 'yes':
        date = 'latest'
    else:
        date = input("Insert date which you'd like to do the conversion for (format: yyyy-mm-dd)")
        # print(date) # test

    URL = str('http://data.fixer.io/api/' + date + '?access_key=WjcLO0j3I9Nn0aGdiYXyEo1tr6t2LzfC')

    response = requests.get(URL)
    rate = response.json()['rates'][from_currency]
    amount_in_EUR = amount/rate
    amount = amount_in_EUR*(response.json()['rates'][to_currency])
    amount = round(amount,2)
    print(amount)
    again = input('Again?:').lower().strip()
    if again == 'yes':
        currency_conversion()

currency_conversion()

# Notes

# Add a 'list_of_currencies' - list of accepted currencies for the API,
# if inputs don't match this list print error "invalid currency"

# add an option for using historical dates
