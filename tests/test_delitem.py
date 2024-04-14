from datetime import timedelta

from ttl_dict import TTLDict


def test_delitem():
    d = TTLDict(ttl=timedelta(seconds=1000))
    key = 1
    value = 1
    d[key] = value

    d._delitem(d._dict[key])
    assert d._dict == {}
    assert d._ll_head is None
    assert d._ll_end is None
