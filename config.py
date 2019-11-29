# config.py主要来放数据库的配置文件
# 在实际开发中，一般将开发，测试，生产链接的是不同的数据库，一套代码多个数据库，
# 对不同的工作使用数据库，开发模块相互独立
import os
basedir =os.path.abspath(os.path.dirname(__file__))
# DIALECT=''
# DRIVER=''
# USERNAME=''
# PASSWORD=''
# HOST=''
# PORT=''
# DATABASE=''
DIALECT = 'mysql'  # 要用的什么数据库
DRIVER = 'pymysql'  # 连接数据库驱动
USERNAME = 'root'  # 用户名
PASSWORD = 'bird'  # 密码
HOST = 'localhost'  # 服务器
PORT = '3306'  # 端口
DATABASE = 'blog'  # 数据库名

#Config基类中包含通用配置，各个子类分别定义专用的配置。如果需要，你还可添加其他的配置

class Config:
    WEBNET_SECRET_KEY=os.getenv('WEBNET_SECRET_KEY')  # os.getenv 获取环境变量
    SESSION_TYPE='filesystem'
    SQLALCHENY_COMMIT_ON_TEARDOWN=True
    SQLALCHENY_RECORD_QUERITES=True
    SQLALCHEMY_TRACK_MODIFICATIONS=True

    @staticmethod       #这里是一个占位函数
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG=True
    SQLALCHEMY_DATABASE_URI=\
        "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(
        DIALECT,
        DRIVER,
        USERNAME,
        PASSWORD,
        HOST,
        PORT,
        DATABASE
    )
    @classmethod   #实例化
    def init_app(cls,app):
        Config.init_app(app)



class TestingConfig(Config):
    DEBUG=True
    SQLALCHEMY_DATABASE_URI=\
        "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(
        DIALECT,
        DRIVER,
        USERNAME,
        PASSWORD,
        HOST,
        PORT,
        DATABASE
    )

class ProductionConfig(Config):
    DEBUG=True
    SQLALCHEMY_DATABASE_URI=\
        "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(
        DIALECT,
        DRIVER,
        USERNAME,
        PASSWORD,
        HOST,
        PORT,
        DATABASE
    )

config={
    'development':DevelopmentConfig,
    'testing':TestingConfig,
    'production':ProductionConfig,
    'default':DevelopmentConfig,
}