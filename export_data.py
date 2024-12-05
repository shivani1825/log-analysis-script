import pandas as pd

# Function to export the requests per endpoint to a CSV file
def export_requests_per_endpoint(endpoint_count, file_name='endpoint_requests.csv'):
    # Convert the dictionary to a pandas DataFrame
    df = pd.DataFrame(list(endpoint_count.items()), columns=['Endpoint', 'Request Count'])
    
    # Export to CSV
    df.to_csv(file_name, index=False)
    print(f"Data exported to {file_name}")

# Function to export success and failure counts to a CSV file
def export_success_failure(success_count, failed_count, file_name='success_failure.csv'):
    # Create a dictionary for success and failure data
    data = {
        'Status': ['Success', 'Failure'],
        'Count': [success_count, failed_count]
    }
    
    # Convert dictionary to DataFrame
    df = pd.DataFrame(data)
    
    # Export to CSV
    df.to_csv(file_name, index=False)
    print(f"Data exported to {file_name}")

# Function to export success rate and total requests to a CSV file
def export_success_rate(success_count, failed_count, file_name='success_rate.csv'):
    total_requests = success_count + failed_count
    success_rate = (success_count / total_requests) * 100 if total_requests > 0 else 0
    
    # Create data dictionary for success rate
    data = {
        'Total Requests': [total_requests],
        'Successful Requests': [success_count],
        'Failed Requests': [failed_count],
        'Success Rate (%)': [success_rate]
    }
    
    # Convert to DataFrame
    df = pd.DataFrame(data)
    
    # Export to CSV
    df.to_csv(file_name, index=False)
    print(f"Data exported to {file_name}")

