# Auto-Pynance

## Requirements
- Python 3.11^
- Poetry


## Getting Started 
```bash
$ docker-compose up
```

### MARKETS
- ping : 서버와 연결 상태 확인
- time : 서버 시간을 받아옴
- exchange_info
- depth : orderbook의 매물대 정보를 받아옴
- trades : 특정심볼에 대해 최근 사용자들의 거래 기록을 가져 옴
- historical_trades
- agg_trades
- klines
- continuous_klines
- index_price_klines
- mark_price_klines
- mark_price
- funding_rate
- ticker_24hr_price_change
- ticker_price  : 현재 가격을 가져 옴
- book_ticker
- open_interest
- open_interest_hist
- top_long_short_position_ratio
- long_short_account_ratio
- top_long_short_account_ratio
- taker_long_short_ratio
- blvt_kline
- index_info
- asset_Index

### ACCOUNT(including orders and trades)
- change_position_mode
- get_position_mode
- change_multi_asset_mode
- get_multi_asset_mode
- new_order : 주문을 넣음 
- new_order_test
- new_batch_order
- query_order
- cancel_order
- cancel_open_orders
- cancel_batch_order
- countdown_cancel_order
- get_open_orders
- get_orders
- get_all_orders
- balance : 선물 지갑 내 현물 자산 현황 
- account
- change_leverage : 레버리지를 변경 함
- change_margin_type : 교차 / 격리 변경
- modify_isolated_position_margin
- get_position_margin_history
- get_position_risk
- get_account_trades : 현재 계정의 특정ㅇ 심볼에 대한 거래 기록을 가져 옴
- get_income_history
- leverage_brackets
- adl_quantile
- force_orders
- api_trading_status
- commission_rate
- download_transactions_asyn
- aysnc_download_info

### STREAMS
- new_listen_key
- renew_listen_key
- close_listen_key

### PORTFOLIO MARGIN
- pm_exchange_info
