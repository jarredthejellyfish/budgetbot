<h1 align="center">BudgetBot</h1>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

## Table of Contents

- [About](#about)
- [Demo / Working](#demo)
- [How it works](#working)
- [Usage](#usage)
- [Built Using](#built_using)
- [To Do](#to_do)
- [Author](#authors)

## About <a name = "about"></a>

BudgetBot uses NPL (natural language processing) to determine when you have made a purchase or recived money and how much. 
It stores all of that info in a CSV database that can be uploaded to Google Sheets or any other spreadhseet service that can make your financial life considerably more convenient.

## Demo <a name = "demo"></a>

![Working](https://media.giphy.com/media/20NLMBm0BkUOwNljwv/giphy.gif)

## How it works <a name = "working"></a>

The bot reads your message and runs it through a couple of NPL algorythms to extract any importnat information related to the financial content.

If it has all the requiered information, it generates a database object and stores it for convenient use later.

The bot uses the GSheet.

The entire bot is written in Python 3.7

## Usage <a name = "usage"></a>

To use the bot, type:

```
/start
```

The initialization command, i.e. "/start" **is not** case sensitive.

The bot will then be enabled on the current conversation or group chat. After that you just need to send messages containing a concept and amount and optionally the date and time of purchase.

### Bot Supports:
* Adding any form of transaction (adding or subtracting from balance).
* Getting daily spending.
* Getting daily budget.
* Overbudget notification.

### Examples:
> <p> @BudgetBot I spent 32€ at Starbuck today. <br /> @BudgetBot I got 312€ from work. <br /> @BudgetBot how much can I spend today?</p>
 

---

<sup>Beep boop. I am a bot. If there are any issues, contact my [Master](gerard@learndeath.co).</sup>

## Built Using <a name = "built_using"></a>

- [Telegram.ext](https://github.com/python-telegram-bot/python-telegram-bot) - Python Telegram API Wrapper.
- [Tesseract](https://github.com/madmaze/pytesseract) - Python Google Tesseract-OCR Engine wrapper.

## Author <a name = "authors"></a>

- [@jarredthejellyfish](https://github.com/jarredthejellyfish) - Idea & Work

## To Do: <a name = "to_do"></a>
- [x] Finish DB
- [ ] Start NPL
- [ ] Finish README.md

## Acknowledgements <a name = "acknowledgement"></a>

- Inspiration **??????????**
- References **??????????**
