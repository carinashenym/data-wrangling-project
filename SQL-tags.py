###use the iterative parsing to process the map file and
find out not only what tags are there, but also how many, to get the
feeling on how much of which data you can expect to have in the map.###

import xml.etree.cElementTree as ET
import pprint
from collections import defaultdict

def count_tags(filename):
    tags = defaultdict(int)
    for event, element in ET.iterparse(filename):
        tags[element.tag] += 1
    return tags

def test():
    tags = count_tags('/Users/carinashen/Downloads/hawaii-latest.osm')
    pprint.pprint(tags)
    assert tags == {'bounds': 1,
                     'member': 3,
                     'nd': 4,
                     'node': 20,
                     'osm': 1,
                     'relation': 1,
                     'tag': 7,
                     'way': 1}



if __name__ == "__main__":
    test()


##  File "/Users/carinashen/PycharmProjects/untitled1/test.py", line 26, in <module>
    test()
            {'bounds': 1,
             'member': 10170,
             'nd': 1455745,
             'node': 1269393,
             'osm': 1,
             'relation': 1682,
  File "/Users/carinashen/PycharmProjects/untitled1/test.py", line 21, in test
    'way': 1}
             'tag': 350113,
             'way': 97806})###
