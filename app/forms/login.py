from flask_wtf import FlaskForm
from wtforms import (
    EmailField,
    StringField,
    PasswordField,
    SubmitField,
)
from wtforms.validators import (
    DataRequired,
    EqualTo,
    Email,
)


class LoginForm(FlaskForm):
    nickname = StringField(validators=[DataRequired(),])
    password = PasswordField(validators=[DataRequired(),])
    submit = SubmitField("Log In")
    # nickname: Mapped[str] 
    # email: Mapped[str]
    # password: Mapped[str]