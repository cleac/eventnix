from eventnix.pages import index

"""
Describe all routes here in format: (endpoint, method, handler_function)
Use asterisk (*) to match any method
Do not add routes anywhere else
"""

ROUTES = (
    ('/', 'GET', index),
)


def init_routes(app):
    """
    Use this function to init app routes.
    This function changes app
    :param app: application
    :return: application
    """

    for endpoint, method, handler in ROUTES:
        app.router.add_route(method, endpoint, handler)

    return app
