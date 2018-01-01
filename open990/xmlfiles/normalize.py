from lxml import etree
# noinspection PyProtectedMember
from open990.definitions import ROOT_DIR
from open990.xmlfiles import util
from lxml.etree import _Element

from xmlfiles.util import _strip_whitespace, _strip_namespace


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
    return stripped


# SO 25771405

def normalize(raw_xml: str) -> str:
    """
    Remove all namespaces from an XML-formatted string, and convert all
    attributes to child elements.
    :param raw_xml: XML-formatted string to normalize
    :return: string containing normalized XML.
    """
    cleaned = util.clean_xml(raw_xml)
    dom = _as_xml(cleaned)
    normalized = _attribs_to_elements(dom)
    return normalized