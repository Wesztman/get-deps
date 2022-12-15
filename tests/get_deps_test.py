from get_deps import get_deps


def test_get_deps():
    table = get_deps.get_deps("get-deps")
    print(table)
