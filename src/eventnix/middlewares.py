from asyncio import coroutine


@coroutine
def debug_middleware_factory(app, handler):
    @coroutine
    def middleware(request):
        if request.app.debug:
            logger = request.app.logger
            logger.info('%s %s', request.method, request.path_qs)
        response = yield from handler(request)
        return response
    return middleware
