import re
import io

# noinspection PyProtectedMember
from lxml.etree import _Element
from lxml import etree

# SO 4770191
def consolidate_text(elem: _Element) -> str:
    """
    Concatenate text sandwiched between child elements, a situation that can
    be created by normalization.
    :param elem: etree element whose text is to be collected.
    :return: the collected text from the etree element.
    """
    texts = elem.xpath("text()")
    return "".join(texts)

def raise_on_empty(raw: str) -> None:
    """
    Assert that every element in an XML hierarchy is non-empty; that is,
    it contains either text or at least one child element. To the best of my
    knowledge, the 990 schemas always meet this constraint; however, if they
    should fail to do so, it would cause some of this code to break silently,
    so we want to detect it.

     :param raw: string containing raw XML
     :return: None
    """
    stripped = clean_xml(raw)
    raw_bytes = io.BytesIO(bytes(stripped, "ascii"))

    for event, element in etree.iterparse(raw_bytes, events=("start",)):
        assert_not_empty(element)

def assert_not_empty(elem: _Element) -> None:
    is_empty = elem.text is None and len(elem) == 0
    assert not is_empty

def _strip_whitespace(raw: str) -> str:
    stripped = re.sub("[\s]+(?![^><]*>)", "", raw)
    return stripped

def _strip_namespace(raw: str) -> str:
    no_ns = re.sub('(xmlns|xsi)(:.*?)?=\".*?\"', "", raw)
    return no_ns

def clean_xml(raw: str) -> str:
    """
    Remove interstitial whitespace (whitespace between XML tags) and
    namespaces. The former makes it difficult to detect text-free nodes,
    and the latter makes Xpaths far uglier and more unwieldy.

    :param raw: string containing XML to be cleaned.

    :return: string containing XML with namespaces and interstitial
    whitespace removed.
    """
    no_ns = _strip_namespace(raw)
    stripped = _strip_whitespace(no_ns)
    return stripped
