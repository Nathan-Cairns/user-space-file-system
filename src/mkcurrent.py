#!/usr/bin/env python


# IMPORTS


import sys
import os


# CONSTANTS #


# Required paths
WORKING_DIR = os.path.join(os.getcwd(), '.versiondir')
VERSIONS_DIR = os.path.join(WORKING_DIR, '.versions')


# FUNCTIONS #


def make_current_version(file_name, version_num):
    new_version_name = '%s.%s' % (file_name, version_num)
    new_version_path = os.path.join(WORKING_DIR, new_version_name)

    if os.path.isfile(new_version_path):
        pass
    else:
        print "Error: there is no version", version_num, 'for file', file_name


# MAIN #


if __name__ == '__main__':
    make_current_version(sys.argv[1], sys.argv[2])
