# geospatial-data-catalogs

[![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/opengeos/geospatial-data-catalogs/blob/master/examples.ipynb)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/opengeos/geospatial-data-catalogs/HEAD?labpath=examples.ipynb)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Introduction

Some of the popular cloud-computing platforms (e.g., [AWS](https://aws.amazon.com/earth/), [Google Earth Engine](https://earthengine.google.com/), [Microsoft Planetary Computer](https://planetarycomputer.microsoft.com/), NASA's Common Metadata Repository ([CMR](https://wiki.earthdata.nasa.gov/display/ED/CMR+SpatioTemporal+Asset+Catalog+%28CMR-STAC%29+Documentation))) host a lot of publicly available geospatial datasets. This repo compiles the list of all geospatial datasets on these platforms as a CSV file and as a JSON file, making it easier to find and use them programmatically. The list is updated daily.

## Usage

This repo provides the list of geospatial datasets in two formats:

### Tab separated values (TSV) format

- AWS Open Data: [aws_open_datasets.tsv](https://github.com/opengeos/geospatial-data-catalogs/blob/master/aws_open_datasets.tsv)
- AWS Open Geospatial Data: [aws_geo_datasets.tsv](https://github.com/opengeos/geospatial-data-catalogs/blob/master/aws_geo_datasets.tsv)
- AWS Open Geospatial Data with STAC endpoint: [aws_stac_catalogs.tsv](https://github.com/opengeos/geospatial-data-catalogs/blob/master/aws_stac_catalogs.tsv)
- STAC Index Catalogs: [stac_catalogs.tsv](https://github.com/opengeos/geospatial-data-catalogs/blob/master/stac_catalogs.tsv)
- Earth Engine Catalog: [gee_catalog.tsv](https://github.com/opengeos/geospatial-data-catalogs/blob/master/gee_catalog.tsv)
- Planetary Computer Catalog: [pc_catalog.tsv](https://github.com/opengeos/geospatial-data-catalogs/blob/master/pc_catalog.tsv)
- NASA CMR STAC Catalog: [nasa_cmr_catalog.tsv](https://github.com/opengeos/NASA-CMR-STAC/blob/master/nasa_cmr_catalog.tsv)

#### Copernicus Services Products
- Copernicus Atmosphere: [copernicus_atmosphere.tsv](https://github.com/opengeos/geospatial-data-catalogs/blob/master/copernicus_atmosphere.tsv)
- Copernicus Climate: [copernicus_climate.tsv](https://github.com/opengeos/geospatial-data-catalogs/blob/master/copernicus_climate.tsv)
- Copernicus Emergency: [copernicus_emergency.tsv](https://github.com/opengeos/geospatial-data-catalogs/blob/master/copernicus_emergency.tsv)
- Copernicus Land: [copernicus_land.tsv](https://github.com/opengeos/geospatial-data-catalogs/blob/master/copernicus_land.tsv)
- Copernicus Marine: [copernicus_marine.tsv](https://github.com/opengeos/geospatial-data-catalogs/blob/master/copernicus_marine.tsv)

### JSON format

- AWS Open Data: [aws_open_datasets.json](https://github.com/opengeos/geospatial-data-catalogs/blob/master/aws_open_datasets.json)
- AWS Open Geospatial Data: [aws_geo_datasets.json](https://github.com/opengeos/geospatial-data-catalogs/blob/master/aws_geo_datasets.json)
- AWS Open Geospatial Data with STAC endpoint: [aws_stac_catalogs.json](https://github.com/opengeos/geospatial-data-catalogs/blob/master/aws_stac_catalogs.json)
- STAC Index Catalogs: [stac_catalogs.json](https://github.com/opengeos/geospatial-data-catalogs/blob/master/stac_catalogs.json)
- Earth Engine Catalog: [gee_catalog.json](https://github.com/opengeos/geospatial-data-catalogs/blob/master/gee_catalog.json)
- Planetary Computer Catalog: [pc_catalog.json](https://github.com/opengeos/geospatial-data-catalogs/blob/master/pc_catalog.json)
- NASA CMR STAC Catalog: [nasa_cmr_catalog.json](https://github.com/opengeos/NASA-CMR-STAC/blob/master/nasa_cmr_catalog.json)

#### Copernicus Services Products
- Copernicus Atmosphere: [copernicus_atmosphere.json](https://github.com/opengeos/geospatial-data-catalogs/blob/master/copernicus_atmosphere.json)
- Copernicus Climate: [copernicus_climate.json](https://github.com/opengeos/geospatial-data-catalogs/blob/master/copernicus_climate.json)
- Copernicus Emergency: [copernicus_emergency.json](https://github.com/opengeos/geospatial-data-catalogs/blob/master/copernicus_emergency.json)
- Copernicus Land: [copernicus_land.json](https://github.com/opengeos/geospatial-data-catalogs/blob/master/copernicus_land.json)
- Copernicus Marine: [copernicus_marine.json](https://github.com/opengeos/geospatial-data-catalogs/blob/master/copernicus_marine.json)

### Examples

The TSV file can be easily read into a Pandas DataFrame using the following code:

```python
import pandas as pd

url = 'https://github.com/opengeos/geospatial-data-catalogs/raw/master/aws_geo_datasets.tsv'
df = pd.read_csv(url, sep='\t')
df.head()
```

## Relevant Projects

- A list of open datasets on AWS: [aws-open-data](https://github.com/opengeos/aws-open-data)
- A list of open geospatial datasets on AWS: [aws-open-data-geo](https://github.com/opengeos/aws-open-data-geo)
- A list of open geospatial datasets on AWS with a STAC endpoint: [aws-open-data-stac](https://github.com/opengeos/aws-open-data-stac)
- A list of STAC endpoints from stacindex.org: [stac-index-catalogs](https://github.com/opengeos/stac-index-catalogs)
- A list of geospatial datasets on Microsoft Planetary Computer: [Planetary-Computer-Catalog](https://github.com/opengeos/Planetary-Computer-Catalog)
- A list of geospatial datasets on Google Earth Engine: [Earth-Engine-Catalog](https://github.com/opengeos/Earth-Engine-Catalog)
- A list of geospatial datasets on NASA's Common Metadata Repository (CMR): [NASA-CMR-STAC](https://github.com/opengeos/NASA-CMR-STAC)
- A list of geospatial data catalogs: [geospatial-data-catalogs](https://github.com/opengeos/geospatial-data-catalogs)
- The Maxar Open Data STAC Catalog: [maxar-open-data](https://github.com/opengeos/maxar-open-data)
- Copernicus Services Products Metadata: [Copernicus-Services-Products-Metadata](https://github.com/do-me/Copernicus-Services-Products-Metadata)
