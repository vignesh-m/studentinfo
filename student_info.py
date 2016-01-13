"""Module to get student info from roll number, use fetch_info."""
from bs4 import BeautifulSoup as bsoup
import logging
import urllib2
import json


def fetch_info(roll_no):
    """
    Fetch student info given roll no.

    See student_parser for student object format
    Throws URLError when url is unreachable.
    """
    url = 'https://www.iitm.ac.in/students/sinfo/%s' % (roll_no)
    logging.info('opening url %s', url)
    res = urllib2.urlopen(url)
    logging.info('status code for response %s', res.getcode())
    html = res.read()
    return student_parser(html)


def parse_tr_second(tr):
    """Get second td in given tr."""
    tds = tr.find_all("td")
    if len(tds) > 1:
        return tds[1].text
    else:
        raise ValueError("tr doesnt have 2 tds")


def student_parser(html):
    """
    Parse given iitm sinfo html to extract student info.

    Return student object of type {name: "", gender: "M/F", dept: "", datejoin: ""}
    """
    logging.info('fetching student info')
    soup = bsoup(html)
    student = {}
    try:
        main = soup.find(id="block-system-main").table
        trs = main.find_all("tr")
        name = trs[0].text  # TODO clean name?
        student["name"] = name
        try:
            student["gender"] = parse_tr_second(trs[1])
        except ValueError:
            logging.error("", exc_info=True)
        try:
            student["dept"] = parse_tr_second(trs[5])
        except ValueError:
            logging.error("", exc_info=True)
        try:
            student["datejoin"] = parse_tr_second(trs[4])
        except ValueError:
            logging.error("", exc_info=True)
        logging.info("return student %s", json.dumps(student))
        return student
    except:
        raise ValueError("Unable to parse html")
