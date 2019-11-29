
from .. import db
from . import auth
from flask import jsonify,request,session,json
from model import Account,Message
from  datetime import datetime

@auth.route('/create',methods=['POST'])
def createAccount():
    form=request.json
    account = Account()
    print(form)
    print(type(form))
    if form==None:
        return 'error',401
    elif form.get('role')==None or form.get('password')==None or form.get('email')==None:
        return 'data lack',400
    else:
        account.role=form.get('role')
        account.password=form.get('password')
        account.email=form.get('email')
        account.birthday=form.get('birthday')
        account.gender=form.get('gender')
        account.nation=form.get('nation')
        account.name=form.get('name')
        account.createTime=datetime.today().strftime('%Y-%m-%d')
        db.session.add(account)
        db.session.commit()
        return  'success',200
