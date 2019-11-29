from app import create_app
if __name__ == '__main__':
    app=create_app()
    app.config['JSON_AS_ASCII'] = False  #不出现中文乱码
    app.run()
