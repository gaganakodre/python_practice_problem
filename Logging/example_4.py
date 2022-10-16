import logging

logger = logging.getLogger(__name__)

logging.basicConfig(filename='sample.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')


def add(x, y):
    """add function"""
    return x + y


def subtract(x, y):
    """subtract function"""
    return x - y


def multiply(x, y):
    """multiply function"""
    return x * y


def divide(x, y):
    """divide function"""
    return x / y


num_1 = 30
num_2 = 20

add_result = add(num_1, num_2)
logger.info('add: {} + {} = {} '.format(num_1, num_2, add_result))

subtract_result = subtract(num_1, num_2)
logger.info('sub: {} - {} = {} '.format(num_1, num_2, subtract_result))

multiply_result = multiply(num_1, num_2)
# print('mul: {} * {} = {} '.format(num_1, num_2, multiply_result))
logger.info('mul: {} * {} = {} '.format(num_1, num_2, multiply_result))

divide_result = divide(num_1, num_2)
# logging.info()()('div: {} / {} = {} '.format(num_1, num_2, divide_result))
logger.info('div: {} / {} = {} '.format(num_1, num_2, divide_result))
