from asyncio import get_event_loop

import logging

from aiopg.sa import create_engine
from os.path import isfile
from yaml import load


def read_validate_config(filepath):
    def validate(cfg):
        assert cfg is not None

        assert 'app' in cfg.keys()
        assert isinstance(cfg['app'], dict)

        assert 'databases' in cfg['app'].keys()
        assert isinstance(cfg['app']['databases'], dict)

        assert 'main' in cfg['app']['databases'].keys()

    assert isfile(filepath)
    with open(filepath, 'r') as stream:
        config = load(stream)
    validate(config)
    return config


def setup_db_engine(app, db_config):
    assert app is not None
    assert db_config is not None

    loop = get_event_loop()

    if isinstance(db_config, str):
        engine = loop.run_until_complete(create_engine(dsn=db_config))
    elif isinstance(db_config, dict):
        engine = loop.run_until_complete(create_engine(**db_config))
    else:
        raise AttributeError("db_config must be either dsn string or dict")
    app['db_engine'] = engine
    return app


def get_logger(config, name='root'):
    logger_config = config.get('logging', None)
    if logger_config:
        logging.config.dictConfig(logger_config)
    return logging.getLogger(name)
