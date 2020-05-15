import logging
from flask import jsonify

logger = logging.getLogger(__name__)


class RequestHelper(object):

    @staticmethod
    def get_request_data(request):

        try:
            if request.mimetype == 'application/json':
                data = request.get_json()
            else:
                data = request.form.to_dict()
            return data

        except Exception as e:
            logger.error("Request Data: Fetching request data failed! " + str(e))
            return jsonify(err_msg="Error in fetching request data."), 400
