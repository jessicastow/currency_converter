# Currency converter

This code was written to fulfill the need at Bilou Beach Villas for a currency converter.

### The problem
The guests at Bilou Beach Villas come from all corners of the globe and thus the owners receive online payments via TransferWise in multiple different currencies. 
The quotes are given in USD, so the received currency needs to be converted to USD to keep an accurate account of the amounts still owed.
This is a challenge because the exchange rates are constantly fluctuating. 
The owner uses online tables to convert currencies for historical dates, however, this is an inefficient method of currency conversion. 

In order to save time, I developed a [python script](https://github.com/jessicastow/currency_converter/blob/main/currency_converter_v1.py) to convert between currencies. 

### Source
This code was inspired by [Turtle Code's video "Make Currency App - Python API](https://www.youtube.com/watch?v=isx6SpxZ4y0), I used his code as a base and improved on it. 

### API
I used the https://fixer.io/ API for currency conversion, it has access to information about 170 currencies and their exchange rates. 

