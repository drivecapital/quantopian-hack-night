"""
Hypothesis behind this algorithm:
If the 10-day simple moving average (short SMA) of a security is higher than its 30-day simple moving average (long SMA), the price of the security will drop.
Conversely, if its short SMA is lower than its long SMA, the price will go up. This is referred to as mean reversion.

However, I *always* want to go long on Facebook and Netflix. Love those guys.
"""

def initialize(context):
    """
    initialize() is called once at the start of the program. Any one-time
    startup logic goes here.
    """

    # Microsoft + FANG:
    context.security_list = [
        sid(5061), # MSFT
        sid(24), # AAPL
        sid(23709), # NFLX
        sid(42950), # FB
        sid(46631) # GOOG
    ]

    # Rebalance every Monday (or the first trading day if it's a holiday)
    # at market open.
    schedule_function(rebalance,
                      date_rules.week_start(days_offset=0),
                      time_rules.market_open())

def compute_weights(context, data):
    """
    Compute weights for each security that we want to order.
    """

    # Get the 30-day price history for each security in our list.
    hist = data.history(context.security_list, 'price', 30, '1d')

    # Create 10-day and 30-day trailing windows.
    prices_10 = hist[-10:]
    prices_30 = hist

    # 10-day and 30-day simple moving average (SMA)
    sma_10 = prices_10.mean()
    sma_30 = prices_30.mean()

    # Weights are based on the relative difference between the short and long SMAs
    raw_weights = (sma_30 - sma_10) / sma_30

    # Normalize our weights
    normalized_weights = raw_weights / raw_weights.abs().sum()

    # Determine and log our long and short positions.
    short_secs = normalized_weights.index[normalized_weights < 0]
    long_secs = normalized_weights.index[normalized_weights > 0]
    
    always_go_long = ['NFLX', 'FB']

    log.info("This week's longs: " + ", ".join([long_.symbol for long_ in long_secs]))
    log.info("This week's shorts: " + ", ".join([short_.symbol for short_ in short_secs if short_.symbol not in always_go_long]))

    # Return our normalized weights. These will be used when placing orders later.
    return normalized_weights

def rebalance(context, data):
    """
    This function is called according to our schedule_function settings and calls
    order_target_percent() on every security in weights.
    """

    # Calculate our target weights.
    weights = compute_weights(context, data)

    # Place orders for each of our securities.
    for security in context.security_list:
        if data.can_trade(security):
            if security.symbol == 'NFLX' or security.symbol == 'FB':
                # I'm going big on these two
                # Note that the abs() makes this value always positive, so I always go long
                order_target_percent(security, abs(weights[security] * 2))
            else:
                # Want to dampen the other stocks' amounts a bit
                order_target_percent(security, weights[security] * 0.75)
