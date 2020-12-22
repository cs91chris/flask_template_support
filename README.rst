Flask-TemplateSupport
=====================

Template support for flask application, a collection for useful extra filters and functions,
and an easy way to register them.


Quickstart
~~~~~~~~~~

Install ``flask_template_support`` using ``pip``:

::

   $ pip install Flask-TemplateSupport

.. _section-1:

Example usage
^^^^^^^^^^^^^

.. code:: python

    from flask import render_template
    from flask_template_support import TemplateSupport


    def test_sum(a, b):
        return a + b


    def test_sub(a, b):
        return a - b


    app = Flask(__name__)
    ts = TemplateSupport()

    ts.init_app(app, functs=(
	    (test_sum, 'sum'),
	    (test_sub, 'sub'),
	))

Run ``test.py`` in example folder and go to http://127.0.0.1:5000/ to see how it works


.. _section-2:

Configuration
^^^^^^^^^^^^^

1. ``NOT_AVAILABLE_DESC``: *(default: N/A)* description for or_na filter
2. ``PRETTY_DATE``: *(default: %d %B %Y %I:%M:%S %p)* default date format for pretty_date filter
3. ``HUMAN_FILE_SIZE_DIVIDER``: *(default: 1000)* default divider for human_file_size filter
4. ``HUMAN_FILE_SIZE_SCALE``: *(default: ['KB', 'MB', 'GB', 'TB'])* default scale for human_file_size filter


License MIT
