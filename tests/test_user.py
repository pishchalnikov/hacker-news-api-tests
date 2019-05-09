import pytest


@pytest.mark.parametrize("user_id", [
    "test", "qa"
])
def test_user_id(api, user_id):
    view = api.user.get_user_by_id(user_id)

    assert user_id == view.id


@pytest.mark.parametrize("user_id, about", [
    ("jl", "This is a test")
])
def test_user_about(api, user_id, about):
    view = api.user.get_user_by_id(user_id)

    assert about == view.about


@pytest.mark.parametrize("user_id, created", [
    ("jl", 1173923446)
])
def test_user_created(api, user_id, created):
    view = api.user.get_user_by_id(user_id)

    assert created == view.created


@pytest.mark.parametrize("item_id, schema_name", [
    ("test", "user_view_schema")
])
def test_user_schema(api, schema, item_id, schema_name):
    view = api.user.get_user_by_id(item_id)

    schema.validate(view, schema_name)
