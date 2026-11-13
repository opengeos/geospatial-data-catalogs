import sys

from leafmap import download_file

links = [
    "https://github.com/giswqs/aws-open-data/raw/master/aws_open_datasets.tsv",
    "https://github.com/giswqs/aws-open-data/raw/master/aws_open_datasets.json",
    "https://github.com/giswqs/aws-open-data-geo/raw/master/aws_geo_datasets.tsv",
    "https://github.com/giswqs/aws-open-data-geo/raw/master/aws_geo_datasets.json",
    "https://github.com/giswqs/aws-open-data-stac/raw/master/aws_stac_catalogs.tsv",
    "https://github.com/giswqs/aws-open-data-stac/raw/master/aws_stac_catalogs.json",
    "https://github.com/giswqs/stac-index-catalogs/raw/master/stac_catalogs.tsv",
    "https://github.com/giswqs/stac-index-catalogs/raw/master/stac_catalogs.json",
    "https://github.com/giswqs/Earth-Engine-Catalog/raw/master/gee_catalog.tsv",
    "https://github.com/giswqs/Earth-Engine-Catalog/raw/master/gee_catalog.json",
    "https://github.com/giswqs/Planetary-Computer-Catalog/raw/master/pc_catalog.tsv",
    "https://github.com/giswqs/Planetary-Computer-Catalog/raw/master/pc_catalog.json",
    "https://github.com/giswqs/NASA-CMR-STAC/raw/master/nasa_cmr_catalog.tsv",
    "https://github.com/giswqs/NASA-CMR-STAC/raw/master/nasa_cmr_catalog.json",
    # Copernicus Metadata
    "https://github.com/do-me/Copernicus-Services-Products-Metadata/raw/main/outputs/tsv/copernicus_atmosphere.tsv",
    "https://github.com/do-me/Copernicus-Services-Products-Metadata/raw/main/outputs/json/copernicus_atmosphere.json",
    "https://github.com/do-me/Copernicus-Services-Products-Metadata/raw/main/outputs/tsv/copernicus_climate.tsv",
    "https://github.com/do-me/Copernicus-Services-Products-Metadata/raw/main/outputs/json/copernicus_climate.json",
    "https://github.com/do-me/Copernicus-Services-Products-Metadata/raw/main/outputs/tsv/copernicus_emergency.tsv",
    "https://github.com/do-me/Copernicus-Services-Products-Metadata/raw/main/outputs/json/copernicus_emergency.json",
    "https://github.com/do-me/Copernicus-Services-Products-Metadata/raw/main/outputs/tsv/copernicus_land.tsv",
    "https://github.com/do-me/Copernicus-Services-Products-Metadata/raw/main/outputs/json/copernicus_land.json",
    "https://github.com/do-me/Copernicus-Services-Products-Metadata/raw/main/outputs/tsv/copernicus_marine.tsv",
    "https://github.com/do-me/Copernicus-Services-Products-Metadata/raw/main/outputs/json/copernicus_marine.json",
]



def main():
    """Download every catalog file, continuing past individual failures.

    Returns:
        int: Process exit code, 0 if all downloads succeeded, otherwise 1.
    """
    failed = []
    for link in links:
        try:
            download_file(link, overwrite=True)
        except Exception as e:  # noqa: BLE001
            print(f"Failed to download {link}: {e}", file=sys.stderr)
            failed.append(link)

    if failed:
        print(f"{len(failed)} of {len(links)} downloads failed:", file=sys.stderr)
        for link in failed:
            print(f"  {link}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
