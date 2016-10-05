from . import ModelMixin
from . import db
from . import timestamp
from models.comment import Comment

class Topic(db.Model, ModelMixin):
    __tablename__ = 'topics'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    content = db.Column(db.String(1000))
    created_time = db.Column(db.String(100))
    # has relationship with comments
    comments = db.relationship('Comment', backref="topic")

    #
    node_id = db.Column(db.Integer, db.ForeignKey('nodes.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __init__(self, form):
        self.title = form.get('title', '')
        self.content = form.get('content', '')
        self.created_time = timestamp()


    def update(self, form):
        self.title = form.get('title', '')
        self.content = form.get('content', '')
        self.save()

