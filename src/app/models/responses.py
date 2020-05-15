# from datetime import datetime
# from app import db
#
#
# #  Define the Responses data model.
# class ResponsesModel(db.Model):
#
#     __tablename__ = 'questions_responses'
#
#     id = db.Column(db.Integer, primary_key=True, unique=True)
#     question_id = db.Column(db.Integer, db.ForeignKey('questions.id'))
#     audit_id = db.Column(db.Integer, db.ForeignKey('questions_audit.id'))
#     user_id = db.Column(db.Integer, db.ForeignKey('questions_users.id'))
#     time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
#
#     def __init__(self, data):
#         self.question_id = data['question_id']
#         self.audit_id = data['audit_id']
#         self.user_id = data['audit_id']
#         self.time = data['time']
