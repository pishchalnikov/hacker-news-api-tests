from client.exceptions import ViewAPIException


class BaseViewObject(dict):

    def __init__(self, data, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not isinstance(data, dict):
            raise ViewAPIException(
                f"JSON Data was {type(data)}, but must be {dict}"
            )
        self.update(data)
