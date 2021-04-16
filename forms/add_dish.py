from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import BooleanField, SubmitField, IntegerField, DateTimeField
from wtforms.validators import DataRequired


class DishesForm(FlaskForm):
    title = StringField('Название блюда', validators=[DataRequired()])
    cooker = IntegerField("ID шеф-повара", validators=[DataRequired()])
    work_size = IntegerField("Длительность приготовления", validators=[DataRequired()])
    ingredients = StringField("Ингредиенты", validators=[DataRequired()])
    category = IntegerField("ID Категории блюда", validators=[DataRequired()])
    submit = SubmitField('Применить')
