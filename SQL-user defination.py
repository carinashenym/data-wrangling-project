import xml.etree.cElementTree as ET
import pprint
import re


def get_user(element):
    if "uid" in element.attrib:
        return element.attrib["uid"]


def process_map(filename):
    users = set()
    for _, element in ET.iterparse(filename):
        uid = get_user(element)
        if uid != None:
            users.add(uid)

    return users


def test():

    users = process_map('/Users/carinashen/Downloads/hawaii-latest.osm')
    pprint.pprint(users)
    assert len(users) == 6



if __name__ == "__main__":
    test()
