"""Basic tests."""
from student_info import student_parser, fetch_info
from gui import start_gui
import logging
from cache import Cache
logging.basicConfig(format="%(asctime)s : %(levelname)s:%(message)s",
                    filename="test.log", level=logging.INFO)

# logging.info("testing using test_html")
# test_filename = 'test_html'
# with open(test_filename) as test_file:
#     print(student_parser(test_file.read()))
# print(fetch_info('cs14b055'))
cache = Cache()
start_gui(cache)
