from datetime import datetime
from app import db
from app.models.questions_audit import QuestionsAuditModel


#  Define the Questions data model.
class QuestionsModel(db.Model):

    __tablename__ = 'questions'

    id = db.Column(db.Integer, primary_key=True, unique=True)
    question = db.Column(db.UnicodeText, nullable=False, default='', unique=True)
    time_added = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    last_modified = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    questions_audit = db.relationship('QuestionsAuditModel', backref='questions')

    def __init__(self, data):
        if 'question' in data:
            self.question = data['question']
        if 'time_added' in data:
            self.time_added = data['time_added']
        if 'last_modified' in data:
            self.last_modified = data['last_modified']


