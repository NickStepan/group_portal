from datetime import datetime, timedelta, UTC
from django.utils.deprecation import MiddlewareMixin


class CookieMiddleware(MiddlewareMixin):
    def process_response(self, request, response):

        if not request.COOKIES.get('theme'):
            response.set_cookie("theme", "light", expires=datetime.now(UTC) + timedelta(days=180))

        return response
