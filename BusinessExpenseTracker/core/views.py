from flask import render_template,request,Blueprint
from BusinessExpenseTracker.models import BlogPost

core = Blueprint('core', __name__)


@core.route('/')
def index():
    '''
     uses pagination to show a limited number of posts by limiting its query
     size and then calling paginate.
    '''
    page = request.args.get('page', 1, type=int)
    blog_posts = BlogPost.query.order_by(BlogPost.date.desc()).paginate(page=page, per_page=10)
    return render_template('index.html',blog_posts=blog_posts)


@core.route('/info')
def info():
    return render_template('info.html')

@core.route('/tcs')
def tcs():
    return render_template('tcs.html')

@core.route('/example')
def example():
    return render_template('example_page1.html')

@core.route('/new_expense')
def new_expense():
    return render_template('new_expense.html')

@core.route('/license')
def license():
    return render_template('license.html')

@core.route('/privacy_policy')
def privacy_policy():
    return render_template('privacy_policy.html')

@core.route('/faq')
def faq():
    return render_template('faq.html')

@core.route('/profile')
def profile():
    return render_template('profile.html')

@core.route('/settings')
def settings():
    return render_template('settings.html')
