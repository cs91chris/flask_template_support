from datetime import datetime
from operator import itemgetter

from dateutil.parser import parse


def or_na(item):
    """

    :param item:
    :return:
    """
    if not item:
        return 'n/a'
    return item


def yes_or_no(item: bool):
    """

    :param item:
    :return:
    """
    return 'yes' if item else 'no'


def reverse(s: list):
    """

    :param s:
    :return:
    """
    return s[::-1]


def pretty_date(date, fmt=None):
    """

    :param date:
    :param fmt:
    :return:
    """
    fmt = fmt or "%d %B %Y %I:%M:%S %p"

    if date:
        if isinstance(date, datetime):
            return date.strftime(fmt)

        return parse(date).strftime(fmt)
    return None


# noinspection PyShadowingNames
def order_by(data, item, reverse=False, silent=True):
    """

    :param data: list of objects
    :param item: item of the object according to which to order
    :param reverse: reverse order
    :param silent: raise or not exception
    :return:
    """
    try:
        return sorted(
            data,
            key=itemgetter(item),
            reverse=reverse
        )
    except KeyError:
        if silent:
            return data
        else:
            raise


def truncate(data, n, terminator=None):
    """

    :param data: input string
    :param n: max length of string
    :param terminator: string to append to output
    :return:
    """
    term = terminator or '...'
    return "{}{}".format(data[:n], term)
