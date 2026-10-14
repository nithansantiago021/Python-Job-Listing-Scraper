import csv
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

URL = "https://realpython.github.io/fake-jobs/"
OUTPUT_FILE = "jobs.csv"


def scrape_jobs():
    try:
        response = requests.get(URL, timeout=10)
        response.raise_for_status()
    except requests.RequestException as error:
        print(f"Error fetching webpage: {error}")
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    jobs = []

    job_cards = soup.select("div.card-content")

    for card in job_cards:
        title_element = card.select_one("h2.title")
        company_element = card.select_one("h3.company")
        location_element = card.select_one("p.location")

        link_element = card.select_one("a.card-footer-item")

        title = title_element.get_text(strip=True) if title_element else ""
        company = company_element.get_text(strip=True) if company_element else ""
        location = location_element.get_text(strip=True) if location_element else ""

        link_element = card.select_one("a.card-footer-item")

        if link_element:
            href = link_element.get("href")

            if isinstance(href, str):
                detail_url = urljoin(URL, href)
            else:
                detail_url = ""
        else:
            detail_url = ""


        jobs.append({
            "Job Title": title,
            "Company": company,
            "Location": location,
            "Job Detail URL": detail_url,
        })

    return jobs


def save_to_csv(jobs):
    fieldnames = ["Job Title", "Company", "Location", "Job Detail URL"]

    try:
        with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(jobs)

        print(f"Saved {len(jobs)} jobs to {OUTPUT_FILE}")

    except OSError as error:
        print(f"Error writing CSV file: {error}")


def main():
    jobs = scrape_jobs()

    if not jobs:
        print("No jobs were found.")
        return

    save_to_csv(jobs)


if __name__ == "__main__":
    main()
