import secrets
import bcrypt
from flask import Flask, request, jsonify
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Email, Length
from flask_wtf.csrf import CSRFProtect, generate_csrf

app = Flask(__name__)
app.config['SECRET_KEY'] = secrets.token_urlsafe(16)
csrf = CSRFProtect(app)

class RegistrationForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])

    def validate(self):
        if not super().validate():
            return False

        return True

@app.route('/register', methods=['POST'])
def register_user():
    form = RegistrationForm()
    if form.validate_on_submit():
        try:
            username = form.username.data.strip()
            password = form.password.data
            if not username or not password:
                return jsonify({'message': 'Invalid request'}), 400
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
            # Store the username and hashed password in your database
            return jsonify({'message': 'User created successfully'}), 201
        except Exception as e:
            return jsonify({'message': 'An error occurred: ' + str(e)}), 500
    return jsonify({'message': 'Invalid request'}), 400