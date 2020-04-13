<h1 align="center">BudgetBot</h1>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![Platform]Telegram](https://www.reddit.com/user/Wordbook_Bot)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

## Table of Contents

- [About](#about)
- [Demo / Working](#demo)
- [How it works](#working)
- [Usage](#usage)
- [Getting Started](#getting_started)
- [Built Using](#built_using)
- [TODO](../TODO.md)
- [Author](#authors)

## About <a name = "about"></a>

BudgetBot uses NPL (natural language processing) to determine when you have made a purchase or recived money and how much. 
It stores all of that info in a CSV database that can be uploaded to Google Sheets or any other spreadhseet service that can make your financial life considerably easier.

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

The first part, i.e. "/start" **is not** case sensitive.

The bot will then be enabled on the current conversation or group chat. After that you just need to send messages containing a concept and amount and optionally the date and time of purchase.

### Bot Supports:
* Adding any form of transaction (adding or subtracting from balance).
* Getting daily spending.
* Getting daily budget.
* Overbudget notification.

### Examples:

> @BudgetBot I spent 32€ at Starbuck today.
> @BudgetBot I got 312€ from work.

---

<sup>Beep boop. I am a bot. If there are any issues, contact my [Master](gerard@learndeath.co)</sup>

## Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See [deployment](#deployment) for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them.

```
Give examples
```

### Installing

A step by step series of examples that tell you how to get a development env running.

Say what the step will be

```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo.

## Deploying your own bot <a name = "deployment"></a>

To see an example project on how to deploy your bot, please see my own configuration:

- **Heroku**: https://github.com/kylelobo/Reddit-Bot#deploying_the_bot

## ⛏️ Built Using <a name = "built_using"></a>

- [PRAW](https://praw.readthedocs.io/en/latest/) - Python Reddit API Wrapper
- [Heroku](https://www.heroku.com/) - SaaS hosting platform

## ✍️ Authors <a name = "authors"></a>

- [@kylelobo](https://github.com/kylelobo) - Idea & Initial work

See also the list of [contributors](https://github.com/kylelobo/The-Documentation-Compendium/contributors) who participated in this project.

## Acknowledgements <a name = "acknowledgement"></a>

- Hat tip to anyone whose code was used
- Inspiration
- References
