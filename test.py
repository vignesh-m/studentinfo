"""Basic tests."""
from student_info import student_parser, fetch_info
import logging
logging.basicConfig(format="%(asctime)s : %(levelname)s:%(message)s",
                    filename="test.log", level=logging.INFO)

logging.info("testing using test_html")
test_filename = 'test_html'
logging.error("logging not working")
with open(test_filename) as test_file:
    print(student_parser(test_file.read()))
print(fetch_info('cs14b055'))
