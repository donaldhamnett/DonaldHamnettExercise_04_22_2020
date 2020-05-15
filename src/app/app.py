import datetime
from flask import request, jsonify
from flask import Blueprint
from urllib.parse import urlparse

main = Blueprint('main', __name__)


@main.app_errorhandler(Exception)
def app_errorhandler(e):
    datetime_str = str(datetime.datetime.now())
    parse_result = urlparse(request.url)
    domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parse_result)

    return jsonify({'message': "Internal server error!!!", "success": False, "datetime": datetime_str,
                    "error_details_api": "{}api-error-log/?datetime={}"
                   .format(domain, datetime_str.replace(" ", '%20'))}), 500
