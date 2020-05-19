import werkzeug
from flask import render_template, url_for, flash, redirect
from app import app, db
from werkzeug.security import generate_password_hash, check_password_hash
from app.models import User, Post
from app.forms import RegistrationForm, LoginForm, PostForm
from flask_login import login_user


posts = [
    {
    'title':'Valami1',
    'subtitle': 'Valami',
    'author': 'Kornel Toth',
    'content': 'djfgdfgdiogjdfigjdfogidjfig jidg difgjdi jdifgji'
    },
    {
    'title':'Valami1',
    'subtitle': 'Valami',
    'author': 'Kornel Toth',
    'content': 'djfgdfgdiogjdfigjdfogidjfig jidg difgjdi jdifgji'
    },
]

@app.route('/', methods=('GET', 'POST'))
def index():

    return render_template('layout.html', title="Home", posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title="About")

@app.route('/blog-post')
def blog_post():

    return render_template('blog-post.html', title="Blog Post")

@app.route('/blog_home')
def blog_home():
    return render_template('blog-home.html', title="Blog Home")

@app.route('/blog-home-alt')
def blog_home_alt():
    return render_template('blog-home-alt.html', title="Blog Home Alt")

@app.route('/blog-list')
def blog_list():
    return render_template('blog-list.html', title="Blog List")

@app.route('/project')
def project():
    return render_template('project.html', title="Project")

@app.route('/resume')
def resume():
    return render_template('resume.html', title="Resume")

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html', title="Portfolio")

@app.route('/signup', methods=["GET","POST"])
def signup():
    form = RegistrationForm()
    if form.validate_on_submit:
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        print(user)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created', 'success')
        return redirect(url_for('login'))
    return render_template('admin/signup.html', title="Sign Up", form=form)

@app.route('/login', methods=["GET","POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
            user = User.query.filter_by(email=form.email.data).first()
            if user and werkzeug.check_password_hash(user.password, form.password.data):
                login_user(user, remember=form.remember.data)
                return redirect(url_for('about'))
            else:
                flash('Login Unsuccessfull. Please check emailand password', 'danger')
    return render_template('admin/login.html', title="Log In", form=form)

@app.route('/contact', methods=["GET","POST"])
def contact():
    form = ContactForm()

    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        subject = request.form.get('subject')

        if form.validate() == False:
            flash('All fields are required.')
            return render_template('contact.html',title="Contact", form=form)
        else:
            message = Message(form.name.data,  sender='tkornel19@gmail.com', recipients='[tkornel19@gmail.com]',)
            message.body = """
            From %s <%s>
            %s
            """ % (form.name.data, form.email.data, form.message.data)
            mail.send(message)
            return render_template('contact.html', success=True)
    elif request.method == 'GET':
        return render_template('contact.html', title="Contact", form=form)

@app.route('/post/new', methods=["GET","POST"])
# @login_required()
def new_post():
    post = PostForm()
    if form.validate_on_submit():
        flash("You post has already created")
        return redirect(url_for('/'))
    return render_template('create_post.html', title='New Post', post=post)
