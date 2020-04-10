from flask import Flask
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


@app.route('/')
def index():
    return render_template(
        'test.html',
        long_text="""
Lorem ipsum dolor sit amet, consectetur adipiscing elit,
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris
nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in
reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
Excepteur sint occaecat cupidatat non proident,
sunt in culpa qui officia deserunt mollit anim id est laborum.
    """)


if __name__ == '__main__':
    app.run()
