import pytest

import data
import config

from jsonschema import validate, FormatChecker

from client.client import HackerNewsAPIClient


class Schema:
    def __init__(self):
        self.schema = data.DataJsonReader("schema.json")

    def validate(self, instance, schema_name):
        schema = self.schema.get(schema_name)
        if not schema:
            raise Exception(f"Schema: {schema_name} not found")
        validate(
                instance=instance,
                schema=self.schema.get(schema_name),
                format_checker=FormatChecker()
        )


@pytest.fixture(scope="module")
def api():
    hn_api = HackerNewsAPIClient(
        host=config.staging["host"],
        port=config.staging["port"],
    )
    return hn_api


@pytest.fixture(scope="module")
def schema():
    return Schema()
