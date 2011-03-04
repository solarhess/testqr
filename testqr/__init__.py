from pyramid.config import Configurator
from sqlalchemy import engine_from_config

from testqr.models import initialize_sql

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    engine = engine_from_config(settings, 'sqlalchemy.')
    initialize_sql(engine)
    config = Configurator(settings=settings)
    config.add_static_view('static', 'testqr:static')
    config.add_route('home', '/', 
                     view='testqr.views.home',
                     view_renderer='home.mako')
    config.add_route('view_card', '/cards/{id}', 
              view='testqr.views.view_card',
              view_renderer='card_details.mako')

    return config.make_wsgi_app()


