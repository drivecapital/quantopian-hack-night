# Hack Night + Quantopian

## Background-info
#### What is a trading algorithm?
Algorithmic trading is a method of executing a large order (too large to fill all at once) using automated pre-programmed trading instructions accounting for variables such as time, price, and volume to send small slices of the order (child orders) out to the market over time. They were developed so that traders do not need to constantly watch a stock and repeatedly send those slices out manually. 

On Quantopian, a trading algorithm is a Python program that defines two special functions: initialize() and handle_data(). initialize() is called when the program is started, and handle_data() is called once per minute during simulation or live-trading in events that we'll refer to as 'bars'. The job of initialize() is to perform any one-time startup logic. The job of handle_data() is to decide what orders, if any, should be placed each minute.

The following is an example of an algorithm that allocates 100% of its portfolio in AAPL:

    def initialize(context):
        # Reference to AAPL
        context.aapl = sid(24)

    def handle_data(context, data):
        # Position 100% of our portfolio to be long in AAPL
        order_target_percent(context.aapl, 1.00)
        
#### Start writing code
Home page of algorithms (check out the Hellow World Algorithm first) - https://www.quantopian.com/algorithms/

#### Check out the examples folder here
I've provided a few simple examples of algorithms I've built/tested using some well known stocks.

See how high (or low!) of a return you can get.

#### Support Links
###### Quantopian-specific
* Getting started tutorial - https://www.quantopian.com/tutorials/getting-started
* API overview - https://www.quantopian.com/help
* Advanced tips (almost certainly beyond the scope of this project) - https://www.quantopian.com/posts/tips-for-writing-robust-algorithms-for-the-hedge-fund

###### General
* What is algoirthmic trading? - https://en.wikipedia.org/wiki/Algorithmic_trading
* Deep dive on high frequency trading (Quantopian is much more low frequency trading, but this is still interesting) - http://www.investopedia.com/news/highfrequency-trading-primer/
* Basic Python Docs - https://docs.python.org/2.7/
* Free 6 week course on Python -https://www.udacity.com/course/programming-foundations-with-python--ud036
