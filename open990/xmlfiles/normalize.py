from lxml import etree
from open990.xmlfiles import util

# noinspection PyProtectedMember
from lxml.etree import _Element

# 10645359
# 16698935
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

def _as_xml(s: str) -> _Element:
    return etree.fromstring(s)

# SO 10645359
def _attribs_to_elements(original: _Element) -> _Element:
    transformed = _transform(original)
    t_str = str(transformed)
    cleaned = util.clean_xml(t_str)
    return cleaned


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