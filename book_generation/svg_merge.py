# from lxml import etree
import base64,os
try:
    from lxml import etree
    print("running with lxml.etree")
except ImportError:
    print("Failed to import ElementTree from any known place")


def paste_elem(src, elem):
    # xml = '<a xmlns="test"><b xmlnslns="test"/></a>'
    # root = etree.fromstring(xml)
    with open(src) as f:
        tree = etree.parse(f)
    root = tree.getroot()
    element = tree.xpath('image')

    if element:
        # Replaces <gco_CharacterString> text
        for key, value in element[0].attrib.iteritems():
            if value == 'avatar':
                element[0].attrib[key] = os.path.abspath(elem)
        # Save back to the XML file
        etree.ElementTree(root).write('svg_tmp/3.svg', pretty_print=True)
        print('OK')