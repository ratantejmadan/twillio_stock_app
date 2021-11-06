from yahoo_fin import stock_info as yf
from price_target import PriceTarget
from main import program_masterbase
def define_reply(message, number):
    text = list(message.split(" "))
    if len(text) > 1:
        ticker = text[1]
    else:
        ticker = ""
    x = yf.get_day_gainers()
    host_response = "Command not recognized. Please try again."
    if text[0] == "PLSHELP":
        host_response = "Welcome to the stock help app"
    elif text[0] == "PRICE":
        if ticker:
            price = yf.get_live_price(ticker)
            host_response = ticker + \
                " is currently trading at $" + "{:.2f}".format(price)
        else:
            host_response = "Ticker missing. Please specify the stock ticker"
    elif text[0] == "INFO":
        host_response = text[1]
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
