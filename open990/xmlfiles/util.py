import re
from lxml.etree import _Element

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

def _strip_whitespace(raw: str) -> str:
    stripped = re.sub("[\s]+(?![^><]*>)", "", raw)
    return stripped

def _strip_namespace(raw: str) -> str:
    no_ns = re.sub('(xmlns|xsi)(:.*?)?=\".*?\"', "", raw)
    return no_ns

def _strip_encoding(raw: str) -> str:
    no_encoding = re.sub("\<\?xml.+\?\>", "", raw)
    return no_encoding

def _to_ascii(raw: str) -> str:
    return raw.encode("ascii", "ignore").decode("ascii")

def clean_xml(raw: str) -> str:
    """
    Remove interstitial whitespace (whitespace between XML tags) and
    namespaces. The former makes it difficult to detect text-free nodes,
    and the latter makes Xpaths far uglier and more unwieldy.

    :param raw: string containing XML to be cleaned.

    :return: string containing XML with namespaces and interstitial
    whitespace removed.
    """
    a = raw.encode("ascii", "ignore").decode("ascii")
    no_encoding = _strip_encoding(a)
    no_ns = _strip_namespace(no_encoding)
    return no_ns
