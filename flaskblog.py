from flask import Flask, render_template

app = Flask(__name__)

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


if __name__ == '__main__':
    app.run(debug=True)

