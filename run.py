from flaskblog import app

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