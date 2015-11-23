from asyncio import coroutine

from aiohttp_jinja2 import render_template
from eventnix.storage import tb_event


@coroutine
def index(request):
    engine = request.app['db_engine']
    with (yield from engine) as conn:
        events = yield from conn.execute(tb_event.select().limit(10))
    return render_template('index.html', request, {
        'name': 'username',
        'events': events,
    })
