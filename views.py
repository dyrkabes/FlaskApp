from app import app, login_manager, open_id
from flask import render_template

from flask.ext.login import LoginManager, login_user, logout_user, current_user, login_required
from flask.ext.bcrypt import check_password_hash
from flask.ext.openid import OpenID

import os

from flask import Flask, g, render_template, flash, redirect, request, url_for, session


from forms import LoginForm, EditForm, RegisterForm, PostForm, PostHandForm, BuffForm


from models import blog


@login_manager.user_loader
def load_user(userid):
    try:
        return blog.User.get(blog.User.id == userid)
    except blog.DoesNotExist:
        return None

@app.before_request
def before_request():
    """
    :return: Connect to the database before each request
    """
    g.db = blog.DATABASE
    g.db.connect()
    g.user = current_user
    if current_user.is_authenticated:
        current_user.set_last_seen()
        app.logger.info("{} has done smthing".format(g.user.username))

    import logging



@app.after_request
def after_request(response):
    """
    :param response:
    :return: Close the db connection after each request
    """
    g.db.close()
    return response


@app.route('/sevices')
def services():
    return render_template('services.html')

@app.route('/services/buff_cost')
def buff_cost():
    form = BuffForm()
    # object toj peredat'
    return render_template('services/buff_cost.html', form=form)

@app.route('/hands')
def hands():
    # rakom
    # user = blog.User.get(blog.User.username == current_user.username)
    # rakom sdelano, peredelat'
    # stream = blog.Hand.get_stream(blog.Hand, user)
    stream = blog.Hand.select()
    title="Hands"
    return render_template(
        'hands.html',
        stream=stream,
        user=user,
        title=title
    )

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

@app.route('/register', methods=["GET", "POST"])
def register():
    if g.user is not None and g.user.is_authenticated:
        return redirect(url_for('index'))
    form = RegisterForm()

    if form.validate_on_submit():
        flash("Registered", "success")
        blog.User.create_user(
            username=form.username.data,
            email=form.email.data,
            password=form.password.data
        )
        return redirect(url_for('index'))
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
@open_id.loginhandler
def login():
    if g.user is not None and g.user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()

    if form.validate_on_submit():
        session['remember_me'] = form.remember_me.data #kak ispol'zovat'?
        try:
            user = blog.User.get(blog.User.username == form.username.data)
        except blog.DoesNotExist:
            flash("Your email or password doesn't match", "failure")
        else:
            if check_password_hash(user.password, form.password.data):
                login_user(user, remember=session['remember_me'])
                flash("you've benn logged in", "success")
                return redirect(url_for('index'))
            else:
                flash("Your email or password doesn't match", "failure")
    return render_template('login.html', form=form)

    #
    # if form.validate_on_submit():
    #     session['remember_me'] = form.remember_me.data
    #
    #     flash("Login requested") #requested?
    #
    #     return open_id.try_login(form.open_id.data, ask_for=['nickname', 'email'])
    # return render_template('login.html',
    #                        title='Sign in',
    #                        form=form,
    #                        providers = app.config['OPENID_PROVIDERS']
    #                     )


#doesnt go there yet
@open_id.after_login
def after_login(response):
    flash("wess", "failure")
    if response.email is None or response.email == "":
        flash("Invalid login", "failure")
        return redirect(url_for('login'))
    user = blog.User.get(blog.User.email == response.email)
    if user is None:
        username = response.username
        if username is None or username == "":
            username = response.email.split('@')[0]
        user = blog.User.create_user(username = username, email = response.email)
    remember_me = False
    if 'remember_me' in session:
        remember_me = session['remember_me']
        session.pop('remember_me', None)
    login_user(user, remember_me = remember_me)
    return redirect(request.args.get('next') or url_for('index'))

@app.route('/logout')
def logout():
    logout_user()
    flash("Logout successful", "success")
    return redirect(url_for('index'))

@app.route('/user/<username>')
@login_required
def user(username):
    user = blog.User.get( blog.User.username == username)
    if user == None:
        flash("User " + user + " not found", "failure")
        redirect(url_for('index'))

    stream = user.get_stream()
    return render_template('user.html',
                           user=user,
                           stream=stream
                           )



@login_required
@app.route('/post', methods=['GET', 'POST'])
def post():

    form = PostForm()

    if form.validate_on_submit():
        flash("added", "success")
        blog.Post.create_post(
            content=form.content.data,
            user=blog.User.get(blog.User.username ** current_user.username)
        )
        return redirect(url_for('index'))

    return render_template('post.html', form=form, user=current_user)

@login_required
@app.route('/edit_profile', methods=["GET", "POST"])
def edit_profile():
    form = EditForm()
    if form.validate_on_submit():
        g.user.update_about_me(form.about_me.data)
        flash("Update is successful, rejoice!", "success")
        return redirect(url_for('user', username=g.user.username))
    if current_user.about_me:
         form.about_me.data = current_user.about_me
    return render_template('edit_profile.html', form=form, user=current_user)

@login_required
@app.route('/post_hand', methods=["GET", "POST"])
def post_hand():
    form = PostHandForm()
    if form.validate_on_submit():
        flash("Hand saved", "success")
        blog.Hand.create_hand(
            content=form.content.data,
            user=blog.User.get(blog.User.username ** current_user.username),
            flop=form.flop.data,
            turn=form.turn.data,
            river=form.river.data,
            summary=form.summary.data,
        )
        return redirect(url_for('hands'))
    return render_template('post_hand.html', form=form, user=current_user)

@login_required
#param pomenyat' name
@app.route('/edit_hand/<id>', methods=["GET", "POST"])
def edit_hand(id):
    hand = blog.Hand.get(blog.Hand.id == id)
    form = PostHandForm()
    if form.validate_on_submit():
        pass

    if hand.content:
         form.content.data = hand.content

    #TODO: ADD IFs
    form.flop.data = hand.flop
    form.turn.data = hand.turn
    form.river.data = hand.river
    form.summary.data = hand.summary

    return render_template('edit_hand.html', form=form, user=current_user)


@app.route('/view_post/<post_id>')
def view_post(post_id):
    post = blog.Post.get(id=post_id)

    return render_template('view_post.html', post=post, user=current_user)

@app.route('/edit_post/<post_id>')
def edit_post(post_id):
    post = blog.Post.get(id=post_id)
    form = PostForm()
    form.content.data = post.content
    return render_template('edit_post.html', post=post, user=current_user, form=form)


#texst
@app.route('/update')
def update():
    g.user.update_email('rellik-the-great@mail.ru')
    return redirect(url_for('index'))




@app.route('/s')
def s():
    return "SHAMA"

@app.route('/')
@app.route('/index')
def index():
    #stream = blog.User.get(blog.User.username**'dyrkabes').get_stream()

    stream = blog.Post.select()

    title="Blog"

    return render_template("index.html", user=g.user,
                           stream=stream, title = title
                           )





@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):

    # test rollback
    blog.DATABASE.rollback()

    return render_template('500.html'), 500
