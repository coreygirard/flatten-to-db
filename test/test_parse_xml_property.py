from hypothesis import given, assume

from src import parse, unparse
from test.strategy_xml import xml_strategy


@given(xml_strategy())
def test_reversible(data):
    s, _ = data
    once = parse.xml(s)
    thrice = parse.xml(unparse.xml(parse.xml(s)))
    assert once == thrice
