from client.connector import Connector
from client.item import Item
from client.user import User


class HackerNewsAPIClient:

    def __init__(self, host, port):
        self._connector = Connector(host=host, port=port)
        self._api_prefix = "v0"

    @property
    def item(self):
        return Item(self._connector, self._api_prefix)

    @property
    def user(self):
        return User(self._connector, self._api_prefix)
