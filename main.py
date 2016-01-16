"""Main module."""
from gui import start_gui
import logging
from cache import Cache
import argparse
import os

logging.basicConfig(format="%(asctime)s : %(levelname)s:%(message)s",
                    filename="test.log", level=logging.INFO)

parser = argparse.ArgumentParser()
parser.add_argument("-c", "--cache-dir",
                    help="Choose directory to store cache in")
parser.add_argument("-n", "--no-cache", action="store_true",
                    help="Disable caching of results")
args = parser.parse_args()

if not args.no_cache:
    if args.cache_dir:
        cache = Cache(cfile=os.path.join(args.cache_dir, 'studentinfo.json'))
    else:
        cache = Cache()
else:
    cache = Cache(use_cache=False)
start_gui(cache)
