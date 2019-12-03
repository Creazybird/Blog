from app import db

# from flask import current_app, jsonify, request
class Account(db.Model):
    __tablename__='account'
    id=db.Column(db.Integer,primary_key=True)
    birthday=db.Column(db.Date)
    createTime=db.Column(db.Date)
    deleteTime=db.Column(db.Date)
    updateTime=db.Column(db.Date)
    gender=db.Column(db.Integer)
    is_delete=db.Column(db.Integer)
    name=db.Column(db.String(100))
    nation=db.Column(db.String(200))
    email=db.Column(db.String(200))
    password=db.Column(db.String(200))
    role=db.Column(db.String(200))

class Message(db.Model):
    __tablename__='message'
    id=db.Column(db.Integer,primary_key=id)
    content=db.Column(db.Text)
    accountId=db.Column(db.Integer)
    is_delete=db.Column(db.Integer)
    createTime=db.Column(db.Date)
    deleteTime=db.Column(db.Date)
    updateTime=db.Column(db.Date)

class Note(db.Model):
    __tablename__='note'
    id=db.Column(db.Integer,primary_key=id)
    classify=db.Column(db.String(200))
    content=db.Column(db.Text)
    createTime=db.Column(db.Date)
    deleteTime=db.Column(db.Date)
    updateTime=db.Column(db.Date)
    is_delete=db.Column(db.Integer)
    role=db.Column(db.String(200))
    messageId=db.Column(db.Integer)
    title=db.Column(db.Text)

