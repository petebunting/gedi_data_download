import argparse
import rsgislib.dataaccess.nasa_cmr

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--indb", type=str, required=True, help="Input database file to download.")
    parser.add_argument("-u", "--user", type=str, required=True, help="Username/Password file.")
    parser.add_argument("-o", "--outdir", type=str, required=True, help="Output directory")
    args = parser.parse_args()

    rsgislib.dataaccess.nasa_cmr.download_granules_use_dwnld_db(args.indb, args.outdir, args.user, use_wget=False)
