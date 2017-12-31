# noinspection PyProtectedMember
from lxml.etree import _Element

# SO 4770191
def consolidate_text(elem: _Element) -> str:
    texts = elem.xpath("text()")
    return "".join(texts)
