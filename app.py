from flask import Flask,render_template , request ,redirect , url_for
from flask.sessions import NullSession
from flask_sqlalchemy import SQLAlchemy
import sqlite3
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, Length
from forms import Item_add
from flask_bootstrap import Bootstrap


conector=sqlite3.connect("test.db")

app = Flask(__name__)
Bootstrap(app)
app.config['SECRET_KEY'] = '7110c8ae51a4b5af97be6534caef90e4bb9bdcb3380af008f90b23a5d1616bf319bc298105da20fe'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./test.db'
db=SQLAlchemy(app)

class Item(db.Model):
    codigo = db.Column(db.Integer , primary_key=True , nullable=False)
    numeroOriginal = db.Column(db.Integer ,nullable=False)
    marca = db.Column(db.String(80) , nullable=False)
    modelo = db.Column(db.String(80) , nullable=False)
    tipoCable = db.Column(db.String(80) , nullable=False)
    descripcion=db.Column(db.String(512))

    def __repr__(self):
        return '<User %r>' % self.username

@app.route("/")
def menu():
    return render_template("menu.html")

@app.route("/add_producto" , methods=["GET","POST"])
def add_producto():
    form=Item_add()
    
    if form.validate_on_submit():
        item=Item(codigo=form.codigo.data,numeroOriginal=form.numeroOriginal.data,
        marca=form.marca.data,modelo=form.modelo.data,tipoCable=form.tipoCable.data)
        db.session.add(item)
        db.session.commit()
        return redirect("/add_producto")
    return render_template("add_item.html", form=form)



app.run(debug=True)