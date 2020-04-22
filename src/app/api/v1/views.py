from flask.views import View
from flask import Response


class BackgroundStuffAPI(View):
    methods = ['GET', ]

    def dispatch_request(self):
        return Response('ok')