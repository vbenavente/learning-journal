def includeme(config):
    """ This function adds routes to Pyramid's Configurator. """
    config.add_route('home', '/')
    config.add_route('detail', '/{id:\d+}')
    config.add_route('update', '/edit/{id:\d+}')
    config.add_route('create', '/create')
