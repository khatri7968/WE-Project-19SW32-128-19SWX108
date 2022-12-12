from flask import Flask, render_template
from forms import RegristrationForm, LogInForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '684cce1ec4bcfbebaa14d2ff73a79fd3'

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
    return render_template('register.html', title='Register', form=form)

@app.route("/login")
def login():
    form = LogInForm()
    return render_template('login.html', title='login', form=form)





if __name__ == '__main__':
    app.run(debug=True)

