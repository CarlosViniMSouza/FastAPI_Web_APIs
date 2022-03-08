"""
See the documentation in:

1. http://127.0.0.1:8000/docs

2. http://127.0.0.1:8000/redoc
"""

from methods import method_get, method_post
import uvicorn as uvi


method_http_get = method_get.methodGet
method_http_post = method_post.methodPost


async def methodGet(method_http_get):
    return method_http_get


async def methodPost(method_http_post):
    return method_http_post


if __name__ == "__main__":
    uvi.run(host="127.0.0.1", port=7070)
