from get_py_deps import get_py_deps


def test_field_names():
    table = get_py_deps.get_py_deps("get-deps")
    assert table.field_names == ["Package", "License", "Url"]