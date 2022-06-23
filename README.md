# SuperSimpleStockMarket


Description:

The source code that will -
- For a given stock,
    - For a given price as input, calculate the dividend yield
    - For a given price as input, calculate the P/E Ratio
    - Record a trade, with timestamp, quantity, buy or sell indicator and price
    - Calculate Volume Weighted Stock Price based on trades in past 5 minutes
- Calculate the GBCE All Share Index using the geometric mean of prices for all stocks

Constraints & Notes:

1. No database, GUI or I/O is required, all data need only be held in memory
2. No prior knowledge of stock markets or trading is required – all formulas are provided below.
3. The code should provide only the functionality requested, however it must be production quality.

Global Beverage Corporation Exchange

| Stock Symbol | Type      | Last Dividend | Fixed Dividend | Par Value |
|--------------|-----------|--------------:|:--------------:|----------:|
| TEA          | Common    |             0 |                |       100 |
| POP          | Common    |             8 |                |       100 |
| ALE          | Common    |            23 |                |        60 |
| GIN          | Preferred |             8 |       2%       |       100 |
| JOE          | Common    |            13 |                |       250 |

Requirements:

- Python 3.6 or higher
- pandas libraries of python


Information:

1. "gbce_stock_info.csv" is a file that is used for custom stock information. If the file is not present, the program will use default stock information that is present in memory.
2. "record_ledger.txt" is used to when the user wants to record the trade to file and memory as well. Otherwise, the trade will be to recorded to memory only. By default, it records to file and memory

To run the application, type in console window:
```
python3 main.py
```

Example output on console window:

If using the gbce_stock_info.csv file:-
```
Reading from /Users/puskardeb/Codes/python/PycharmProjects/SuperSimpleStockMarket/files/gbce_stock_info.csv...
```

Else if using the default stock info:-
```
Reading from default stock info in memory ...
{('ALE', 'common', '23', '', '60'),
 ('GIN', 'preferred', '8', '2', '100'),
 ('JOE', 'common', '13', '', '250'),
 ('POP', 'common', '8', '', '100'),
 ('TEA', 'common', '0', '', '100')}
```

```
Please select an option as per choice:-
1 for calculating dividend yield.
2 for calculating P/E ratio.
3 for recording trade.
4 for calculating Volume Weighted Stock Price.
5 for calculating the GBCE All Share Index.
0 for exiting...

Enter option:
```

Tests:

To test the assignment using unittest, type in console window:-

```
python3 test.py
```
