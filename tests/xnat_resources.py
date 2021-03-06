#!/usr/bin/python
import setup_test
import argparse
import sys
import os
import glob
import getpass
from neuro_tools.xnat import Xnat, util

def main():
    parser = argparse.ArgumentParser(description='XNAT sender')
    parser.add_argument('-project', help='Project ID', required=True)
    parser.add_argument('-subject', help='Subject ID', required=True)
    parser.add_argument('-input', help='Files to be sent', required=True)
    parser.add_argument('-destination', help='Destination in XNAT', required=True)
    parser.add_argument('-server', help='Server for XNAT connection', required=True)
    parser.add_argument('-username', help='Username for XNAT connection', required=True)
    parser.add_argument('-password', help='Password for XNAT connection', required=True)
    args = parser.parse_args()
    
    # Creating connection and load experiment object
    xnat = Xnat(args.server, args.username, args.password)
    item = xnat.session.projects[args.project].subjects[args.subject].experiments[0]
    
    # Sending each PRESENTATION file
    logsfiles = sorted( glob.glob( '{}/**/{}*.log'.format( args.input, args.subject ) ) ) 
    xnat.import_resource(item, 'PRESENTATION', logsfiles)
    print('PRESENTATION imported.')
    
    # Sending each ECG file
    ecgfiles = sorted( glob.glob( '{}/ECG/{}_*.*'.format( args.input, args.subject ) ) ) 
    xnat.import_resource(item, 'ECG', ecgfiles)
    print('ECG imported.')

# init
if __name__ == '__main__':
    main()
