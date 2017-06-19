from flask import Flask



app = Flask(__name__)

@app.route('/v1', methods = ['GET'])
def v1():
    return app.send_static_file('button_v1.html')

@app.route('/v2', methods = ['GET'])
def v2():
    return app.send_static_file('button_v2.html')

@app.route('/v3', methods = ['GET'])
def v3():
    return app.send_static_file('button_v3.html')


if __name__ == '__main__':
    app.run()
    #app.run(host='0.0.0.0', port=5000)