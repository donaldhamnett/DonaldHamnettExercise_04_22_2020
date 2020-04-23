from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import DataRequired


class HistoryForm(FlaskForm):

    question = IntegerField('Question ID', validators=[DataRequired()])
    submit = SubmitField('Look Up')
