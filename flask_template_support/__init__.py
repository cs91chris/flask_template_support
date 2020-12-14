from .filters import or_na, order_by, pretty_date, reverse, truncate, yes_or_no
from .functions import now
from .version import *

DEFAULT_FILTERS = {
    "or_na":       (or_na, None),
    "yes_or_no":   (yes_or_no, None),
    "reverse":     (reverse, None),
    "pretty_date": (pretty_date, None),
    "order_by":    (order_by, None),
    "truncate":    (truncate, None),
}

DEFAULT_FUNCTIONS = {
    "now": (now, None),
}

from .template_support import TemplateSupport
