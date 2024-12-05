import matplotlib.pyplot as plt
import csv

# Function to visualize request count per endpoint from the CSV file
def visualize_requests_per_endpoint(csv_file):
    endpoints = []
    counts = []
    
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            endpoints.append(row[0])
            counts.append(int(row[1]))
    
    plt.figure(figsize=(10, 6))
    plt.bar(endpoints, counts, color='skyblue')
    plt.title("Number of Requests per Endpoint")
    plt.xlabel("Endpoints")
    plt.ylabel("Request Count")
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig('requests_per_endpoint.png')  # Save the figure as a PNG file
    plt.show()

# Function to visualize success vs failure rate from the CSV file
def visualize_success_failure(csv_file):
    labels = []
    sizes = []
    
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            labels.append(row[0])
            sizes.append(int(row[1]))
    
    colors = ['lightgreen', 'lightcoral']
    
    plt.figure(figsize=(7, 7))
    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
    plt.title("Success vs Failure Rate")
    plt.axis('equal')  # Equal aspect ratio ensures the pie chart is circular
    plt.savefig('success_vs_failure.png')  # Save the pie chart as a PNG file
    plt.show()

# Function to visualize the success rate from the CSV file
def visualize_success_rate(csv_file):
    total_requests = 0
    success_rate = 0
    
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        row = next(reader)  # Read the first row
        total_requests = int(row[0])
        success_rate = float(row[3])

    plt.figure(figsize=(6, 6))
    plt.bar(['Success Rate'], [success_rate], color='blue')
    plt.ylabel('Success Rate (%)')
    plt.title(f'Success Rate: {success_rate}%')
    plt.tight_layout()
    plt.savefig('success_rate.png')  # Save the bar chart as a PNG file
    plt.show()

if __name__ == '__main__':
    # Update the paths if your CSV files are in a different location
    visualize_requests_per_endpoint('endpoint_requests.csv')
    visualize_success_failure('success_failure.csv')
    visualize_success_rate('success_rate.csv')
