import os 
import connexion

from connexion.resolver import RestyResolver 
from injector import Binder
from flask_injector import FlaskInjector

from services.provider import ItemsProvider
from services.elastic_factory import ElasticSearchIndex, ElasticSearchFactory
from conf.elasticsearch_mapper import room_mapping

def configure(binder: Binder) -> Binder:
    binder.bind(
        ItemsProvider,
        ItemsProvider([{"Name" : "Test 1"}])
    )

    binder.bind(
        ElasticSearchIndex, 
        ElasticSearchIndex(
            ElasticSearchFactory(
                os.environ['ELASTICSEARCH_HOST'],
                os.environ['ELASTICSEARCH_PORT'],
            ),
            'rooms',
            'room',
            room_mapping
        )
    )
    return binder 

if __name__ == '__main__':
    app = connexion.App('__name__', port=9090, specification_dir='swagger/')
    app.add_api('my_supper_app.yaml', resolver=RestyResolver('api'))

    FlaskInjector(app=app.app, modules=[configure])
    app.run()

