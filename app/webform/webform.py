from flask import Flask, render_template, flash, request
from wtforms import validators, StringField, SubmitField, FieldList, FormField
from flask_wtf import FlaskForm

# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = 'secretkey'


class RegistrationForm(FlaskForm):
    email = StringField('E-mail:', validators=[validators.required(), validators.email()])
    ip = StringField('IP Address:', validators=[validators.required(), validators.ip_address()])
    submit = SubmitField('Submit')


@app.route("/", methods=['GET', 'POST'])
def webform():
    form = RegistrationForm(request.form)

    print(form.errors)
    if request.method == 'POST':
        email = request.form['email']
        ip = request.form['ip']
        print(email)
        print(ip)

        if form.validate_on_submit():
            flash('Your registration has been accepted. Report will be sent to: ' + email
                  + 'as soon as it will be ready')
        else:
            flash('Error: All the form fields are required. ')

    return render_template('webform.html', form=form)


if __name__ == "__main__":
    app.run()
