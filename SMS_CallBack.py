from flask import Flask, request
import datetime

app = Flask(__name__, static_folder='static')


@app.route('/')
def home():
    return app.send_static_file('myfile.txt') # quick and dirty way to put POST values on a webpage


@app.route("/MessageStatus", methods=["POST"])
def incoming_sms():
    #Grab the correct values to show the delivery API response
    message_sid = request.values.get('MessageSid', None)
    message_status = request.values.get('MessageStatus', None)
    message_to = request.values.get('To')
    message_from = request.values.get('From')
    message_date = datetime.datetime.now()

    #Debug to see if the values are pulling correct
    print('Time of Message: ' + message_date.strftime(
        '%y-%m-%d %H:%M:%S') + '   To: ' + message_to + '   From: ' + message_from + '   SID: ' + message_sid + '   Status: ' + message_status)
    #File to save values
    file1 = open('static/myfile.txt', 'a')
    #Save values and meta data to be pulled by root www
    file1.write('Time of Message: ' + message_date.strftime(
        '%y-%m-%d %H:%M:%S') + '   To: ' + message_to + '   From: ' + message_from + '   SID: ' + message_sid + '   Status: ' + message_status + '\n')

    return ('')


if __name__ == "__main__":
    app.run(debug=True)
