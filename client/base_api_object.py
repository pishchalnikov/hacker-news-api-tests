from pprint import pformat


class BaseAPIObject:

    def __init__(self, connector, api_prefix):
        self._connector = connector
        self._api_prefix = api_prefix

    @staticmethod
    def _ensure_status(status_code, response):
        if not status_code == response.status_code:
            try:
                content = response.json()
            except ValueError:
                content = response.text

            msg = "Expected status code: {0}\n" \
                  "Got status code: {1}\n" \
                  "With content:\n{2}" \
                .format(status_code,
                        response.status_code,
                        pformat(content))

            raise AssertionError(msg)
