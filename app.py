from flask import Flask, render_template, request, jsonify


app = Flask(__name__)
import json

f=open("config.json","r")
config=json.load(f)
f.close()


WEBPORT=config['websitePort']

input_restriction= False
received_message = "initial placeholder"  # 用于存储服务器端收到的消息
sent_message = "initial placeholder"

@app.route('/data')
def get_data():
    # 在这里获取数据，这里简单地返回一个字典作为示例

    return jsonify({'received_message':received_message, 'sent_message':sent_message,'input_restriction':input_restriction})

@app.route('/')
def index():
    return render_template('index.html', message=received_message,received_message=received_message)

@app.route('/send', methods=['POST'])
def send_message():
    global sent_message
    global input_restriction
    sent_message = request.data.decode('utf-8')  # 将接收到的数据解码为字符串

    input_restriction=True
    return sent_message

@app.route('/whatareyousaying', methods=['POST'])
def receive_query():
    return sent_message

@app.route('/receive', methods=['POST'])
def receive_message():
    global received_message
    global input_restriction
    received_message = request.data.decode('utf-8')  # 将接收到的数据解码为字符串\
    print("received"+ received_message)
    input_restriction=False
    #return jsonify({'script': 'updateReceivedMsg(' + received_message + ');'})
    #return 'Message received successfully! from receive_message888'
    return "message received by website, thanks"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=WEBPORT)
