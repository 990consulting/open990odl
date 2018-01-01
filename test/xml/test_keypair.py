from open990.xmlfiles import keypair
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
    actual = keypair.flatten(cleaned)

    assert actual is not None
    assert actual.__class__ == list

    expected_set = set(expected)
    actual_set = set(actual)
    assert expected_set == actual_set

