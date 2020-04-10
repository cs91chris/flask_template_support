from .version import *
from .functions import now
from .filters import or_na, reverse, order_by, truncate, yes_or_no, pretty_date

DEFAULT_FILTERS = (
    (or_na, None),
    (yes_or_no, None),
    (reverse, None),
    (pretty_date, None),
    (order_by, None),
    (truncate, None),
)

DEFAULT_FUNCTIONS = (
    (now, None),
)

from .template_support import TemplateSupport
