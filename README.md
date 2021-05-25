# ChatAja! Bot Webhook Sample with Phyton

## Requirements

* [Python 3](https://www.python.org/)
* [Flask](http://flask.pocoo.org/)
* [Pip 3](https://pypi.org/project/pip/)
* [Ngrok](https://ngrok.com/)
* Bot Access Token from `Chatbot Builder` ChatAja app

## How to run

* Clone this repository and install dependencies `requirements.txt`

```bash
$ git clone https://gitlab.playcourt.id/iskandarsuhaimi/webhook-kiwaribot-sample-python.git
$ cd webhook-kiwaribot-sample-python
$ pip3 install -f requirement.txt
```

* Go to `Jelajah` menu
* chat with `Chatbot Builder`
* Create bot and get `access_token`
* Copy and Paste to `controller.py`

* Run webhook server

```bash
$ export FLASK_APP=index.py
$ export FLASK_ENV=development
$ flask run
```

* Tunneling your webhook server

```bash
$ ngrok http 5000
```

* Register your webhook url by copy your ngrok https url from CLI, then input it into `Chatbot Builder`

* Enjoy!
