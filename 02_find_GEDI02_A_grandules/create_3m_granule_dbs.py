import datetime

import rsgislib.dataaccess.nasa_cmr
import rsgislib.tools.utils

import numpy

file_sizes = dict()

for year in numpy.arange(2019, 2023, 1):
    print(year)
    file_sizes[year] = dict()
    # Q1
    start_date = datetime.datetime(year=year, month=1, day=1)
    end_date = datetime.datetime(year=year, month=3, day=31)
    granules_lst = rsgislib.dataaccess.nasa_cmr.find_all_granules("GEDI02_A", version="002", start_date=start_date, end_date=end_date, page_size=100, max_n_pages=100)
    print("\tQ1 N Granules: {}".format(len(granules_lst)))

    if len(granules_lst) > 0:
        file_sizes[year]["Q1"] = float(rsgislib.dataaccess.nasa_cmr.get_total_file_size(granules_lst))
        dwnld_db_file = f"GEDI02_A_{year}_Q1.json"
        miss_granules = rsgislib.dataaccess.nasa_cmr.create_cmr_dwnld_db(db_json=dwnld_db_file, granule_lst=granules_lst, dwnld_file_mime_type="application/x-hdfeos")
        print("\tQ1 {} Missed Granules: {}\n".format(year, len(miss_granules)))

    # Q2
    start_date = datetime.datetime(year=year, month=4, day=1)
    end_date = datetime.datetime(year=year, month=6, day=30)
    granules_lst = rsgislib.dataaccess.nasa_cmr.find_all_granules("GEDI02_A", version="002", start_date=start_date, end_date=end_date, page_size=100, max_n_pages=100)
    print("\tQ2 N Granules: {}".format(len(granules_lst)))

    if len(granules_lst) > 0:
        file_sizes[year]["Q2"] = float(rsgislib.dataaccess.nasa_cmr.get_total_file_size(granules_lst))
        dwnld_db_file = f"GEDI02_A_{year}_Q2.json"
        miss_granules = rsgislib.dataaccess.nasa_cmr.create_cmr_dwnld_db(db_json=dwnld_db_file, granule_lst=granules_lst, dwnld_file_mime_type="application/x-hdfeos")
        print("\tQ2 {} Missed Granules: {}\n".format(year, len(miss_granules)))

    # Q3
    start_date = datetime.datetime(year=year, month=7, day=1)
    end_date = datetime.datetime(year=year, month=9, day=30)
    granules_lst = rsgislib.dataaccess.nasa_cmr.find_all_granules("GEDI02_A", version="002", start_date=start_date, end_date=end_date, page_size=100, max_n_pages=100)
    print("\tQ3 N Granules: {}".format(len(granules_lst)))

    if len(granules_lst) > 0:
        file_sizes[year]["Q3"] = float(rsgislib.dataaccess.nasa_cmr.get_total_file_size(granules_lst))
        dwnld_db_file = f"GEDI02_A_{year}_Q3.json"
        miss_granules = rsgislib.dataaccess.nasa_cmr.create_cmr_dwnld_db(db_json=dwnld_db_file, granule_lst=granules_lst, dwnld_file_mime_type="application/x-hdfeos")
        print("\tQ3 {} Missed Granules: {}\n".format(year, len(miss_granules)))

    # Q4
    start_date = datetime.datetime(year=year, month=10, day=1)
    end_date = datetime.datetime(year=year, month=12, day=31)
    granules_lst = rsgislib.dataaccess.nasa_cmr.find_all_granules("GEDI02_A", version="002", start_date=start_date, end_date=end_date, page_size=100, max_n_pages=100)
    print("\tQ4 N Granules: {}".format(len(granules_lst)))

    if len(granules_lst) > 0:
        file_sizes[year]["Q4"] = float(rsgislib.dataaccess.nasa_cmr.get_total_file_size(granules_lst))
        dwnld_db_file = f"GEDI02_A_{year}_Q4.json"
        miss_granules = rsgislib.dataaccess.nasa_cmr.create_cmr_dwnld_db(db_json=dwnld_db_file, granule_lst=granules_lst, dwnld_file_mime_type="application/x-hdfeos")
        print("\tQ4 {} Missed Granules: {}\n".format(year, len(miss_granules)))

rsgislib.tools.utils.write_dict_to_json(file_sizes, "GEDI02_A_quarter_file_sizes.json")
