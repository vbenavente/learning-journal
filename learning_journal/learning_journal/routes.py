def includeme(config):
    """ This function adds routes to Pyramid's Configurator """
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('update', '/{id:\d+}/edit')
    config.add_route('detail', '/{id:\d+}')
    config.add_route('create', '/create')
