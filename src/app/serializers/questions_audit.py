from app import ma
from app.models.questions_audit import QuestionsAuditModel


class QuestionsAuditSchema(ma.ModelSchema):
    class Meta:
        model = QuestionsAuditModel
