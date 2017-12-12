# coding=utf-8
from views import vk_proxy


def setup_routes(app):
    app.router.add_route('*', r'/{path:.*}', vk_proxy)
