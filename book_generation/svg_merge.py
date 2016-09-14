from lxml import etree
import base64


def paste_elem(src, elem):
    # xml = '<a xmlns="test"><b xmlnslns="test"/></a>'
    # root = etree.fromstring(xml)
    with open(src) as f:
        tree = etree.parse(f)
    with open(elem, "rb") as image_file:
        encoded_string = str(base64.b64encode(image_file.read()))
    root = tree.getroot()
    element = root.xpath('//image')

    if element:
        # Replaces <gco_CharacterString> text
        for key, value in element[0].attrib.iteritems():
            if value == 'avatar':
                element[0].attrib[key] = 'data:image/png;base64,{}'.format(encoded_string[2:-1])
        # Save back to the XML file
        etree.ElementTree(root).write('svg_tmp/2.svg', pretty_print=True)
    print(tree.getroot())
    print(etree.tostring(root))