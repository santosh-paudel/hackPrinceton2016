import datetime
from flask import url_for
from init import db

class Meme(db.Document):
    created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
    title = db.StringField(max_length=255, required=True)
    description = db.StringField(required=True)
    numLikes = db.IntField(min_value=0)
    url = db.URLField()
    tags = db.ListField(db.StringField(max_length=30, required=True))

    def __unicode__(self):
        return self.title

    meta = {
        'allow_inheritance': True,
        'indexes': ['-created_at'],
        'ordering': ['-created_at']
    }