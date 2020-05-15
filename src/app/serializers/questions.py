from app import ma
from app.models.questions import QuestionsModel


class QuestionsSchema(ma.ModelSchema):
    class Meta:
        model = QuestionsModel
