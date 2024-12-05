import re
from collections import defaultdict
from visualize import visualize_requests_per_endpoint, visualize_success_failure, visualize_success_rate
from export_data import export_requests_per_endpoint, export_success_failure, export_success_rate

import csv  # Importing CSV module

# Function to read the log file
def read_log_file(file_name):
    with open(file_name, 'r') as file:
        return file.readlines()

# Function to parse the log entries and extract details
def parse_logs(logs):
    log_data = []
    
    # Regular expression pattern to match log entries
    log_pattern = r'(?P<ip>\d+\.\d+\.\d+\.\d+).*\] "(?P<method>\w+) (?P<endpoint>\S+) HTTP/\d\.\d" (?P<status>\d+)'
    
    # Loop through each line in the logs
    for line in logs:
        match = re.search(log_pattern, line)
        if match:
            log_data.append({
                'ip': match.group('ip'),
                'endpoint': match.group('endpoint'),
                'status': int(match.group('status'))
            })
    return log_data

# Function to count requests per endpoint
def count_requests_per_endpoint(log_data):
    endpoint_count = defaultdict(int)
    for log in log_data:
        endpoint_count[log['endpoint']] += 1
    return endpoint_count

# Function to count successful and failed requests
def count_success_failed_requests(log_data):
    success_count = 0
    failed_count = 0
    for log in log_data:
        if log['status'] == 200:
            success_count += 1
        else:
            failed_count += 1
    return success_count, failed_count

# Function to generate and export log metrics
def generate_metrics(log_data):
    # Get counts per endpoint
    endpoint_count = count_requests_per_endpoint(log_data)
    
    # Get success and failure counts
    success_count, failed_count = count_success_failed_requests(log_data)
    
    # Export data
    export_requests_per_endpoint(endpoint_count)
    export_success_failure(success_count, failed_count)
    export_success_rate(success_count, failed_count)
    
    # Displaying the metrics
    total_requests = success_count + failed_count
    success_rate = (success_count / total_requests) * 100 if total_requests > 0 else 0

    print(f"Total Requests: {total_requests}")
    print(f"Successful Requests: {success_count}")
    print(f"Failed Requests: {failed_count}")
    print(f"Success Rate: {success_rate:.2f}%")
    print("\nRequests per Endpoint:")
    
    for endpoint, count in endpoint_count.items():
        print(f"  {endpoint}: {count} requests")

    # Visualize the metrics
    visualize_requests_per_endpoint('endpoint_requests.csv')
    visualize_success_failure('success_failure.csv')
    visualize_success_rate('success_rate.csv')

# Example usage:
logs = read_log_file('sample.log')  # Read the log file
log_data = parse_logs(logs)  # Parse the log data

# Generate and export metrics
generate_metrics(log_data)
