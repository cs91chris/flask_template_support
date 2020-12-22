from flask_template_support import DEFAULT_FILTERS, DEFAULT_FUNCTIONS


class TemplateSupport:
    def __init__(self, app=None, **kwargs):
        """

        :param app:
        """
        self._app = app
        if self._app:
            self.init_app(app, **kwargs)

    def init_app(self, app, filters=None, functions=None):
        """

        :param functions: function's tuple
        :param filters: filter's tuple
        :param app:
        """
        self._app = app

        if not hasattr(app, 'extensions'):
            app.extensions = dict()
        app.extensions['template_support'] = self

        self.set_default_config(app)

        filters = {**DEFAULT_FILTERS, **(filters or {})}
        functions = {**DEFAULT_FUNCTIONS, **(functions or {})}
        self.register_filters(filters.values())
        self.register_functions(functions.values())

    @staticmethod
    def set_default_config(app):
        """

        :param app:
        """
        app.config.setdefault('NOT_AVAILABLE_DESC', "N/A")
        app.config.setdefault('PRETTY_DATE', "%d %B %Y %I:%M:%S %p")
        app.config.setdefault('HUMAN_FILE_SIZE_DIVIDER', 1000)
        app.config.setdefault('HUMAN_FILE_SIZE_SCALE', ['KB', 'MB', 'GB', 'TB'])

    def register_functions(self, functions):
        """

        :param functions: function's tuple
        """
        for f in functions:
            if isinstance(f, tuple):
                self._register_function(f[0], f[1])
            else:
                self._register_function(f)

    def register_filters(self, filters):
        """

        :param filters: filter's tuple
        """
        for f in filters:
            if isinstance(f, tuple):
                self._register_filter(f[0], f[1])
            else:
                self._register_filter(f)

    def _register_function(self, template_function, name=None):
        """

        :param template_function:
        :param name:
        :return:
        """

        def create_callback(n, f):
            """

            :param n: function name
            :param f: function reference
            :return:
            """

            def callback():
                """

                :return: dict
                """
                return {n: f}

            return callback

        _name = name or template_function.__name__

        self._app.template_context_processors[None].append(
            create_callback(_name, template_function)
        )
        self._app.logger.debug("Registered function: '{}'".format(_name))

    def _register_filter(self, template_filter, name=None):
        """

        :param template_filter:
        :param name:
        """
        _name = name or template_filter.__name__

        self._app.add_template_filter(template_filter, _name)
        self._app.logger.debug("Registered filter: '%s'", _name)
