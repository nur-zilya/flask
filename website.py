from flask import Flask, render_template, request, url_for, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = "no one has to know this key"

class NamerForm(FlaskForm):
    name = StringField("What is your name", validators=[DataRequired()])
    submit = SubmitField("Submit")


@app.route('/home', methods=["GET", "POST"])
def home():
    return render_template("home.html")

@app.route('/name', methods=["GET", "POST"])
def name():
    name = None
    form = NamerForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
        
    return render_template("name.html",
        name = name,
        form = form)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500

@app.route('/info')
def info():
    # fname=request.form.to_dict()['fname']
    # lname=request.form.to_dict()['lname']
    return render_template("info.html")

if __name__=='__main__':
    app.run(debug=True)
