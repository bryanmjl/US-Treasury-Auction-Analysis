# US treasury auction webscrape


## A. Overview
Auction results of U.S. Treasury marketable securities are released on TreasuryDirect website at https://www.treasurydirect.gov/auctions/announcements-data-results/announcement-results-press-releases/

Through creating an automated selenium bot, we can periodically webscrape auction results for a year and this can be used for analysis in demand of securities, which can be good indicators of how well the economy is peforming.

Therefore, we can start by downloading auction results from 2022-01-01 to 2022-12-31, for all terms of Bill and Notes from competitive auctions


## B. File Directory Layout
1. ```webscrape_results``` 
    - Folder which contains webscraped results of 2022 Bills and Notes auction results competitive
    - ```webscrape_results/bill_URLs_2022.csv``` 
    - ```webscrape_results/note_URLs_2022.csv```
2. ```Helper.py```
    - Python .py file containing helper functions needed
    - ```get_2022_bills_webscrape```
    - ```get_2022_notes_webscrape```
    - ```parse_xml```
3. ```Main.ipynb```
    - Main file for analysis of our auction results (Please see this file for more details)

## C. References
1. https://www.treasurydirect.gov/auctions/how-auctions-work/#:~:text=At%20the%20auction%2C%20Treasury%20first,the%20offering%20has%20been%20awarded.
2. https://www.treasurydirect.gov/marketable-securities/treasury-bills/
3. https://www.treasurydirect.gov/marketable-securities/treasury-notes/
