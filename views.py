# coding=utf-8

import aiohttp
from aiohttp import web
from urllib.parse import urlparse, urljoin

from decorators import rate_limit

VK_API_URL = 'https://api.vk.com'
RATE_LIMIT_CALLS_COUNT = 5
RATE_LIMIT_INTERVAL = 5


@rate_limit(calls_count=RATE_LIMIT_CALLS_COUNT, interval=RATE_LIMIT_INTERVAL)
async def vk_proxy(request):
    params = request.rel_url.query
    data = await request.read()

    # Change server domain on api domain
    request.headers['Host'] = urlparse(VK_API_URL).hostname

    request_to_vk_kwargs = dict(
        method=request.method,
        url=urljoin(VK_API_URL, request.url.path),
        headers=request.headers,
        params=params,
        data=data,
    )

    async with aiohttp.ClientSession() as session:
        async with session.request(**request_to_vk_kwargs) as resp:
            body = await resp.read()
            headers = resp.headers.copy()

    # Updating headers from VK response
    # - remove `Transfer-Encoding` for disabling auto decoding
    # - remove `Content-Encoding` for disabling gzip unarchivation
    # - remove `Content-Length` for changing of content size after disabling unarchivation
    # - change `Connection` for closing a client connetion
    for header in ['Transfer-Encoding', 'Content-Encoding', 'Content-Length']:
        if headers.get(header):
            del headers[header]

    if headers.get('Connection'):
        headers['Connection'] = 'close'

    return web.Response(body=body, headers=headers)
