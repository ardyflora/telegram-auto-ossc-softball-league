# telegram-auto-ossc-softball-league

> A Telegram bot that gives you the up to date ossc softball league scores.

Some of the cool features:
* **/fixture** - List the date, team, time, place and diamond location from current week till end of league

Please refer to screenshots below to see `telegram-auto-ossc-softball-league` in action:

###### `/fixture` in action
<img src="https://snag.gy/jSpkHF.jpg" width="600">

## Benefits
* You don't have to login to OSSC website each and everytime to check which game is this week and what's the location.
* Easier to check which team you are playing against this week and what time game is at.


## Features to be added
* `/timePlace` - will give time and location for this week game with date
* `/team` - which team you will be facing this week and where do they stand
* `/rank` - will display team ranking for the league
* `/points` - will give points for the league

## Installation
* You will need to install python telegram bot
  * Please follow the link:  
    https://github.com/python-telegram-bot/python-telegram-bot
* PrettyTable - Which is used to display the result as shown in the **telegram-auto-ossc-softball-league screenshot** above
   * To install PrettyTable, Please follow: https://pypi.python.org/pypi/PrettyTable
* selenium - which is used to scrape ossc website
   * To install selenium, Please follow: http://selenium-python.readthedocs.io/installation.html

## How to Execute?
* `python scrapeSoftballOsscData.py` - Scrapes the information from the ossc website and displays it as shown in the screenshot above.


## Release History
* 0.0.1
    * Work in progress
        * Now, that we have the information as seen in screenshot, Now I will add the features in telegram bot.

## Meta

Ardy Flora – flora_ripudaman@hotmail.com

Distributed under the MIT license. See ``LICENSE.txt`` for more information.

[https://github.com/ardyflora/telegram-fantasy-premier-league-bot](https://github.com/ardyflora/)

## Contributing

1. Fork it (<https://github.com/ardyflora/telegram-auto-ossc-softball-league>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request
