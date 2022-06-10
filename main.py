import argparse
import logging
import os
import sys
from log_analyzer import LogAnalysis

def main():

    # Use argparse library for argument parsing
    parser = argparse.ArgumentParser(description='Analyze the content of log files')

    parser.add_argument('Input',
                        metavar='input',
                        type=str,
                        help='path to input log file')

    parser.add_argument('Output',
                        metavar='output',
                        type=str,
                        help='path to output save file')

    parser.add_argument('-a',
                        '--all',
                        action='store_true',
                        help='run all operations below')

    parser.add_argument('-m',
                        '--most',
                        action='store_true',
                        help='most frequent IP')

    parser.add_argument('-l',
                        '--least',
                        action='store_true',
                        help='least frequent IP')

    parser.add_argument('-e',
                        '--eps',
                        action='store_true',
                        help='events per second')

    parser.add_argument('-t',
                        '--total',
                        action='store_true',
                        help='total amount of bytes exchanged')

    args = parser.parse_args()

    # argument checks
    if not (args.all or args.most or args.least or args.eps or args.total):
        parser.error('No operation selected, add -h for help')
    
    # verify input path is a file
    if not os.path.isfile(args.Input):
        print('The input path specified does not exist')
        sys.exit()

    # verify txt format for output file
    if args.Output[-4:] != '.txt':
            print('The output file must have .txt format')
            sys.exit()
    

    # begin analysis
    la = LogAnalysis(args.Input)

    # check args to see which analysis should be performed
    if args.most or args.all:
        la.most_frequent("client_ip")
    if args.least or args.all:
        la.least_frequent("client_ip")
    if args.eps or args.all:
        la.events_per_second_calculate()
    if args.total or args.all:
        la.total_bytes_calculate()

    la.analysis_output(args.Output)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logging.exception(e)   