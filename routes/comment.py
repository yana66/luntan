from models.comment import Comment

# 这个是什么
from routes import *

from . import current_user, login_required, admin_required


main = Blueprint('comment', __name__)

Model = Comment

# @main.route('/')
# def index():
#     ms = Model.query.all()
#     return render_template('topic_index.html', node_list=ms)


# @main.route('/new')
# def new():
#     return render_template('topic_edit.html')


# @main.route('/<int:id>')
# def show(id):
#     m = Model.query.get(id)
#     return render_template('topic.html', topic=m)


# @main.route('/edit/<id>')
# def edit(id):
#     t = Model.query.get(id)
#     return render_template('topic_edit.html', todo=t)


@main.route('/add', methods=['POST'])
@login_required
def add():
    form = request.form
    m = Model(form)
    m.topic_id = int(form.get('topic_id'))
    m.user_id = int(form.get('user_id'))
    m.save()
    return redirect(url_for('topic.show', id=m.topic_id))


# @main.route('/update/<int:id>', methods=['POST'])
# def update(id):
#     form = request.form
#     t = Model.query.get(id)
#     t.update(form)
#     return redirect(url_for('.index'))
#
#
# @main.route('/delete/<int:id>')
# def delete(id):
#     t = Model.query.get(id)
#     t.delete()
#     return redirect(url_for('.index'))
