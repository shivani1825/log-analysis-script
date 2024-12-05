import os
from log_analysis import analyze_log_file, save_endpoint_requests_to_csv, save_success_failure_to_csv, save_success_rate_to_csv
from visualize import plot_requests_per_endpoint, plot_success_vs_failure, plot_success_rate

def main():
    # Step 1: Log file path
    log_file_path = 'path_to_your_log_file.log'  # Update this path

    # Step 2: Analyze the log file
    endpoint_requests, success_count, failure_count, total_requests, success_rate = analyze_log_file(log_file_path)

    # Step 3: Save results to CSV files
    save_endpoint_requests_to_csv(endpoint_requests)
    save_success_failure_to_csv(success_count, failure_count)
    save_success_rate_to_csv(total_requests, success_count, failure_count, success_rate)

    print("Data has been saved to CSV files.")

    # Step 4: Generate visualizations
    plot_requests_per_endpoint('endpoint_requests.csv')
    plot_success_vs_failure('success_failure.csv')
    plot_success_rate('success_rate.csv')

    print("Visualizations have been generated and saved as images.")

if __name__ == '__main__':
    main()
