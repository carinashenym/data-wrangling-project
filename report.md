## analysis Hawaii from open street map by SQL ##

Additional Data Exploration
---

### how many amenities there in east Hawaii
```
Select count(*)as num, amenity
from planet_osm_polygon
group by amenity
order by num desc
```
output
```
2870;""
21;"parking"
4;"school"
3;"place_of_worship"
2;"restaurant"
2;"fuel"
1;"post_office"
1;"grave_yard"
1;"pharmacy"
1;"toilets"
1;"fast_food"
1;"bank"
1;"police"
```
