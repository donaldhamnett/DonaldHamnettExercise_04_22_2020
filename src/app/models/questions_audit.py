from datetime import datetime
from app import db


#  Define the QuestionsAudit data model.
class QuestionsAuditModel(db.Model):

    __tablename__ = 'questions_audit'

    id = db.Column(db.Integer, primary_key=True, unique=True)
    question_id = db.Column(db.Integer, db.ForeignKey('questions.id'))
    previous_state = db.Column(db.UnicodeText, nullable=False, default='')
    current_state = db.Column(db.UnicodeText, nullable=False, default='')
    time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, data):
        self.question_id = data['question_id']
        if 'previous_state' in data:
            self.previous_state = data['previous_state']
        if 'time' in data:
            self.time = data['time']
        if 'current_state' in data:
            self.current_state = data['current_state']
