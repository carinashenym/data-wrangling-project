import xml.etree.cElementTree as ET
from collections import defaultdict
import re
import pprint

OSMFILE = "/Users/carinashen/Documents/Projects/data-wrangling-project/east-hawaii-map.osm"
street_type_re = re.compile(r'\b\S+\.?$', re.IGNORECASE)
osm_file = open(OSMFILE, "r")
street_types = defaultdict(set)

expected = ["Street", "Avenue", "Boulevard", "Drive", "Court", "Place", "Square", "Lane", "Road",
            "Trail", "Parkway"]


mapping = { "St": "Street",
            "Blvd": "Boulevardt",
            "Rd":"Road",
            "Dr":"Drive",
            "Hwy":"Highway"
            }


def audit_street_type(street_types, street_name):
    m = street_type_re.search(street_name)
    if m:
        street_type = m.group()
        if street_type not in expected:
            street_types[street_type].add(street_name)


def is_street_name(elem):
    return (elem.attrib['k'] == "addr:street")


def audit(osmfile):

    for event, elem in ET.iterparse(osm_file, events=("start",)):

        if elem.tag == "way":
            for tag in elem.iter("tag"):
                if is_street_name(tag):
                    audit_street_type(street_types, tag.attrib['v'])
    osm_file.close()
    return street_types


def update_name(name, mapping):
    m = street_type_re.search(name)
    if m:
        street_type = m.group()
        if street_type not in expected:
            if street_type in mapping.keys():
                name = re.sub(street_type_re, mapping[street_type], name)

    return name


def test():
    st_types = audit(OSMFILE)
    pprint.pprint(dict(st_types))
    assert len(st_types) == 4


    for st_type, ways in st_types.iteritems():
        for name in ways:
            better_name = update_name(name, mapping)
            print (name, "=>", better_name)
            if name == "Kahakai Blvd":
                assert better_name == "Kuahakai Boulevardt"
            if name == "Orchid Land Dr":
                assert better_name == "Orchid Land Drive"
            if name == "Old Volcano Hwy":
                assert better_name == "Old Volcano Highway"

if __name__ == '__main__':
    test()
