from datetime import datetime
from dateutil.parser import parse

from operator import itemgetter


def or_na(item):
    """

    :param item:
    :return:
    """
    if not item:
        return 'N/A'
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


def pretty_date(date, fmt="%d %B %Y %I:%M:%S %p"):
    """

    :param date:
    :param fmt:
    :return:
    """
    if date:
        if isinstance(date, datetime):
            return date.strftime(fmt)
        return parse(date).strftime(fmt)
    return None


def order_by(data: list, item, reverse=False):
    """

    :param data:
    :param item:
    :param reverse:
    :return:
    """
    try:
        return sorted(
            data,
            key=itemgetter(item),
            reverse=reverse
        )
    except KeyError:
        return data


def truncate(data: str, n):
    """

    :param data:
    :param n:
    :return:
    """
    return ' '.join(data.split()[:n])
