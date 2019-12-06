from .. import db
from . import auth
from flask import jsonify,request,session,json
from model import Note
from  datetime import datetime
from textrank4zh import TextRank4Sentence

def getAbstract(text,num=3):
    tr4s = TextRank4Sentence()
    tr4s.analyze(text=text, lower=True, source='all_filters')
    # return [item.sentence for item in tr4s.get_key_sentences(num)]
    res=''
    for item in tr4s.get_key_sentences(num):
        res=res+item.sentence
    return res+'...'


@auth.route('/note',methods=['POST'])
def postNote():
    print(request)
    data=request.json
    print(data)
    if data.get('title')==None or data.get('content')==None or data.get('classify')==None or data.get('role')==None:
        return '创建的笔记不符合格式,缺少参数','400'
    elif data.get('role')=='Super':
        note=Note()
        note.is_delete=0
        note.createTime=datetime.today().strftime('%Y-%m-%d')
        note.title=data.get('title')
        note.content = data.get('content')
        note.classify = data.get('classify')
        note.role = data.get('role')
        db.session.add(note)
        db.session.commit()
        return 'success' ,200
    else:
        return '权限不够',401

@auth.route('/note',methods=['GET'])
def getNote():
    para=request.args.to_dict()
    #一页10条
    #python中也没有块级作用域
    if para.get('page'):
        post_page=int(para.get('page'),10)
        if post_page != None and post_page != 0:
            page = post_page
            resNote = Note.query.filter_by(is_delete=0).order_by(Note.id.desc()).limit(10).offset((page - 1) * 10).all()
        elif post_page == 0:
            resNote = Note.query.filter_by(is_delete=0).order_by(Note.id.desc()).all()
        else:
            return 'page is null', 400
        data = []
        for item in resNote:
            temp = {
                'id': item.id,
                'title': item.title,
                'content': item.content,
                'abstract': getAbstract(item.content),
                'classify': item.classify,
                'createTime': item.createTime.strftime('%Y-%m-%d %H:%M:%S'),  # 通过strftime装换
            }
            data.append(temp)
        res = {'data': data}
        return jsonify(res), 200
    elif para.get('noteId'):
        noteID=int(para.get('noteId'),10)
        if noteID==None:
            return 'need a valid messageId',400
        else:
            queryNote=Note.query.filter_by(id=noteID).first()
            temp={
                'id': queryNote.id,
                'title': queryNote.title,
                'content': queryNote.content,
                'classify': queryNote.classify,
                'createTime': queryNote.createTime.strftime('%Y-%m-%d %H:%M:%S')
            }
            res={'data':temp}
            return jsonify(res),200
    else:
        return 'less required para',400
