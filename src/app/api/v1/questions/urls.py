from flask import Blueprint, jsonify

from app.api.v1.questions.views import QuestionsAPIView

questions = Blueprint('questions', __name__)

questions_view = QuestionsAPIView.as_view('questions_view')
questions.add_url_rule('/questions', view_func=questions_view, methods=['POST', 'PATCH', 'GET'], strict_slashes=False)


@questions.app_errorhandler(404)
def page_not_found(e):
    return jsonify(err_msg="Requested URL not found on this server!"), 404


@questions.app_errorhandler(405)
def page_not_found(e):
    return jsonify(err_msg="The method is not allowed for the requested URL!"), 405


@questions.app_errorhandler(500)
def page_not_found(e):
    return jsonify(err_msg="Internal server error!"), 500