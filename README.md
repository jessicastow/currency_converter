# Currency converter 💱 💸 🌴

This code was written to fulfill the need at [Bilou Beach Surf Resorts](https://www.biloubeach.com/) for a currency converter.

### The problem
The guests at Bilou Beach Villas come from all corners of the globe and thus the owners receive online payments via TransferWise in multiple different  currencies (AUD, EUR, GBP, etc.). 
The guests are quoted in USD. The currency received needs to be converted to USD on the date of payment to keep an accurate account of the amounts still owed.
This is a challenge because the exchange rates are constantly fluctuating. 
The owner uses online tables to convert currencies for historical payment dates. However, this is an inefficient method of currency conversion as the resort owners need to scroll through pages of historical data. 

In order to save time, I developed a [python script](https://github.com/jessicastow/currency_converter/blob/main/currency_converter_v1.py) to convert between currencies on the date of payment using historical data, using the [Fixer.io API](https://fixer.io/). 

### 💡 Source
This code was inspired by [Turtle Code's video "Make Currency App - Python API"](https://www.youtube.com/watch?v=isx6SpxZ4y0).

### 🌐 API
I used the https://fixer.io/ API for currency conversion, it has access to information about 170 currencies and their exchange rates. 

### 🏃‍♀️ Run
Click on this [link](https://trinket.io/python3/9aeeb653f0?outputOnly=true&runOption=run) to try out the program. (Please note this will only work on a desktop computer).

### My solution, explained

My code made use of the following variables and arguments:

- `base`: Currency we are wanting to convert from (input). The user will be asked to enter their currency. 
- `target`: Currency we are wanting to convert to (output). The user will be asked to enter their currency.
- Note: for `base` and `target` currencies, these need to be the three letter ISO currency code, e.g. South African Rands are abbreviated as 'ZAR'. The list of abbreviations for currencies can be found [here](https://www.countries-ofthe-world.com/world-currencies.html).
- `amount`: The amount the user would like to convert.
- `date`: The date the user would like the conversion for (in the format yyyy-mm-dd).
- `today`: argument to see whether the user would like the most recent (today/latest) conversion or if they want to use historical information. 
- `output`: The amount of the target currency. Calculated by multiplying the the input (base) amount and the rate of the target currency. 
- `again`: Asks the user whether they would like to do another conversion. If the user answers 'yes' then the script is run again, any other response will end the program. 

Any feedback on my solution is welcome! Email me: stowjess@gmail.com

### Notes/Updates to do...


1. Add a `list_of_currencies` - list of accepted currencies for the API, if `base` or `target` inputs don't match this list print error "Invalid currency"
