"""
I really like Tesla and am not a fan of Twitter. However, because I'm not a smart man I have a hunch that during the summer Twitter is going to be HOT, so I will buy.
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
            if get_datetime().month in [5, 6, 7]:
                order_target_percent(context.twitter, 0.5)
            else:
                order_target_percent(context.twitter, -0.5)
            
    if data.can_trade(context.tesla):
        order_target_percent(context.tesla, 0.5)