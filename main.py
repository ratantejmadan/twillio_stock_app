from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from basic_scripts import define_reply
import datetime
from yahoo_fin import stock_info as yf
# from user import add_user
app = Flask(__name__)

numbers = []
program_masterbase = {}
time_types = ["Hour", "Day", "Week", "Month", "Quarter", "Year"]


def target_monitor():
    while True:
        for user in program_masterbase:
            for time_type in time_types:
                for target in program_masterbase[user][time_type]:
                    if datetime.datetime.now() == target:
                        program_masterbase[user][time_type].remove(target)
                        response = MessagingResponse()

                        response.message(f"Hello, {target.ticker} is currently trading at {yf.get_live_price(target.ticker)}")
                        return str(response)


@app.route('/sms', methods=['GET', 'POST'])
def sms():
    number = request.form['From']
    message = request.values.get('Body', None)
    response = MessagingResponse()
    response.message(define_reply(message, number))
    target_monitor()

    return str(response)



if __name__ == '__main__':
    app.run()
