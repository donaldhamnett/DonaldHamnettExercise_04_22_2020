import logging
import traceback

from flask import request, Response, json
from flask.views import MethodView
from app.api.v1.helpers.request import RequestHelper
from app.api.v1.helpers.database import DatabaseHelper

logger = logging.getLogger(__name__)


class QuestionsAPIView(MethodView):

    def post(self):
        response_obj = Response(mimetype='application/json')
        data = RequestHelper.get_request_data(request)

        try:

            response_obj.data = DatabaseHelper.insert(data)
            response_obj.status_code = 201

        except Exception as e:
            logger.error(f'Questions: Error while processing request.\n{str(e)}\n{str(traceback.print_exc())}')
            response_obj.data = json.dumps(
                {
                    'err_msg': 'Error while adding question.'
                }
            )
            response_obj.status_code = 400

        return response_obj

    def patch(self):
        response_obj = Response(mimetype='application/json')
        data = RequestHelper.get_request_data(request)

        try:
            response_obj.data = DatabaseHelper.update(data)
            response_obj.status_code = 202

        except Exception as e:
            logger.error(f'Questions: Error while processing request.\n{str(e)}\n{str(traceback.print_exc())}')
            response_obj.data = json.dumps(
                {
                    'err_msg': 'Error while updating question.'
                }
            )
            response_obj.status_code = 400

        return response_obj

    def get(self):
        response_obj = Response(mimetype='application/json')
        data = RequestHelper.get_request_data(request)

        try:
            response_obj.data = DatabaseHelper.query(data)
            response_obj.status_code = 200

        except Exception as e:
            logger.error(f'Questions: Error while processing request.\n{str(e)}\n{str(traceback.print_exc())}')
            response_obj.data = json.dumps(
                {
                    'err_msg': 'Error while querying question.'
                }
            )
            response_obj.status_code = 400

        return response_obj

