#!/home/thenerdsuperuser/.local/share/virtualenvs/something-CdvUv4a3/bin/python3.7

from config import *
from time import gmtime, strftime
from datetime import datetime
from docopt import docopt


usage = '''

Some shitty app's API
Usage:  main.py --new <tweet>
        main.py --show <num>
        main.py (-h | --help)
        main.py --version

Options:

    -h --help   Show this screen.
    --version   Show Version.

'''

'''

Logger Functions

'''

bot_username = 'something'
logfile_name = bot_username + ".log"
errorfile_name = "errors.log"

now = datetime.now()
timestr = now.strftime("%Y-%m-%d %H:%M:%S")


def log(message):
    """Log message to logfile."""
    path = os.path.realpath(os.path.join(
        os.getcwd(), os.path.dirname(__file__)))
    with open(os.path.join(path, logfile_name), 'a+') as f:
        t = strftime("%d %b %Y %H:%M:%S", gmtime())
        f.write("\n" + t + " " + message)


def ErrorLog(message):
    """Log message to logfile."""
    path = os.path.realpath(os.path.join(
        os.getcwd(), os.path.dirname(__file__)))
    with open(os.path.join(path, errorfile_name), 'a+') as f:
        t = strftime("%d %b %Y %H:%M:%S", gmtime())
        f.write("\n" + t + " " + message)


'''

Tweepy Functions

'''


def init():
    global api

    # initialize api
    api = create_api()


def feed(num):
    timeline = api.home_timeline(count=num)
    for tweet in timeline:
        name = tweet.user.name
        name = name.upper()
        text = tweet.text

        print(name + ' said\n' + text + "\n\n")


def main():
    args = docopt(usage, version='Something v1')
    if args['--new']:
        text = args['<tweet>']
        api.update_status(text)

    elif args['--show']:
        num = args['<num>']
        feed(num)


if __name__ == "__main__":
    init()
    main()
