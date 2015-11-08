# EventNix

[![Build Status](https://travis-ci.org/anxolerd/eventnix.svg?branch=master)](https://travis-ci.org/anxolerd/eventnix)

## Description
EventNix is my university assignment for _databases_ course.
It is an event registration system written in `python` with the usage of [`aiohttp`](http://aiohttp.readthedocs.org/en/stable/) framework.

## Bootstrap

First you have to prepare the environment
```bash
$ git clone git@github.com:anxolerd/eventnix.git
$ cd eventnix
$ virtualenv -p python3.4 --prompt='[eventnix]' .venv
$ source .venv/bin/activate
[eventnix] $ pip install -r requirements.txt
```

Now you can run the project:
```bash
$ ./manage.sh run
```

Open `localhost:8080` in your browser
