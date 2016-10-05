from models.topic import Topic
from models.node import Node
from models.user import User
from routes import *
from functools import wraps

from . import current_user, login_required, admin_required


main = Blueprint('topic', __name__)

Model = Topic




@main.route('/<int:id>')
def show(id):
    u = current_user()
    m = Model.query.get(id)
    return render_template('topic.html', topic=m, user=u)


@main.route('/edit/<id>')
@login_required
def edit(id):
    m = Model.query.get(id)
    return render_template('topic_edit.html', topic=m)


@main.route('/add', methods=['POST'])
@login_required
def add():
    form = request.form
    m = Model(form)
    m.node_id = int(form.get('node_id'))
    m.user_id = int(form.get('user_id'))
    m.save()
    return redirect(url_for('node.show', id=m.node_id))


@main.route('/update/<int:id>', methods=['POST'])
@login_required
def update(id):
    form = request.form
    t = Model.query.get(id)
    t.update(form)
    return redirect(url_for('node.show', id=t.node_id))


@main.route('/delete/<int:id>')
@login_required
def delete(id):
    t = Model.query.get(id)
    t.delete()
    return redirect(url_for('node.show', id=t.node_id))
