import datetime
from flask import url_for
from init import db

class Dictionary(db.EmbeddedDocument):
    key = db.StringField(max_length=30, required=True)
    value = db.IntField(min_value=0)

    def __unicode__(self):
        return self.key




class Meme(db.Document):
    created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
    title = db.StringField(max_length=255, required=True)
    description = db.StringField(required=True)
    numLikes = db.IntField(min_value=0)
    numShares = db.IntField(min_value=0)
    numDownloads = db.IntField(min_value=0)
    url = db.StringField()
    native_tags = db.ListField(db.StringField(max_length=30, required=True))
    foreign_tags = db.ListField(db.StringField(max_length=30, required=True))

    def __unicode__(self):
        return self.title

    meta = {
        'allow_inheritance': True,
        'indexes': ['-created_at'],
        'ordering': ['-created_at']
    }


class User(db.Document):
    created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
    firstName = db.StringField(max_length=100, required=True)
    lastName = db.StringField(max_length=100, required=True)
    email = db.EmailField(max_length=100, required=True)
    userName = db.StringField(max_length=20, required=True)
    password = db.StringField(max_length=20, required=True)
    localeCount = db.ListField(db.EmbeddedDocumentField(Dictionary, required=True), required=True)

    def __unicode__(self):
        return self.userName

    meta = {
        'allow_inheritance': True,
        'indexes': ['-created_at'],
        'ordering': ['-created_at']
    }


class Tag(db.Document):
    tag = db.StringField(max_length=30, required=True)
    locale = db.StringField(max_length=30, required=True)

    def __unicode__(self):
        return self.tag

class Locale(db.Document):
    locale = db.StringField(max_length=30, required=True)

    def __unicode__(self):
        return self.locale

