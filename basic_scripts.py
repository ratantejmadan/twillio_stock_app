from yahoo_fin import stock_info as yf
from yahoo_fin.stock_info import get_company_info, get_currencies, \
    get_earnings_history, \
    get_stats
from main_storage import program_masterbase, time_types, users_to_target_tracker
from price_target import PriceTarget
import pandas as pd


def define_reply(message, number):
    text = list(message.split(" "))
    if len(text) > 1:
        ticker = text[1]
    else:
        ticker = ""
    x = yf.get_day_gainers()
    host_response = "Command not recognized. Please try again."
    if text[0] == "PLSHELP":
        host_response = "Welcome to the stock help app!"
    elif text[0] == "PRICE":
        if ticker:
            price = yf.get_live_price(ticker)
            host_response = ticker + \
                " is currently trading at $" + "{:.2f}".format(price)
        else:
            host_response = "Ticker missing. Please specify the stock ticker"
    elif text[0] == "GETSTOCKSTATS":
        host_response = get_stats('NFLX')
    elif text[0] == "INFO":
        host_response = text[1]
    elif message == "TOPRISERS":
        host_response = "1.2.3.4.5"
    elif message == "MARKETS":
        host_response = "MARKETS"
    elif message == "INDUSTRIES":
        host_response = "INDUSTRIES"
    elif text[0] == "CURRENCIES":
        host_response = currency_parser()
    elif message == "SETPRICETARGET":
        if number not in users_to_target_tracker:
            users_to_target_tracker[number] = 0
        users_to_target_tracker[number] += 1
        newtarg = PriceTarget(text[1], text[2], text[3], users_to_target_tracker[number])
        program_masterbase[number][text[3]].append(newtarg)
        host_response = f"We set a price target of {text[2]} on {text[1]} for you. " \
                        f"We'll let you know if the stock reaches your target this {text[3]}!"
    elif message == "SEEALLPRICETARGETS":
        host_response = str(program_masterbase[number])
    elif message == "CLEARALLPRICETARGETS":
        for time in time_types:
            program_masterbase[number][time] = []
        host_response = "We've cleared all of your price targets. " \
                        "Type SETPRICETARGET {Stock Ticker} {Price} {Time Period} " \
                        "to set some new ones!"
    elif text[0] == "CLEARPRICETARGETS":
        program_masterbase[number][text[1]] = []
        host_response = f"We've cleared all price targets for this {text[1]}. "\
                        "Type SETPRICETARGET {Stock Ticker} {Price} {Time Period}"\
                        "to set some new ones!"
    elif text[0] == "DELETETARGET":
        for timeslot in program_masterbase[number]:
            for target in timeslot:
                if target.number == text[1]:
                    timeslot.remove(target)
        host_response = "We deleted the target."
    else:
        host_response = "Command not recognized. Please try again."
    return host_response


def currency_parser():
    curr_stats = ""
    for i in range(0, len(get_currencies()["Name"])):
        curr_stats = (get_currencies()["Name"][i] + " " + str(get_currencies()["Last Price"][i])
              + " " + str(get_currencies()["Change"][i]) + " " + str(get_currencies()["% Change"][i]))

    return curr_stats

currency_parser()
