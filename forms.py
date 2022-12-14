from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, Length

class SignupForm(FlaskForm):

    name = StringField('nombre', validators = [DataRequired(), Length(max = 25)])
    password = PasswordField('contra', validators = [DataRequired()])
    email = StringField('email', validators = [DataRequired(), Email()])
    submit = SubmitField('envio_formulario')
