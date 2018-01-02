import io
from typing import List, Tuple
from lxml import etree

# noinspection PyProtectedMember
from lxml.etree import _Element

def _is_blank(text: str) -> bool:
    if text is None:
        return True
    if text.strip() == "":
        return True
    return False

def flatten(xml_str: str) -> List[Tuple]:
    raw_bytes = io.BytesIO(bytes(xml_str, "ascii"))
    pairs = []
    xpath_root = ""
    for event, element in etree.iterparse(raw_bytes, events=("start", "end")):
        if event == "start":
            xpath_root += "/%s" % element.tag
        else:
            if not _is_blank(element.text):
                pair = (xpath_root, element.text.strip())
                pairs.append(pair)
            n = len(element.tag) + 1
            xpath_root = xpath_root[:-n]
    return pairs
