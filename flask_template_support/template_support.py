from flask_template_support import DEFAULT_FILTERS, DEFAULT_FUNCTIONS


class TemplateSupport:
    def __init__(self, app=None, **kwargs):
        """

        :param app:
        """
        self._app = app
        if self._app:
            self.init_app(app, **kwargs)

    def init_app(self, app, fltrs=None, functs=None):
        """

        :param functs: function's tuple
        :param fltrs: filter's tuple
        :param app:
        """
        self._app = app

        if not hasattr(app, 'extensions'):
            app.extensions = dict()
        app.extensions['template_support'] = self

        self.register_filters(DEFAULT_FILTERS + (fltrs or ()))
        self.register_functions(DEFAULT_FUNCTIONS + (functs or ()))

    def register_functions(self, functs):
        """

        :param functs: function's tuple
        """
        for f in functs:
            if isinstance(f, tuple):
                self._register_function(f[0], f[1])
            else:
                self._register_function(f)

    def register_filters(self, fltrs):
        """

        :param fltrs: filter's tuple
        """
        for f in fltrs:
            if isinstance(f, tuple):
                self._register_filter(f[0], f[1])
            else:
                self._register_filter(f)

    def _register_function(self, funct, name=None):
        """

        :param funct:
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

        _name = name or funct.__name__

        self._app.template_context_processors[None].append(
            create_callback(_name, funct)
        )
        self._app.logger.debug("Registered function: '{}'".format(_name))

    def _register_filter(self, fltr, name=None):
        """

        :param fltr:
        :param name:
        """
        _name = name or fltr.__name__

        self._app.add_template_filter(fltr, _name)
        self._app.logger.debug("Registered filter: '%s'", _name)
