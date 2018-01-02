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

def test_strip_encoding():
    to_strip = '<?xml version="xml-1.0" encoding="utf-8" ?>'
    expected = ''
    actual = util._strip_encoding(to_strip)
    assert expected == actual

def test_clean_xml(when):
    raw = "this is the original string"

    no_encoding = """this has had the encoding string removed (the IRS claimed
                  UTF-8 but had lots of extended characters that blew things up
                  """
    when(util)._strip_encoding(raw).thenReturn(no_encoding)

    expected = "namespaces have been removed."
    when(util)._strip_namespace(no_encoding).thenReturn(expected)

    actual = util.clean_xml(raw)
    assert expected == actual
