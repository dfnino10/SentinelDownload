import os
import zipfile
from collections import OrderedDict

from sentinelsat import SentinelAPI

import cfg
import glob

api = SentinelAPI(cfg.copernicus["user"], cfg.copernicus["password"], 'https://scihub.copernicus.eu/dhus')
outdir = '/david_nfs/1C_level/'
api.download(S2A_MSIL2A_20200425T151711_N0214_R125_T18NYM_20200425T192736, outdir)
"""
tiles = ['18NVN']
query_kwargs = {
    'platformname': 'Sentinel-2',
    'producttype': 'S2MSI1C',
    'date': ('NOW-30DAYS', 'NOW'),
    'cloudcoverpercentage': (0, 20),
    'limit': 1}

date (tuple of (str or datetime) or str, optional) --
A time interval filter based on the Sensing Start Time of the products. Expects a tuple of (start, end), e.g. (“NOW-1DAY”, “NOW”). The timestamps can be either a Python datetime or a string in one of the following formats:

yyyyMMdd
yyyy-MM-ddThh:mm:ss.SSSZ (ISO-8601)
yyyy-MM-ddThh:mm:ssZ
NOW
NOW-<n>DAY(S) (or HOUR(S), MONTH(S), etc.)
NOW+<n>DAY(S)
yyyy-MM-ddThh:mm:ssZ-<n>DAY(S)
NOW/DAY (or HOUR, MONTH etc.) - rounds the value to the given unit
Alternatively, an already fully formatted string such as “[NOW-1DAY TO NOW]” can be used as well.


products = OrderedDict()
for tile in tiles:
    print(tile)
    kw = query_kwargs.copy()
    kw['tileid'] = tile  # products after 2017-03-31
    pp = api.query(**kw)
    print(pp.values())
    products.update(pp)
api.download_all(products, outdir)
"""
os.chdir(outdir)

for zip_file in glob.glob("*.zip"):
    with zipfile.ZipFile(zip_file) as zip_ref:
        zip_ref.extractall(outdir)
    os.remove(zip_file)
