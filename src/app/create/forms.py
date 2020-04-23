from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class CreateForm(FlaskForm):

    question = StringField('Question', validators=[DataRequired()])
    submit = SubmitField('Create')
