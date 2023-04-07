import requests

print('This program converts currencies on your date of choice.')

def currency_converter():
    base = str(input("Currency you'd like to convert from:")).upper().strip()
    target   = str(input("Currency you'd like to convert to:")).upper().strip()
    amount = int(input("Amount you'd like to convert:"))

    date = None
    today = str(input("Would you like to use today's conversion rate?")).lower().strip()
    if today == 'yes':
        date = 'latest'
    else:
        date = input("Insert date which you'd like to do the conversion for (format: yyyy-mm-dd)")
        # print(date) # test

    url = "https://api.apilayer.com/fixer/" + date + "?symbols=" + target +"&base=" + base

    payload = {}
    headers= {
    "apikey": "WjcLO0j3I9Nn0aGdiYXyEo1tr6t2LzfC"
    }

    response = requests.request("GET", url, headers=headers, data = payload)

    status_code = response.status_code
    result = response.json()['rates'][target]

    output = amount*result
    output = round(output, 2)

    if date == 'latest':
        print('Today,', amount, base, "is equal to", output, target)
    else:
        print("On", date, amount, base, "was equal to", output, target)

    again = input('Again?:').lower().strip()
    if again == 'yes':
        currency_converter()

currency_converter()


# Notes

# Add a 'list_of_currencies' - list of accepted currencies for the API,
# if inputs don't match this list print error "invalid currency"
