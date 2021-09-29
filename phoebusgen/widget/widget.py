from xml.etree.ElementTree import Element, SubElement, tostring
from xml.dom import minidom
from phoebusgen._shared_property_helpers import _SharedPropertyFunctions

class _Widget(object):
    def __init__(self, w_type, name, x_pos, y_pos, width, height):
        self.root = Element('widget', type=w_type, version='2.0.0')
        name_child = SubElement(self.root, 'name')
        name_child.text = name

        self._shared = _SharedPropertyFunctions(self.root)
        self._shared.integer_property(self.root, 'x', x_pos)
        self._shared.integer_property(self.root, 'y', y_pos)
        self._shared.integer_property(self.root, 'width', width)
        self._shared.integer_property(self.root, 'height', height)

    def visible(self, visible):
        child = SubElement(self.root, 'visible')
        child.text = str(visible)

    def version(self, version):
        self.root.attrib['version'] = version

    def name(self, val):
        self._shared.generic_property(self.root, 'name', val)

    def width(self, val):
        self._shared.integer_property(self.root, 'width', val)

    def height(self, val):
        self._shared.integer_property(self.root, 'height', val)

    def x(self, val):
        self._shared.integer_property(self.root, 'x', val)

    def y(self, val):
        self._shared.integer_property(self.root, 'y', val)

    #def class_name(self, name):
    #    pass

    #def rule(self, rule):
    #    pass

    #def scripts(self, script):
    #    pass

    def tool_tip(self, tool_tip):
        child = SubElement(self.root, 'tooltip')
        child.text = tool_tip

    def find_element(self, tag):
        elements = self.root.findall(tag)
        # check to make sure there are not more than 1 elements
        # we don't want duplicate tags
        if len(elements) > 1:
            print('Warning, more than one element of the same tag! Returning a list')
            return elements
        elif len(elements) == 0:
            return None
        else:
            return elements[0]

    def remove_element(self, tag):
        element = self.find_element(tag)
        if element is not None:
            self.root.remove(element)

    def get_element_value(self, tag):
        return self.find_element(tag).text

    # From: https://pymotw.com/3/xml.etree.ElementTree/create.html
    def _prettify(self, elem):
        """Return a pretty-printed XML string for the Element.
        """
        rough_string = tostring(elem, 'utf-8')
        reparse_xml = minidom.parseString(rough_string)
        return reparse_xml.toprettyxml(indent="  ", newl="\n")

    def __str__(self):
        return self._prettify(self.root)

    def __repr__(self):
        return self._prettify(self.root)


if __name__ == '__main__':
    pass
