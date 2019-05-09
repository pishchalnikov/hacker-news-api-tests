from client.base_api_object import BaseAPIObject
from client.base_view_object import BaseViewObject


class User(BaseAPIObject):
    _user_path = "user"

    def get_user_by_id(self, user_id, status=200):

        response = self._connector.do_get(
            f"{self._api_prefix}/{self._user_path}/{user_id}.json")
        self._ensure_status(status, response)

        return UserView(response.json())


class UserView(BaseViewObject):

    @property
    def id(self):
        return self.get("id")

    @property
    def about(self):
        return self.get("about")

    @property
    def created(self):
        return self.get("created")

    @property
    def delay(self):
        return self.get("delay")

    @property
    def karma(self):
        return self.get("karma")
