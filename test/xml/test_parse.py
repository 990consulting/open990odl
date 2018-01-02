from open990.xmlfiles import parse
from open990.xmlfiles import util
from lxml import etree

###################
# Functional test #
###################

def test_flatten_f():
    raw = """
    <first>
        <second>
            <a>1</a>
            <b>2</b>
        </second>
    </first>
    """

    expected = [
        ("/first/second/a", "1"),
        ("/first/second/b", "2")
    ]

    cleaned = util.clean_xml(raw)
    actual = parse.flatten(cleaned)

    assert actual is not None
    assert actual.__class__ == list

    expected_set = set(expected)
    actual_set = set(actual)
    print(expected_set)
    print(actual_set)
    assert expected_set == actual_set

def test_is_blank_passes():
    assert not parse._is_blank("I'm not blank!")

def test_is_blank_none():
    assert parse._is_blank(None)

def test_is_blank_empty():
    assert parse._is_blank("")

def test_is_blank_whitespace():
    assert parse._is_blank("\n\n   ")
