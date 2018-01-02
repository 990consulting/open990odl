import io
from typing import List, Tuple
from lxml import etree

# noinspection PyProtectedMember
from lxml.etree import _Element

def flatten(xml_str: str) -> List[Tuple]:
    raw_bytes = io.BytesIO(bytes(xml_str, "ascii"))
    pairs = []
    xpath_root = ""
    for event, element in etree.iterparse(raw_bytes, events=("start", "end")):
        if event == "start":
            xpath_root += "/%s" % element.tag
        else:
            if element.text is not None:
                pair = (xpath_root, element.text)
                pairs.append(pair)
            n = len(element.tag) + 1
            xpath_root = xpath_root[:-n]
    return pairs
