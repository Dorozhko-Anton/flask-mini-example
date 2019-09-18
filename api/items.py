from flask_injector import inject
from services.provider import ItemsProvider

@inject
def search(dataprovider: ItemsProvider) -> list:
    return dataprovider.get()