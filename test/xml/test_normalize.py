from open990.xmlfiles import normalize as N
from open990.xmlfiles.util import consolidate_text
from lxml import etree
from mockito import mock

def test_attribs_to_elements(when):
    original = mock()

    transformed = "transformed"
    when(N)._transform(original).thenReturn(transformed)

    stripped = "stripped"
    when(N)._strip_whitespace(transformed).thenReturn(stripped)

    expected = mock()
    when(etree).fromstring(stripped).thenReturn(expected)

    actual = N._attribs_to_elements(original)
    assert expected == actual

def test_strip_namespace(when):
    to_strip = '<Return xmlns="http://www.irs.gov/efile" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.irs.gov/efile" returnVersion="2009v1.0">'
    expected = '<Return returnVersion="2009v1.0">'

    actual = N._strip_namespace(to_strip)

    # Don't care if there's extra whitespace
    actual_standardized = " ".join(actual.split())
    assert expected == actual_standardized

def test_strip_whitespace():
    raw = """
    <inner>
        <outer />
    </inner>
    """

    # Removes any whitespace between tags
    expected = "<inner><outer /></inner>"
    actual = N._strip_whitespace(raw)
    assert expected == actual

def test_normalize(when):
    raw = "the original XML"

    no_namespace = "the namespace has been removed"
    when(N)._strip_namespace(raw).thenReturn(no_namespace)

    stripped = "interstitial whitespace has been stripped"
    when(N)._strip_whitespace(no_namespace).thenReturn(stripped)

    dom = mock()
    when(N)._as_xml(stripped).thenReturn(dom)

    expected = "string containing normalized XML"
    when(N)._attribs_to_elements(dom).thenReturn(expected)

    actual = N.normalize(raw)
    assert expected == actual

####################
# Functional tests #
####################

def test_normalize_f():
    raw = """
    <element attribute="value" />
    """

    """
    Turns out XML tree comparison is really hard. But this is what we expect:
    
    <element>
        <attribute>value</attribute>
    </element>
    """

    # Verify manually
    actual = N.normalize(raw)
    assert actual is not None
    assert etree._Element == actual.__class__
    assert {}            == actual.attrib
    assert "element"     == actual.tag
    assert {"attribute"} == set([c.tag for c in actual])
    assert "value"       == actual[0].text

def test_normalize_f_recursive():
    raw = """
    <outer>
        <inner attribute="value">
            <innermost />
        </inner>
    </outer>
    """

    """
    Expected:
    
    <outer>
        <inner>
            <innermost />
            <attribute>value</attribute>
        </inner>
    </outer>
    """

    # Verify manually
    actual = N.normalize(raw)
    assert actual is not None
    assert actual.text is None
    assert etree._Element == actual.__class__
    assert {}             == actual.attrib
    assert "outer"        == actual.tag
    assert {"inner"}      == set([c.tag for c in actual])

    inner = actual[0]
    assert "inner" == inner.tag
    assert inner.text is None

    children = {}
    for c in inner:
        children[c.tag] = c.text

    assert children["innermost"] is None
    assert "value" == children["attribute"]

def test_normalize_f_text():
    raw = """
    <e attribute="value">text</e>
    """

    """
    Expected:
    
    <e>
     <attribute>value</attribute>
     text
    </e>
    """

    actual = N.normalize(raw)
    assert actual is not None
    assert "e"           == actual.tag
    assert "text"        == consolidate_text(actual)
    assert {}            == actual.attrib
    assert {"attribute"} == set([c.tag for c in actual])
    assert "value"       ==actual[0].text

def test_normalize_f_namespace():
    raw = """
    <outer xmlns="horrible">
        <inner />
    </outer>
    """

    """
    Expected:
    
    <outer>
        <inner />
    </outer>
    """

    actual = N.normalize(raw)
    assert actual is not None
    assert actual.text is None

    assert "outer"   == actual.tag
    assert {}        == actual.attrib
    assert {"inner"} == set([c.tag for c in actual])
