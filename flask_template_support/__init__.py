from .filters import or_na
from .filters import reverse
from .filters import order_by
from .filters import truncate
from .filters import yes_or_no
from .filters import pretty_date

from .functions import now


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
