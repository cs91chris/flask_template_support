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
    return render_template('test.html')


if __name__ == '__main__':
    app.run()
