from wtforms import Form
from wtforms import StringField, TextAreaField, SelectField,RadioField,EmailField,IntegerField
from wtforms import EmailField
from wtforms import validators

class UserForm(Form):
    nombre=StringField("nombre",[validators.DataRequired(message='el campo es requerido'),
                                 validators.length(min=4,max=10,message='ingresa nombre valido')])
    email=EmailField("correo")
    apaterno=StringField('apaterno')
    amaterno=StringField('amaterno')
    edad=IntegerField('edad',
                      [validators.number_range(min=1, max=20, message='valor no valido')])
    
    correo=EmailField('correo',[
        validators.Email(message='Ingrese un correo valido'
                         )])

   

  
