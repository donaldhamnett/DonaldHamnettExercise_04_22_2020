from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired


class UpdateForm(FlaskForm):

    id = IntegerField('Question ID', validators=[DataRequired()])
    question = StringField('New Question', validators=[DataRequired()])
    submit = SubmitField('Update')
