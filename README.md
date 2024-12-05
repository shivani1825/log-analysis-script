# Log Analysis and Visualization Project:
-----------------------------------------

This project performs log file analysis and generates visualizations of endpoint requests, success vs. failure, and success rate. It processes server log data and provides both CSV output and graphical visualizations. This project is useful for understanding the traffic and behavior in server logs, detecting trends, and visualizing success vs. failure rates.

## Features:
------------

- **Analyzes** server log files for endpoint requests.
- **Tracks** the number of successful and failed requests.
- **Calculates** the success rate of requests.
- **Generates** CSV files for further analysis.
- **Creates** visualizations (bar charts and pie charts) using `matplotlib`.

## Requirements:
----------------

- Python 3.x
- `matplotlib` library

### Install Dependencies:
-------------------------

1. Clone the repository or download the project files.

2. Install the required dependencies by running:

   pip install -r requirements.txt

If matplotlib is not already installed, you can install it manually with:
    
    pip install matplotlib

## How to Run the Script:
----------------------
1.Prepare your log file (e.g., server_log.log) and place it in the project folder.

2.Modify the path of the log file in main.py:

3.log_file_path = 'path_to_your_log_file.log'  # Update with the correct path

## Run the main.py script:
-------------------------

python main.py

This will process the log file, generate the required CSV files, and display the visualizations.

## Expected Output:
-------------------

Upon running the script, you will get:

CSV Files:
----------

endpoint_requests.csv: Contains the number of requests for each endpoint.
success_failure.csv: Contains the count of successful and failed requests.
success_rate.csv: Contains the total success rate based on the total requests.

Generated Visualizations:
------------------------

requests_per_endpoint.png: A bar chart showing the number of requests for each endpoint.
success_vs_failure.png: A pie chart displaying the ratio of success to failure.
success_rate.png: A pie chart showing the success rate percentage.

Console Output:
--------------

Data has been saved to CSV files.
Visualizations have been generated and saved as images.

## Code Structure:
------------------

log_analysis.py: Contains functions for analyzing the log file, including counting requests, success/failure, and calculating success rate.
visualize.py: Contains functions for generating charts (bar charts and pie charts) using matplotlib.
main.py: The main entry point that integrates the analysis and visualization process.
requirements.txt: Lists the required Python libraries for the project.

## How the Code Works:
----------------------

Log Analysis (log_analysis.py):
-------------------------------

Reads and processes the log file.
Extracts endpoint requests and calculates success/failure counts for each IP address.
Computes the success rate of the server based on the total number of requests.

Visualization (visualize.py):
----------------------------

Uses the matplotlib library to create visual representations (bar charts and pie charts) based on the analysis.

Main Script (main.py):
----------------------

Calls the analysis and visualization functions in sequence.
Saves the output to CSV and generates the visualizations.

## Code Flow:
-------------

The log file is read and parsed for details like IP addresses, request types, and status codes.
The script processes the log to calculate:
The number of requests for each endpoint.
The number of successful and failed requests.
The success rate percentage.
The data is saved in CSV files for later analysis.
The script generates three visualizations (bar charts and pie charts) to provide insights into the server log behavior.

Example Log File (sample.log):
------------------------------
Here is a sample log file (sample.log) that you can use for testing:

192.168.1.1 - - [03/Dec/2024:10:12:34 +0000] "GET /home HTTP/1.1" 200 512
203.0.113.5 - - [03/Dec/2024:10:12:35 +0000] "POST /login HTTP/1.1" 401 128 "Invalid credentials"
10.0.0.2 - - [03/Dec/2024:10:12:36 +0000] "GET /about HTTP/1.1" 200 256


## Troubleshooting:
-------------------

Error: ModuleNotFoundError: If you get an error related to missing modules, ensure you’ve installed the required dependencies (matplotlib, etc.) via pip install -r requirements.txt.
File Path Error: Ensure that the path to your log file in main.py is correct. Update it to point to the actual location of the sample.log or your own log file.
