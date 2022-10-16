import logging


logging.basicConfig(filename='Employee.log', level='ERROR',
                    format='%(asctime)s:%(levelname)s:%(message)s')


def leap_year(year_):
    if year_ % 400 == 0 and (year % 100 == 0):
        logging.info('Leap year: {}'.format(year_))

    elif year_ % 4 == 0 and year_ % 100 != 0:
        logging.info('Leap year: {}'.format(year_))

    else:
        logging.info('not Leap year: {}'.format(year_))


if __name__ == '__main__':
    year = int(input("enter the year u want to check "))
    leap_year(year)
