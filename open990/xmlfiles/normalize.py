from lxml import etree
import re
# noinspection PyProtectedMember
from open990.definitions import ROOT_DIR

from lxml.etree import _Element

def _transform(to_transform: str) -> str:
    path = ROOT_DIR + "/../data/attrib2elem.xsl"
    xslt = etree.parse(path)

    transform = etree.XSLT(xslt)
    transformed = transform(to_transform)
    return transformed

def _as_xml(s: str) -> _Element:
    return etree.fromstring(s)

# SO 10645359
def _attribs_to_elements(original: _Element) -> _Element:
    transformed = _transform(original)
    t_str = str(transformed)
    stripped = _strip_whitespace(t_str)
    tree = etree.fromstring(stripped)
    return tree

def _strip_namespace(raw: str) -> str:
    no_ns = re.sub('(xmlns|xsi)(:.*?)?=\".*?\"', "", raw)
    return no_ns


# SO 25771405
def _strip_whitespace(raw: str) -> str:
    stripped = re.sub("[\s]+(?![^><]*>)", "", raw)
    return stripped

def normalize(raw_xml: str) -> str:
    """
    Remove all namespaces from an XML-formatted string, and convert all
    attributes to child elements.
    :param raw_xml: XML-formatted string to normalize
    :return: string containing normalized XML.
    """
    no_namespace = _strip_namespace(raw_xml)
    stripped = _strip_whitespace(no_namespace)
    dom = _as_xml(stripped)
    normalized = _attribs_to_elements(dom)
    return normalized