import pandas as pd
import csv
import json

class LogAnalysis:
    # store list of log headers to ease refactoring if log format changes in future
    log_headers = ["timestamp",
                    "response_header_size", 
                    "client_ip", 
                    "response_code", 
                    "response_size", 
                    "request_method", 
                    "url", 
                    "username", 
                    "access_type", 
                    "response_type"]

    def __init__(self, input_path):
        # log entries to be stored in pandas DataFrame for simplified analysis
        self.logs_df = pd.DataFrame()

        self.analysis = {}

        self.log_input(input_path)

    def log_input(self, path):
        # register a new dialect to account for irregular spacing between data fields
        csv.register_dialect('skip_space', delimiter=' ', skipinitialspace=True)

        # read logs into pandas DataFrame
        self.logs_df = pd.read_csv(path,
                                dialect='skip_space',
                                header=None,
                                names=LogAnalysis.log_headers)
    

    # Most frequent (IP) method takes parameter for column name in case method to be used for other columns
    def most_frequent(self, column_name):
        # assumption: if multiple IPs are least frequent, only need to return 1

        # indexes selected column by value count
        most_freq = self.logs_df[column_name].value_counts().idxmax()

        # would refactor dictionary key used to a match/case if method used for other columns
        self.analysis["Most frequent IP"] = most_freq
    

    # Least frequent (IP) method takes parameter for column name in case method to be used for other columns
    def least_frequent(self, column_name):
        # assumption: if multiple IPs are least frequent, only need to return 1

        # indexes selected column by value count
        least_freq = self.logs_df[column_name].value_counts().idxmin()

        # would refactor dictionary key used to a match/case if method used for other columns
        self.analysis["Least frequent IP"] = least_freq
    

    def events_per_second_calculate(self):
        # assumption: events per second calculation = 
        #   (no. of events in log) divided by (last event time of log minus first event time of log)
        event_count = self.logs_df["timestamp"].count()
        start_time = self.logs_df["timestamp"].min()
        end_time = self.logs_df["timestamp"].max()

        self.analysis["Events per second"] = round(event_count / (end_time - start_time), 6)
    
    def total_bytes_calculate(self):
        # assumption: total bytes exchanged = sum of all response sizes plus sum of all response header sizes from log
        response_header_bytes = self.logs_df["response_header_size"].sum()
        response_bytes = self.logs_df["response_size"].sum()

        self.analysis["Total amount of bytes exchanged"] = int(response_header_bytes + response_bytes)

    def analysis_output(self, path):
        # create json object from analysis results
        json_obj = json.dumps(self.analysis, indent=4)
        
        # write txt file
        with open(path, 'w') as output:
            output.write(json_obj)
        print(f'Analysis stored at {path}')