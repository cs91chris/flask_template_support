Flask-TemplateSupport
=====================

Template support for flask application


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

Run ``test.py`` in example folder and go to http://127.0.0.1:5000/ to see if it works


License MIT
