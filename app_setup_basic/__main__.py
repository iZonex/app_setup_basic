import sys
from .routing import router_setup
from aiohttp import web

def main(args=None):
    """The main routine."""
    if args is None:
        args = sys.argv[1:]

    app = web.Application()
    router_setup(app)
    web.run_app(app)


if __name__ == "__main__":
    main()
