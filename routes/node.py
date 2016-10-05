from models.node import Node
from models.topic import Topic
from models.user import User
from routes import *
from . import current_user, login_required, admin_required

# for decorators
from functools import wraps


main = Blueprint('node', __name__)


Model = Node



@main.route('/')
# @login_required
def index():
    ms = Model.query.all()
    m = Topic.query.all()
    u = current_user()
    return render_template('homepage.html', node_list=ms, topic_list=m, user=u)


@main.route('/<int:id>')
# @login_required
def show(id):
    u = current_user()
    # ms is for nav items.
    ms = Model.query.all()
    m = Model.query.get(id)
    return render_template('node.html', node_list=ms, node=m, user=u)


@main.route('/edit/<id>')
@admin_required
def edit(id):
    m = Model.query.get(id)
    return render_template('node_edit.html', node=m)


@main.route('/add', methods=['GET', 'POST'])
@admin_required
def add():
    if request.method == 'POST':
        form = request.form
        m = Model(form)
        m.save()
        return redirect(url_for('.index'))
    return render_template('node_add.html')


@main.route('/update/<int:id>', methods=['POST'])
def update(id):
    form = request.form
    m = Model.query.get(id)
    m.update(form)
    return redirect(url_for('.index'))


@main.route('/delete/<int:id>')
@admin_required
def delete(id):
    m = Model.query.get(id)
    m.delete()
    return redirect(url_for('.index'))
