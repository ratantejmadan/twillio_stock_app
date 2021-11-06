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
        host_response = "Functionality not yet supported."
    elif message == "MARKETS":
        host_response = "Functionality not yet supported."
    elif message == "INDUSTRIES":
        host_response = "Functionality not yet supported."
    elif text[0] == "SETPRICETARGET":
        new_targ = PriceTarget(text[1], text[2], text[3])
        program_masterbase[number][text[3]].append(new_targ)
        host_response = "We'll let you know if your stock reaches this price. Cheers!"
    elif message == "CLEARALLPRICETARGETS":
        host_response = "We cleared all of your existing price targets."
        for target in program_masterbase[]
    elif message == "CLEARALLPRICETARGETS":
        host_response = "Functionality not yet supported."
    elif message == "DELETETARGET":
        host_response = "Functionality not yet supported."

    return host_response
