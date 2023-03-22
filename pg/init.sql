CREATE TABLE IF NOT EXISTS ticker_data (
    market                  varchar     primary key not null,
    symbol                  varchar     primary key not null,
    interval                varchar     primary key not null,
    open_time               bigint      primary key not null,

    open                    real        not null,
    high                    real        not null,
    low                     real        not null,
    close                   real        not null,
    volume                  real        not null,
    close_time              bigint      not null,
    count                   integer,
    taker_buy_volume        real,
    taker_buy_quote_volume  real
);

