"""
I am superstitious and also an idiot. 
"""

def initialize(context):
    """
    initialize() is called once at the start of the program. Any one-time
    startup logic goes here.
    """

    context.twitter = sid(45815) 
    context.tesla = sid(39840)

    # Rebalance every Monday (or the first trading day if it's a holiday)
    # at market open.
    schedule_function(rebalance,
                      date_rules.week_start(days_offset=0),
                      time_rules.market_open())

def rebalance(context, data):
    """
    This function is called according to our schedule_function settings and calls
    order_target_percent() on Twitter and Tesla.
    """

    # Place orders for each of our securities.
    if data.can_trade(context.twitter):
        log.info(data.current(context.twitter, 'price'))
        current_twitter_price = data.current(context.twitter, 'price')
        cents_part = float("{0:.2f}".format(current_twitter_price % 1))
        # If the cents portion of the stock is divisible by 3, everyone knows that is bad luck for social network stocks
        if cents_part * 100 % 3 == 0.0:
            log.info('Shorting!')
            order_target_percent(context.twitter, -0.5)
        else:
            order_target_percent(context.twitter, 0.5)
            
    if data.can_trade(context.tesla):
        current_tesla_price = data.current(context.tesla, 'price')
        cents_part = float("{0:.2f}".format(current_tesla_price % 1))
        # If the cents portion of the stock is an odd number, it's bad luck for cars, obviously
        if cents_part * 100 % 2 != 0.0:
            order_target_percent(context.tesla, -0.5)
        else:
            order_target_percent(context.tesla, 0.5)