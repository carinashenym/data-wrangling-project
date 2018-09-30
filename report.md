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
### how many schools here in east hawaii
```
Select count(*)
from planet_osm_polygon
Where amenity = 'school'
```
output
```
4
```
### number of ways
```
Select count(*)
from planet_osm_ways
```
output
```
4906
```

### who is the contributer of the map
```
SELECT count(*) as editer, auth_name
FROM spatial_ref_sys
group by auth_name
ORDER BY editer DESC
LIMIT 10
```
output
```
5756;"EPSG"
1;"spatialreferencing.org"
```
