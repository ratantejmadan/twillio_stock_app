from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from basic_scripts import define_reply
app = Flask(__name__)


@app.route('/sms', methods=['GET', 'POST'])
def sms():
    message = request.values.get('Body', None)
    response = MessagingResponse()
    response.message(define_reply(message))

    return str(response)


if __name__ == '__main__':
    app.run()
