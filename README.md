# EventNix

[![Build Status](https://travis-ci.org/anxolerd/eventnix.svg?branch=master)](https://travis-ci.org/anxolerd/eventnix)

## Description
EventNix is my university assignment for _databases_ course.
It is an event registration system written in `python3.4` with the usage of [`aiohttp`](http://aiohttp.readthedocs.org/en/stable/) framework.

## Requirements
- Python 3.4
- PostgreSQL database

## Bootstrap

First you have to clone project and prepare the environment

```bash
$ git clone git@github.com:anxolerd/eventnix.git
$ cd eventnix
$ virtualenv -p python3.4 --prompt='[eventnix]' .venv
$ source .venv/bin/activate
[eventnix] $ pip install -r requirements.txt
```

Create empty PostgreSQL database in any convenient way:

```sql
postgres=# create user eventnix with password '********';
postgres=# create database eventnix owner eventnix;
```

Apply initial database creation script:
```sql
eventnix=> \i eventnix/storage/migrations/2015-11-22-18-25_create_tables.sql
```

Then create config files using examples in `config` dir. Your gunicorn config must be called `gunicorn.py` and be placed within `config` directory.

Now you can run the project:
```bash
$ ./manage.sh run /path/to/projectconfig
```

Open `localhost:8080` in your browser
