"""Main module."""
from gui import start_gui
import logging
from cache import Cache

logging.basicConfig(format="%(asctime)s : %(levelname)s:%(message)s",
                    filename="test.log", level=logging.INFO)

cache = Cache()
start_gui(cache)
