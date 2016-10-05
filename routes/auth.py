from models.user import User
# from models.topic import Topic
from routes import *
from . import current_user, login_required, admin_required

# for decorators
from functools import wraps


main = Blueprint('auth', __name__)


Model = User



@main.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        form = request.form
        m = Model(form)
        status, msgs = m.valid()
        if status:
            m.save()
            return redirect(url_for('auth.login'))
        else:
            for msg in msgs:
                return msg
    return render_template('auth_register.html')


@main.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        form = request.form
        m = Model(form)
        user = Model.query.filter_by(username=m.username).first()
        if m.valid_login(user):
            session['user_id'] = user.id
            return redirect(url_for('node.index'))
        else:
            return '登录失败'
    return render_template('auth_login.html')

@main.route('/logout')
@login_required
def logout():
    session['user_id'] = None
    return redirect(url_for('node.index'))

# @main.route('/user/update_password', methods=['POST'])
# def update_password():
#     u = current_user()
#     password = request.form.get('password', '')
#     print('password', password)
#     if u.change_password(password):
#         print('修改成功')
#     else:
#         print('用户密码修改失败')
#     return redirect('/profile')
#
#
# @main.route('/user/update_avatar', methods=['POST'])
# def update_avatar():
#     u = current_user()
#     avatar = request.form.get('avatar', '')
#     print('password', avatar)
#     if u.change_avatar(avatar):
#         print('修改成功')
#     else:
#         print('用户密码修改失败')
#     return redirect('/profile')
#
#
# @main.route('/profile', methods=['GET'])
# def profile():
#     u = current_user()
#     if u is not None:
#         print('profile', u.id, u.username, u.password)
#         return render_template('profile.html', user=u)
#     else:
#         return redirect(url_for('.login_view'))




