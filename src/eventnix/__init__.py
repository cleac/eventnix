from aiohttp import web
from aiohttp_jinja2 import setup as setup_jinja2
from eventnix.dispatcher import init_routes
from eventnix.middlewares import debug_middleware_factory
from eventnix.util import read_validate_config, setup_db_engine, get_logger
from jinja2 import FileSystemLoader
from os.path import dirname, join

ROOT = dirname(__file__)
TEMPLATES_DIR = join(ROOT, 'templates')


def build_app(config_file):
    config = read_validate_config(config_file)
    logger = get_logger(config)
    app = web.Application(
        debug=True, middlewares=[debug_middleware_factory], logger=logger
    )
    init_routes(app)
    setup_jinja2(app, loader=FileSystemLoader(TEMPLATES_DIR))
    setup_db_engine(app, config['app']['databases']['main'])
    return app


__all__ = ('ROOT', 'TEMPLATES_DIR',)
