from .web_handlers import handle

def router_setup(app):
    app.router.add_get('/', handle)
    app.router.add_get('/{name}', handle)
