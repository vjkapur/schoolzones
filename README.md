# School zone calculations
Attempting to calculate the comprehensive set of roadway/ROW considered part of a "school zone" in DC

## School zone definition
There is a before and after created by the pending [Safe Routes to School legislation](https://lims.dccouncil.us/Legislation/B24-0565) currently under consideration by the DC Council.

### before SRS
This seems a little nebulous. From the [Chapter 31 of the DC Code](https://code.dccouncil.us/us/dc/council/code/titles/38/chapters/31/), the only clear indication appears to be this:

> every street within 100 yards of any school building within a school zone.

This would imply building walls are the operant boundary for determining schoolzones, which would be unhelpful for schools with any setback. It's also unclear if there is some discretization of "street"; if part of a street is within 100 yards of a school building, is the street covered for the entirety of that block? Would welcome any clarification on how DDOT is considering this.

### pending SRS
As written, the current SRS text seems clearer:

> “School zone” means the 150 yards immediately surrounding a school facility, starting from the edge of its grounds.

This expands the boundary from 100 yards to 150 yards, and appears to expand it from building boundaries to ground boundaries.

There was [no official map](https://twitter.com/Janeese4DC/status/1471487059273687046) created around the time the legislation was unveiled.

## Available data sets
[OpenDataDC](https://opendata.dc.gov/) has two useful datasets:
- **[Public School Grounds](https://opendata.dc.gov/datasets/DCGIS::public-school-grounds):** Nominally contains polygons for school grounds, though it's unclear what this covers. Local to my SMD, the Langdon Elementary grounds appear incomplete, missing some recreation space located on an adjacent DC-owned plot. The Woodridge Elementary building (occupied currently by Friendship Charter Schools) appears to be missing entirely. Using this for school grounds for now.
- **[Street Right of Way Polygons](https://opendata.dc.gov/datasets/DCGIS::street-right-of-way-polygons/about):** Polygons for all of DC's street and public ROW segments.

## Goals
Ideally, the two datasets above could be used to generate:
- **school zone polygons:** A set of polygons covering school zones corresponding to the public school grounds.
- **school zone roadway:** A set of polygons corresponding to roadway within a school zone
- **remainder segments:** A set of polygons corresponding to the remainder of discretized roadway segments covered by a school zone

## Methodology
Going to read these datasets into geopandas dataframes and see where it goes. Might render as a webpage using Leaflet if it gets anywhere.