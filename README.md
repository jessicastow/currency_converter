# Currency converter 💱 💸 🌴

This code was written to fulfill the need at [Bilou Beach Surf Resorts](https://www.biloubeach.com/) for a currency converter.

### The problem
The guests at Bilou Beach Villas come from all corners of the globe and thus the owners receive online payments via TransferWise in multiple different  currencies (AUD, EUR, GBP, etc.). 
The guests are quoted in USD. The currency received needs to be converted to USD on the date of payment to keep an accurate account of the amounts still owed.
This is a challenge because the exchange rates are constantly fluctuating. 
The owner uses online tables to convert currencies for historical payment dates. However, this is an inefficient method of currency conversion as the resort owners need to scroll through pages of historical data. 

In order to save time, I developed a [python script](https://github.com/jessicastow/currency_converter/blob/main/currency_converter_v1.py) to convert between currencies on the date of payment using historical data, using the [Fixer.io API](https://fixer.io/). 

### 💡 Source
This code was inspired by [Turtle Code's video "Make Currency App - Python API](https://www.youtube.com/watch?v=isx6SpxZ4y0), I used his code as a base and improved on it. 

### 🌐 API
I used the https://fixer.io/ API for currency conversion, it has access to information about 170 currencies and their exchange rates. 

### My solution, explained

My code made use of the following variables and arguments:

- `from_currency`: Currency we are wanting to convert from (input). The user will be asked to enter their currency. 
- `to_currency`: Currency we are wanting to convert to (output). The user will be asked to enter their currency. 
- `amount`: The amount the user would like to convert
- `date`: The date the user would like the conversion for.
- `today`: argument to see whether the user would like the most recent (today/latest) conversion or if they want to use historical information. 
- `URL`: 
- `response`:
- `rate`:
- `again`: Asks the user whether they would like to do another conversion. 

### Notes


1. Add a 'list_of_currencies' - list of accepted currencies for the API, if inputs don't match this list print error "invalid currency"

2. Code not working for historical dates? Fix this issue...
