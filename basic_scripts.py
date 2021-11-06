from twilio.rest import Client
import yfinance as yf
# from yahoo_finance import Share


def send_sms(numbers, string):
    account_sid = ""
    auth_token  = ""
    client = Client(account_sid, auth_token)
    for i in range(len(numbers)):
        message = client.messages.create(
            to=numbers[i],
            from_="",
            body=string)
        print(message.sid)


def define_reply(message):
    test = list(message.split(" "))
    if test[0] == "HELP":
        host_response = "Welcome to the stock help app"
    elif test[0] == "PRICE":
        ticker = yf.Ticker(test[1])
        host_response = test[1] + "price is " + ticker.info[""]
    elif test[0] == "INFO":
        host_response = test[1]
    elif message == "TOPRISERS":
        host_response = "1.2.3.4.5"
    elif message == "MARKETS":
        host_response = "MARKETS"
    elif message == "INDUSTRIES":
        host_response = "INDUSTRIES"
    elif message == "SETPRICETARGET":
        host_response = "SETPRICETARGET"
    elif message == "CLEARALLPRICETARGETS":
        host_response = "CLEARALLPRICETARGETS"
    elif message == "CLEARALLPRICETARGETS":
        host_response = "CLEARALLPRICETARGETS"
    elif message == "DELETETARGET":
        host_response = "DELETETARGET"
    else:
        host_response = "Command not recognized. Please try again."
    return host_response
