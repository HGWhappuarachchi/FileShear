from io import BytesIO
from flask import render_template, url_for, flash, redirect, request, abort, send_file
from app import app, db
from app.forms import RegistrationForm, LoginForm, UploadForm
from app.models import User, File
from flask_login import login_user, current_user, logout_user, login_required, LoginManager
from werkzeug.security import generate_password_hash, check_password_hash

login_manager = LoginManager(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html')

@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='pbkdf2:sha256')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route("/upload", methods=['GET', 'POST'])
@login_required
def upload():
    form = UploadForm()  # Ensure this form class exists and is properly defined
    if request.method == 'POST':
        file = request.files['file']
        if file:
            file_data = file.read()
            new_file = File(filename=file.filename, data=file_data, owner=current_user)
            db.session.add(new_file)
            db.session.commit()
            flash('File has been uploaded!', 'success')
            return redirect(url_for('home'))
    return render_template('upload.html', form=form)


@app.route("/files")
@login_required
def files():
    user_files = File.query.filter_by(owner=current_user).all()
    return render_template('files.html', files=user_files)

@app.route("/download/<int:file_id>")
@login_required
def download(file_id):
    file = File.query.get_or_404(file_id)
    if file.owner != current_user:
        abort(403)
    return send_file(BytesIO(file.data), download_name=file.filename, as_attachment=True)