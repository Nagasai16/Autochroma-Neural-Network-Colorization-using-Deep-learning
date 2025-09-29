import os
from flask import Flask, render_template, request, redirect, url_for, session, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename

# Import the colorization function from your backend file
from colorization_backend import colorize_image

app = Flask(__name__)
app.secret_key = "your-secret-key"

# Upload & Output folders
UPLOAD_FOLDER = 'uploads'
OUTPUT_FOLDER = 'static/output'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['OUTPUT_FOLDER'] = OUTPUT_FOLDER
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

# Dummy in-memory user store
users = {}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    username = session.get('username')
    uploaded_image = session.get('uploaded_image')
    colorized_image = session.get('colorized_image')
    return render_template(
        'index.html',
        username=username,
        uploaded_image=uploaded_image,
        colorized_image=colorized_image
    )

@app.route('/upload', methods=['POST'])
def upload():
    if 'username' not in session:
        flash("Please login first to upload images.", "error")
        return redirect(url_for('login'))

    if 'image' not in request.files:
        flash("No file part", "error")
        return redirect(url_for('index'))

    file = request.files['image']
    if file.filename == '':
        flash("No selected file", "error")
        return redirect(url_for('index'))

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        upload_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(upload_path)

        try:
            # Call the colorization function
            output_path = colorize_image(upload_path)
            colorized_filename = os.path.basename(output_path)

            session['uploaded_image'] = filename
            session['colorized_image'] = colorized_filename

            flash("Image uploaded and colorized successfully!", "success")
        except Exception as e:
            flash(f"Error during colorization: {e}", "error")

        return redirect(url_for('index'))
    else:
        flash("Allowed image types: png, jpg, jpeg, gif", "error")
        return redirect(url_for('index'))

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/static/output/<filename>')
def output_file(filename):
    return send_from_directory(app.config['OUTPUT_FOLDER'], filename)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = users.get(username)
        if user and check_password_hash(user['password'], password):
            session['username'] = username
            session.pop('uploaded_image', None)
            session.pop('colorized_image', None)
            flash('Logged in successfully!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Invalid username or password', 'error')
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users:
            flash('Username already exists', 'error')
        else:
            hashed_password = generate_password_hash(password)
            users[username] = {'password': hashed_password}
            flash('Registration successful! Please login.', 'success')
            return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    session.pop('uploaded_image', None)
    session.pop('colorized_image', None)
    flash('Logged out successfully!', 'success')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
