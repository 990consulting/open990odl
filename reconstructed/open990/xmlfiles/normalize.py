from lxml import etree
from lxml.etree import _Element
from open990.xmlfiles.util import clean_xml

def _transform(to_transform: str) -> str:
    xslt_str = """
        <xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
            xmlns:msxsl="urn:schemas-microsoft-com:xslt" exclude-result-prefixes="msxsl">
            <xsl:output method="xml" indent="yes"/>

            <xsl:template match="@* | node()">
                <xsl:copy>
                    <xsl:apply-templates select="@* | node()"/>
                </xsl:copy>
            </xsl:template>

          <xsl:template match="@*">
            <xsl:element name="{name()}"><xsl:value-of select="."/></xsl:element>
          </xsl:template>
        </xsl:stylesheet>
    """

    xslt = etree.fromstring(xslt_str)

    transform = etree.XSLT(xslt)
    transformed = transform(to_transform)
    return transformed

# SO 15830421
def _as_xml(s: str) -> _Element:
    encoded = s.encode("ascii")
    parser = etree.XMLParser(ns_clean=True, recover=True, encoding="ascii")
    return etree.fromstring(encoded, parser=parser)

# SO 10645359
def _attribs_to_elements(original: _Element) -> _Element:
    transformed = _transform(original)
    t_str = str(transformed)
    cleaned = clean_xml(t_str)
    return cleaned

def normalize(raw_xml: str) -> str:
    """
    Remove all namespaces from an XML-formatted string, and convert all
    attributes to child elements.
    :param raw_xml: XML-formatted string to normalize
    :return: string containing normalized XML.
    """
    dom = _as_xml(raw_xml)
    normalized = _attribs_to_elements(dom)
    return normalized
