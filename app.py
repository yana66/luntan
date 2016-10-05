from flask import Flask
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from models import db

from models.node import Node



app = Flask(__name__)
db_path = 'bbs.sqlite'
manager = Manager(app)


def register_routes(app):
    # from routes.todo import main as routes_todo
    from routes.node import main as routes_node
    from routes.topic import main as routes_topic
    from routes.auth import main as routes_auth
    from routes.comment import main as routes_comment

    app.register_blueprint(routes_auth, url_prefix='/auth')
    app.register_blueprint(routes_node, url_prefix='/story')
    app.register_blueprint(routes_topic, url_prefix='/topic')
    app.register_blueprint(routes_comment, url_prefix='/comment')


def configure_app():
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    app.secret_key = 'secret_key'
    app. config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///{}'.format(db_path)
    db.init_app(app)
    register_routes(app)


def configured_app():
    configure_app()
    return app


@manager.command
def server():
    app = configured_app()
    config = dict(
        debug=True,
        host='0.0.0.0',
        port=3030,
    )
    app.run(**config)


def configure_manager():
    Migrate(app, db)
    manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    configure_manager()
    configure_app()
    manager.run()



