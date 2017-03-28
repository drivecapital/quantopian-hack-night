# Hack Night + Quantopian

## Background-info
#### What is a trading algorithm?

On Quantopian, a trading algorithm is a Python program that defines two special functions: initialize() and handle_data(). initialize() is called when the program is started, and handle_data() is called once per minute during simulation or live-trading in events that we'll refer to as 'bars'. The job of initialize() is to perform any one-time startup logic. The job of handle_data() is to decide what orders, if any, should be placed each minute.

The following is an example of an algorithm that allocates 100% of its portfolio in AAPL:

    def initialize(context):
        # Reference to AAPL
        context.aapl = sid(24)

    def handle_data(context, data):
        # Position 100% of our portfolio to be long in AAPL
        order_target_percent(context.aapl, 1.00)

#### Support Links
* Home page of algorithms (check out the Hellow World Algorithm first) - https://www.quantopian.com/algorithms/
* Getting started tutorial - https://www.quantopian.com/tutorials/getting-started
