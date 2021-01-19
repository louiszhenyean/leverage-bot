import config
import keys
from binance.client import Client

def get_current_minute(): # >>> RED_CANDLE // GREEN_CANDLE // WEAK_RED // WEAK_GREEN // RED_INDECISIVE // GREEN_INDECISIVE // SOMETHING_IS_WRONG
    klines = keys.client.futures_klines(symbol=config.pair, interval=Client.KLINE_INTERVAL_1MINUTE, limit=3)

    first_run_Open  = round(((float(klines[0][1]) + float(klines[0][4])) / 2), 2)
    first_run_Close = round(((float(klines[0][1]) + float(klines[0][2]) + float(klines[0][3]) + float(klines[0][4])) / 4), 2)
    previous_Open   = round(((first_run_Open + first_run_Close) / 2), 2)
    previous_Close  = round(((float(klines[1][1]) + float(klines[1][2]) + float(klines[1][3]) + float(klines[1][4])) / 4), 2)

    # current_Time    = int(klines[2][0])
    current_Open    = round(((previous_Open + previous_Close) / 2), 2)
    current_Close   = round(((float(klines[2][1]) + float(klines[2][2]) + float(klines[2][3]) + float(klines[2][4])) / 4), 2)
    current_High    = max(float(klines[2][2]), current_Open, current_Close)
    current_Low     = min(float(klines[2][3]), current_Open, current_Close)

    price_movement = (current_High - current_Low) / current_Open * 100

    # print("The current_Time is  :   " + str(current_Time))
    # print("The current_Open is  :   " + str(current_Open))
    # print("The current_Close is :   " + str(current_Close))
    # print("The current_High is  :   " + str(current_High))
    # print("The current_Low is   :   " + str(current_Low))
    # print("The price_movement is:   " + str(price_movement))

    if (current_Open == current_High):
        if (price_movement >= config.threshold):
            minute_candle = "RED_CANDLE"
            print("Current MINUTE   :   🩸🩸🩸 RED 🩸🩸🩸")
        else:
            minute_candle = "WEAK_RED"
            print("Current MINUTE   :   🩸 WEAK_RED 🩸")
    elif (current_Open == current_Low):
        if (price_movement >= config.threshold):
            minute_candle = "GREEN_CANDLE"
            print("Current MINUTE   :   🥦🥦🥦 GREEN 🥦🥦🥦")
        else:
            minute_candle = "WEAK_GREEN"
            print("Current MINUTE   :   🥦 WEAK_GREEN 🥦")
    else:
        if (current_Open > current_Close):
            print("Current MINUTE   :   🩸 RED_INDECISIVE 🩸")
            minute_candle = "RED_INDECISIVE"
        elif (current_Close > current_Open):
            print("Current MINUTE   :   🥦 GREEN_INDECISIVE 🥦")
            minute_candle = "GREEN_INDECISIVE"
        else:
            minute_candle = "SOMETHING_IS_WRONG"
            print("❗SOMETHING_IS_WRONG in get_minute_candle()❗")
    return minute_candle