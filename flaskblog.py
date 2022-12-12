from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy

from forms import RegristrationForm, LogInForm
from flask import flash
from flask import redirect
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = '684cce1ec4bcfbebaa14d2ff73a79fd3'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)

with app.app_context():
    db.create_all()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"
posts = [
    {
        'author': 'Programming with Marsh',
        'title': 'Blog Post-1',
        'content': 'First Post content',
        'date_posted': 'May 21, 2019'
    },

    {
        'author': 'Corey Achafer',
        'title': 'Blog Post-2',
        'content': '2nd Post content',
        'date_posted': 'May 22, 2019'
    },

]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('About.html', title = 'About')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegristrationForm()
    if form.validate_on_submit():
        flash(f'Acccount created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LogInForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data =="12345":
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash("Login Uncsuccessful. Please check username and password", 'danger')
    return render_template('login.html', title='login', form=form)

if __name__ == '__main__':
    app.run(debug=True)

# Adding user to db
# user_1 = User(username='Khatri7968', email='engrpawan111@gmail.com', password='password')
# db.session.add(user_1)

# Commit to db
# db.seession.commit()

# Shows all users means list of users
# User.query.all()
#
# Getting first user
# User.query.first()
#
# Getting specific user
# User.query.filter_by(username='Khatri7968').all()
#
# It returns the user
# User.query.get(1)
#
# Creating a post
# post_1 = Post(title='Blog 1', content='First post content', user_id=user.id)
# db.session.add(post_1)
# user.posts

# post = Post.query.first()
# post.user_id
# post.author
#