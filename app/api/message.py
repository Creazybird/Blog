
from .. import db
from . import auth
from flask import jsonify,request,session,json
from model import Message,Account
from  datetime import datetime

@auth.route('/message',methods=['POST'])
def  saveContent():
    message=Message()
    data=request.json
    if data.get('accountId')!=None and type(data.get('accountId'))==int:
        if data.get('content'):
            user=Account.query.filter_by(id=data.get('accountId')).first()
            if user:
                message.accountId=1
                message.content=data.get('content')
                message.is_delete=0
                message.createTime=datetime.today().strftime('%Y-%m-%d')
                db.session.add(message)
                db.session.commit()
                return 'message ok',200
            else:
                return 'lack content', 400
        else:
            return  'lack content',400

    else:
        return 'error',400

@auth.route('/message',methods=['GET'])
def getContent():
    para=request.args.to_dict()  # 获取query参数,这里获取的是一个ImmutableMultiDict的数据类型，调用to_dict()变成字典
    if para['accountId']:
        user=Account.query.filter_by(id=para['accountId']).first()
        message_list=Message.query.filter_by(accountId=user.id).all()
        data=[]
        for item in message_list:
            if item.is_delete==0:
                json_item={
                    'id':item.id,
                    'message':item.content,
                }
                data.append(json_item)
        res=[{'data':data}]
        return jsonify(res),200
    else:
        return 'there is no message for this accountId',400

@auth.route('/message',methods=['PUT'])
def putContent():
    data=request.json
    if data:
        if data.get('messageId'):
            q_message=Message.query.filter_by(id=data.get('messageId')).first()
            if q_message and q_message.is_delete==0:
                    q_message.content=data.get('message')
                    db.session.add(q_message)
                    db.session.commit()
                    return 'success to put',200
            else:
                return 'is None', 400
        else:
            return 'can not select messageId',400
    else:
        return 'dataform is wrong',400


@auth.route('/message',methods=['Delete'])
def deleteContent():
    para=request.args.to_dict()
    print(para)
    if para.get('messageId'):
        q_message=Message.query.filter_by(id=para.get('messageId')).first()
        if q_message.is_delete==0:
            q_message.is_delete=1
            db.session.add(q_message)
            db.session.commit()
            return 'delete success',200
        else:
            return 'this message is deleted',400
    else:
        return 'formdata is not ok',400





