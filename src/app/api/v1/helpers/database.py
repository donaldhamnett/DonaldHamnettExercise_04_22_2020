from datetime import datetime
from flask import json
from app import db
from app.models.questions import QuestionsModel
from app.serializers.questions import QuestionsSchema
from app.models.questions_audit import QuestionsAuditModel
from app.serializers.questions_audit import QuestionsAuditSchema


class DatabaseHelper(object):

    @staticmethod
    def insert(data):
        now = datetime.utcnow().isoformat(timespec='seconds')
        data['current_state'] = data['question']
        data['time_added'] = now
        data['last_modified'] = now
        data['time'] = now
        question_entry = QuestionsModel(data)
        question_audit_entry = QuestionsAuditModel(data)
        question_schema = QuestionsSchema()
        question_audit_schema = QuestionsAuditSchema()

        db.session.add(question_entry)
        db.session.add(question_audit_entry)
        db.session.commit()

        return json.dumps(
            {
                'question': question_schema.dump(question_entry),
                'question_audit': question_audit_schema.dump(question_audit_entry)
            }
        )

    @staticmethod
    def update(data):
        question_id = data['id']
        question_record = QuestionsModel.query.filter(QuestionsModel.id == question_id).first()
        question_schema = QuestionsSchema()
        question_audit_schema = QuestionsAuditSchema()

        question_record_data = question_schema.dump(question_record)
        now = datetime.utcnow().isoformat(timespec='seconds')
        question_audit_entry = QuestionsAuditModel(
            {
                'current_state': data['question'],
                'previous_state': question_record_data['question'],
                'time': now,
                'question_id': question_id
            }
        )

        db.session.add(question_audit_entry)
        question_record.question = data['question']
        question_record.last_modified = now

        db.session.commit()

        return json.dumps(
            {
                'question': question_schema.dump(question_record),
                'question_audit': question_audit_schema.dump(question_audit_entry)
            }
        )

    @staticmethod
    def query(data):
        question_id = data['id']
        question_query = QuestionsModel.query.filter(QuestionsModel.id == question_id).first()
        question_audit_query = QuestionsAuditModel.query.filter(
            QuestionsAuditModel.question_id == data['id']
        ).order_by(QuestionsAuditModel.time)
        question_schema = QuestionsSchema()
        question_audit_schema = QuestionsAuditSchema(many=True)
        return json.dumps(
            {
                'question': question_schema.dump(question_query),
                'question_audit': question_audit_schema.dump(question_audit_query)
            }
        )
