import pytest


@pytest.mark.parametrize("item_id", [
    1, 2, 3
])
def test_item_id(api, item_id):
    view = api.item.get_item(item_id)

    assert item_id == view.id


@pytest.mark.parametrize("item_id, title", [
    (8863, "My YC app: Dropbox - Throw away your USB drive")
])
def test_item_title(api, item_id, title):
    view = api.item.get_item(item_id)

    assert title == view.title


@pytest.mark.parametrize("item_id, by", [
    (8863, 'dhouston')
])
def test_item_by(api, item_id, by):
    view = api.item.get_item(item_id)

    assert by == view.by


@pytest.mark.parametrize("item_id, descendants", [
    (8863, 71)
])
def test_item_descendants(api, item_id, descendants):
    view = api.item.get_item(item_id)

    assert descendants == view.descendants


@pytest.mark.parametrize("item_id, url", [
    (8863, "http://www.getdropbox.com/u/2/screencast.html")
])
def test_item_url(api, item_id, url):
    view = api.item.get_item(item_id)

    assert url == view.url


@pytest.mark.parametrize("item_id, schema_name", [
    (8863, "item_view_schema")
])
def test_item_schema(api, schema, item_id, schema_name):
    view = api.item.get_item(item_id)

    schema.validate(view, schema_name)
