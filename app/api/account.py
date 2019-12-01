
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
        account.is_delete=0
        account.createTime=datetime.today().strftime('%Y-%m-%d')
        db.session.add(account)
        db.session.commit()
        return  'success',200

@auth.route('/account',methods=['GET'])
def getAllAccount():
    para=request.args.to_dict()
    if para=={}:
        #获取所有的账户信息
        accounts=Account.query.filter_by(is_delete=0).all()
    elif para.get('accountId'):
        accounts=Account.query.filter_by(id=para.get('accountId'),is_delete=0).all()
    else:
        return 'format error',400
    data=[]
    for item in accounts:
        acc_item={
            'id':item.id,
            'name':item.name,
            'email':item.email,
            'role':item.role,
        }
        data.append(acc_item)
    return jsonify(data),200

@auth.route('/account',methods=['DELETE'])
def deleteAccount():
    #删除账号，管理员账号是不能删除的
    #实现批量删除,这里的删除都是软删除
    para=request.args.to_dict()
    if para.get('accountId'):
         accList=para.get('accountId').split(',')
         for item in accList:
             account=Account.query.filter_by(id=item).first()
             account.is_delete=1
             db.session.add(account)
             db.session.commit()
         return 'delete is success',200
    else:
        return '传入的参数错误',400



