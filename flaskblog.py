from flask import Flask, render_template, url_for
from forms import RegristrationForm, LogInForm
from flask import flash
from flask import redirect

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

