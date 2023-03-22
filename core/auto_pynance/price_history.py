from datetime import datetime, timedelta
import requests
import zipfile
import io


def get_usdm_data(symbol: str, interval = '1m', start_date = datetime(2020, 1, 1)):
    sess = requests.session()
    today = datetime.today()
    current = start_date
    while current < today:
        try:
            target = f'{symbol}-{interval}-{current.year:04}-{current.month:02}-{current.day:02}'
            target_url = f'https://data.binance.vision/data/futures/um/daily/klines/{symbol}/{interval}/{target}.zip'

            res = sess.get(target_url)
            if res.content[0:2] == b'PK':
                file = io.BytesIO(res.content)
                with zipfile.ZipFile(file, 'r') as z:
                    print(f'[+] Extracting {target}.csv')
                    z.extractall(f'./usdm-data')            
            usdm_header = 'open_time,open,high,low,close,volume,close_time,quote_volume,count,taker_buy_volume,taker_buy_quote_volume,ignore\n'
            with open(f'./usdm-data/{target}.csv', 'r+') as f:
                content = f.read()
                header = content[:len(usdm_header)]
                if header != usdm_header:
                    f.seek(0, 0)
                    f.write(usdm_header + content)
        except Exception:
            pass
        current += timedelta(days=1)

get_usdm_data('BTCUSDT')