import requests
from bs4 import BeautifulSoup
from datetime import datetime
import csv

# Function for date conversion
def convert_to_desired_format(date_string):
    formats_to_try = [
        "%Y-%m-%d",
        "%d %B %Y",
        "%d %b %Y",
        "%b %d, %Y",
        "%B %d, %Y",
    ]

    for format_str in formats_to_try:
        try:
            date_obj = datetime.strptime(date_string, format_str)
            return date_obj.strftime("%Y-%m-%d")
        except ValueError:
            pass

    return None  # Return None if the date string is in an unsupported format

# Read URLs from a CSV file
with open('input.csv', 'r') as file:
    reader = csv.DictReader(file)
    urls = [row['URL'] for row in reader]  # Replace 'URL' with the actual column name in your CSV

# Open the output CSV file
with open('output.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "URL", "Date", "Source", "Category","Image URL"])  # Write the header

    for url in urls:
        print("*******************")
        print(f"parsing {url}")
        print("*******************")
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        # Check if the URL is from Amazon or Retool
        if 'retool' in url:
            title = soup.find('h1', class_='post-full-title').text
            date = soup.find('p', class_='post-full-meta-date').text
            source = "Retool"
            category = "Blog Post"
        elif 'ajot.me' in url:
            title = soup.find('h1', class_='article-title').text
            date = soup.find('time', class_='byline-meta-date').text
            source = "ajot.me"
            category = "Blog Post"
        elif 'curiousmints' in url:
            title = soup.select_one('div.blog-article-page h1.leading-snug').text
            date = soup.select_one('div.blog-article-page a.tooltip-handle').text
            source = "Curious Mints"
            category = "Blog Post"
        elif 'warp.dev' in url:
            title = soup.find('h1', class_='h1-ovrd').text
            date = soup.find('p', class_='date-term').text.split(" ")[-1]
            source = "warp.dev"
            category = "Documentation"           
        else:
            title = soup.find('div', class_='entryTitle').find('a').text
            date = soup.find('p', class_='dex-blog-post-summary-date').text
            source = "Amazon"
            category = "Alexa"
        og_image = soup.find('meta', property='og:image')
        # If an og:image tag is found
        if og_image:
            og_image_url = og_image.get('content')
            print(og_image_url)

        print("Raw Date:", date)  # Print the date before parsing
        # Parse date and convert it to the desired format
        date = convert_to_desired_format(date)

        print(f"title:{title},date:{date},source:{source},category:{category},og_image:{og_image_url}")
        writer.writerow([title, url, date, source, category, og_image_url])  # Write the data row
