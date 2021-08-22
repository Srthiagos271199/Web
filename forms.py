from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, Length

class Item_add(FlaskForm):
    codigo = StringField("Codigo de la Empresa",validators=[DataRequired()])
    numeroOriginal = StringField("Numero Original",validators=[DataRequired()])
    marca = StringField("Marca",validators=[DataRequired()])
    modelo = StringField("Modelo",validators=[DataRequired()])
    tipoCable= StringField("Tipo de Cable",validators=[DataRequired()])
    submit= SubmitField("Agregar")