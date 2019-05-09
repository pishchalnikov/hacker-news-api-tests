from client.base_api_object import BaseAPIObject
from client.base_view_object import BaseViewObject


class Item(BaseAPIObject):
    _item_path = "item"

    def get_item(self, item_id, status=200):

        response = self._connector.do_get(
            f"{self._api_prefix}/{self._item_path}/{item_id}.json")
        self._ensure_status(status, response)

        return ItemView(response.json())


class ItemView(BaseViewObject):

    @property
    def id(self):
        return self.get("id")

    @property
    def by(self):
        return self.get("by")

    @property
    def descendants(self):
        return self.get("descendants")

    @property
    def kids(self):
        return self.get("kids")

    @property
    def score(self):
        return self.get("score")

    @property
    def time(self):
        return self.get("time")

    @property
    def title(self):
        return self.get("title")

    @property
    def type(self):
        return self.get("type")

    @property
    def url(self):
        return self.get("url")
