import datetime
from flask import url_for
from mem import db

class Post(db.Document):
    created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
    title = db.StringField(max_length=255, required=True)
    description = db.StringField(required=True)
    comments = db.ListField(db.EmbeddedDocumentField('Comment'))
    numLikes = db.IntField(min_value=0)
    url = db.URLField()

    def get_absolute_url(self):
        return url_for('post', kwargs={"slug": self.slug})

    def __unicode__(self):
        return self.title

    meta = 
    {
        'allow_inheritance': True,
        'indexes': ['-created_at', 'slug'],
        'ordering': ['-created_at']
    }