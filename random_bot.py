import pandas as pd
from binance.client import Client
from binance import ThreadedWebsocketManager
from dotenv import dotenv_values

def simple_bot(msg):
    time = pd.to_datetime(msg['E'], unit = 'ms')
    price = float(msg['c'])
    print(f"Time: {time} | Price: {price}")
    if int(price) % 10 == 0:
        order = client.create_order(symbol='BTCUSDT', side='BUY', type='MARKET', quantity= 0.01)
        print("\n"+50*"-")
        print(f"Buy {order['executedQty']} for {order['cummulativeQuoteQty']} USDT")
        print(50 * "-" + "\n")
        twm.stop()

if __name__ == "__main__":
    config = dotenv_values(".env")
    client = Client(api_key=config['BINANCE_TEST_KEY'], api_secret=config['BINANCE_TEST_SECRET'], testnet=True)

    twm = ThreadedWebsocketManager()
    twm.start()
    twm.start_symbol_miniticker_socket(callback=simple_bot, symbol='BTCUSDT')
    twm.join()