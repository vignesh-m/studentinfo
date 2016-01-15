""" Cache class to store, extract student data in local file.
    Uses pickle to encode list of students.
"""
import pickle
import student_info
import os
import logging


class Cache(object):
    def __init__(self, cfile='./tmp/studentinfo.dat', use_cache=True):
        self.cfile = cfile
        self.use_cache = use_cache
        self.extract()

    def extract(self):
        if not self.use_cache:
            pass
        try:
            cfile = open(self.cfile, 'rb')
            self.students = pickle.load(cfile)
        except (FileNotFoundError, IOError):
            os.makedirs(os.path.dirname(self.cfile), exist_ok=True)
            cfile = open(self.cfile, 'wb')
            self.students = {}
            self.store()

    def store(self, student=None):
        if not self.use_cache:
            pass
        if student:
            self.students[student['rollno']] = student
        with open(self.cfile, 'wb') as cfile:
            pickle.dump(self.students, cfile)

    def fetch_info(self, roll_no):
        roll_no = roll_no.upper()
        if self.use_cache and roll_no in self.students:
            logging.info('serving %s from cache' % roll_no)
            return self.students[roll_no]
        else:
            logging.info('serving %s from url' % roll_no)
            student = student_info.fetch_info(roll_no)
            self.store(student)
            return student
