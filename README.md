# Python Job Listings Scraper
A demonstration of a light weight Python web scraper that extracts job postings from https://realpython.github.io/fake-jobs/ test website and exports the structured data into a CSV file.

## Project Details
Project URL: https://roadmap.sh/projects/job-listings-scraper

## Tech stack
- **Requests**: To perform HTTP GET requests and fetch raw HTML web pages.
- **Beautiful Soup (bs4)**: To parse HTML documents and navigate the DOM tree.
- **CSV (Standard Library)**: To store, format, and save job listings into CSV format. 

## Running the project

### Prerequisites
Make sure Python 3.10+ is installed on your system.

### Installation
Clone the repository and install the required Python libraries:
```BASH
# clone the repository
git clone https://github.com/nithansantiago021/Python-Job-Listing-Scraper.git
cd Python-Job-Listing-Scraper

# Install dependencies
pip install requests bs4
```

### Execution
Run the main scraper script:

```BASH
python3 scrapping.py
```
upon successful run, the scarper prints a status message and populates `jobs.csv`

```BASH
Saved 100 jobs to jobs.csv
```

### License
This project is licensed under the MIT License.