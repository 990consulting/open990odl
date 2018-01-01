from open990.xmlfiles import util
from pytest import fail, raises

def test_strip_whitespace():
    raw = """
    <inner>
        <outer />
    </inner>
    """

    # Removes any whitespace between tags
    expected = "<inner><outer /></inner>"
    actual = util._strip_whitespace(raw)
    assert expected == actual

def test_strip_namespace():
    to_strip = '<Return xmlns="http://www.irs.gov/efile" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.irs.gov/efile" returnVersion="2009v1.0">'
    expected = '<Return returnVersion="2009v1.0">'

    actual = util._strip_namespace(to_strip)

    # Don't care if there's extra whitespace
    actual_standardized = " ".join(actual.split())
    assert expected == actual_standardized

def test_raise_on_empty_passes():
    ok = """
        <first xmlns="http://www.blah.com">
            <second>
                <a>text</a>
            </second>
        </first>
        """
    util.raise_on_empty(ok)

def test_raise_on_empty_contracted():
    not_ok = """
        <first xmlns="http://www.blah.com">
            <second>
                <a>text</a>
                <b />
            </second>
        </first>
        """
    with raises(AssertionError):
        util.raise_on_empty(not_ok)

def test_raise_on_empty_expanded():
    not_ok = """
        <first xmlns="http://www.blah.com">
            <second>
                <a>text</a>
                <b></b>
            </second>
        </first>
        """
    with raises(AssertionError):
        util.raise_on_empty(not_ok)

def test_raise_on_empty_uses_clean(when):
    raw = "shouldn't run on this"
    cleaned = "<this_is>what we want</this_is>"
    when(util).clean_xml(raw).thenReturn(cleaned)
    util.raise_on_empty(raw)
