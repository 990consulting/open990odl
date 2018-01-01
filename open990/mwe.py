import io
from lxml import etree
with open("../tmp/debug/2.xml", "r") as p:
    txt = p.read()
    raw_bytes = io.BytesIO(bytes(txt, "utf-8"))
    xpath = ""
    for event, element in etree.iterparse(raw_bytes, events=("start", "end")):
        if event == "start":
            xpath += "/%s" % element.tag
            is_empty = (element.text is None or element.text.strip() == "") and len(element) == 0
            if is_empty:
                print(element.tag, element.sourceline)
        else:
            n = len(element.tag) + 1
            xpath = xpath[:-n]
