import io
from typing import List, Tuple
from lxml import etree
from open990.xmlfiles import util

# noinspection PyProtectedMember
from lxml.etree import _Element

def flatten(xml_str: str) -> List[Tuple]:
    """
    Transforms XML into a list of key-value pairs, with the keys consisting
    of normalized Xpaths and the values consisting of the text from each
    Xpath. The etree is assumed to be normalized (all attributes turned into
    elements) and cleaned (namespaces and interstitial whitespace stripped).

    :param xml_str: String representing cleaned, normalized XML
    :return: List of Xpath-value pairs
    """
    raw_bytes = io.BytesIO(bytes(xml_str, "ascii"))
    pairs = []
    xpath_root = ""
    for event, element in etree.iterparse(raw_bytes, events=("start", "end")):
        if event == "start":
            xpath_root += "/%s" % element.tag
            util.assert_not_empty(element)
            if element.text is not None:
                pair = (xpath_root, element.text)
                pairs.append(pair)
        else:
            n = len(element.tag) + 1
            xpath_root = xpath_root[:-n]
    return pairs