from flask import Flask, request,render_template,Response,redirect,url_for
import forms
from flask_wtf.csrf import CSRFProtect
from flask import g 
from config import DevelopmentConfig
from flask import flash
from models import db
from models import Alumnos
app=Flask(__name__)
app.config.from_object(DevelopmentConfig)
csrf=CSRFProtect()



@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404

@app.route("/index",methods=["GET","POST"])
def index():
    alum_form=forms.UserForm2(request.form)
    if request.method=='POST' and alum_form.validate():
        alum=Alumnos(nombre=alum_form.nombre.data,
                    apaterno=alum_form.apaterno.data,
                    email=alum_form.email.data)
        db.session.add(alum)
        db.session.commit()
    return render_template("index.html", form=alum_form)


@app.route("/eliminar", methods=["GET","POST"])
def eliminar():
    alum_form=forms.UserForm2(request.form)
    if request.method=='GET':
        id=request.args.get('id')
        alum1=db.session.query(Alumnos).filter(Alumnos.id==id).first()
        alum_form.id.data=request.args.get('id')
        alum_form.nombre.data=alum1.nombre
        alum_form.apaterno.data=alum1.apaterno
        alum_form.email.data=alum1.email
    if request.method=='POST':
        id=alum_form.id.data
        alum=Alumnos.query.get(id)
        db.session.delete(alum)
        db.session.commit()
        return redirect(url_for('ABCompleto'))
    return render_template('eliminar.html',form=alum_form)

@app.route("/modificar", methods=["GET","POST"])
def modificar():
    alum_form=forms.UserForm2(request.form)
    if request.method=='GET':
        id=request.args.get('id')
        alum1=db.session.query(Alumnos).filter(Alumnos.id==id).first()
        alum_form.id.data=request.args.get('id')
        alum_form.nombre.data=alum1.nombre
        alum_form.apaterno.data=alum1.apaterno
        alum_form.email.data=alum1.email
    if request.method=='POST':
        id=alum_form.id.data
        
        alum=db.session.query(Alumnos).filter(Alumnos.id==id).first()
        alum.nombre=alum_form.nombre.data
        alum.apaterno=alum_form.apaterno.data
        alum.email=alum_form.email.data
        db.session.add(alum)
        db.session.commit()
        return redirect(url_for('ABCompleto'))
    return render_template('modificar.html',form=alum_form)

@app.route("/ABC_Completo",methods=["GET","POST"])
def ABCompleto():
    alumno=""
    
  
    alumno=Alumnos.query.all()
    return render_template("ABC_Completo.html",alumnos=alumno)


@app.route("/alumnos",methods=["GET","POST"])

def alumnos():
    print('dentro de 2')
    
    nombre=""
    apa=""
    correo=""
    ama=""
    alum_form=forms.UserForm(request.form)
    if request.method=='POST' and alum_form.validate():
        nombre=alum_form.nombre.data
        apa=alum_form.apaterno.data
        ama=alum_form.amaterno.data
        correo=alum_form.email.data
        mensaje='Bienvenido: {}'.format(nombre)
        flash(mensaje)
        print("nombre :{}".format(nombre))
        print("apaterno :{}".format(apa))
        print("amaterno :{}".format(ama))

        
        
    return render_template("alumnos.html",form=alum_form,nom=nombre,apapaterno=apa,ama=ama)






if __name__=="__main__":
    csrf.init_app(app)
    db.init_app(app)
    with app.app_context():
        db.create_all()
    
    app.run()

