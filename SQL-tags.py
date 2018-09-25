###use the iterative parsing to process the map file and
##find out not only what tags are there, but also how many, to get the
##feeling on how much of which data you can expect to have in the map.

import xml.etree.cElementTree as ET
import pprint
from collections import defaultdict

def count_tags(filename):
    tags = defaultdict(int)
    for event, element in ET.iterparse(filename):
        tags[element.tag] += 1
    return tags

def test():
    tags = count_tags('/Users/carinashen/Documents/Projects/data-wrangling-project/east-hawaii-map.osm')
    pprint.pprint(tags)
    assert tags == defaultdict(<class 'int'>,
            {'bounds': 1,
             'member': 2380,
             'nd': 43515,
             'node': 36667,
             'osm': 1,
             'relation': 84,
             'tag': 16117,
             'way': 4906})



if __name__ == "__main__":
    test()
