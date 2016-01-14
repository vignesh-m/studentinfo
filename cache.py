""" Cache class to store, extract student data in local file.
    Uses JSON to encode list of students.
"""
import json


class Cache(object):
    def __init__(self, cdir='~/tmp/studentinfo.json'):
        self.dir = cdir
        self.extract()

    def extract(self):
        with open('~/tmp/studentinfo.json') as cfile:
            self.students = json.loads(cfile.read())

    def store(self, student=None):
        if student:
            self.students.append(student)
        with open('~/tmp/studentinfo.json') as cfile:
            cfile.write(json.dumps(self.students))
