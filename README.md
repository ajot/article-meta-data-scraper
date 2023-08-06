# Article Metadata Scraper

A simple Python script to extract and organize specific data from various web sources. Given a list of URLs, the script can parse web content from these sources and save the structured data into a CSV file.

## Features
- Reads input URLs from a CSV file.
- Supports extraction from various sources like Retool, ajot.me, Curious Mints, warp.dev, and Amazon.
- Extracts information such as Title, Date, Source, Category, and OpenGraph Image URL.
- Converts extracted date to a consistent YYYY-MM-DD format.
- Saves the extracted data into an output CSV file.

## Installation

To run this script, you need to have Python 3 and pip (Python package installer) installed on your system. The script uses the BeautifulSoup4 and requests libraries. You can install these using pip:

```bash
pip install beautifulsoup4 requests
```

## Usage
To use this script, you need a CSV file with a list of URLs to scrape. The URLs should be in a column named 'URL' (or modify the script to match your column name). 

1. Populate input.csv with the URLs you wish to parse, ensuring the URLs are under a column named 'URL'.

2. Execute the script:

```bash
python src/main.py
```
3. Refer to output.csv for the structured data.

## Customization
The script can be customized to work with other websites or to extract different information. You would need to modify the BeautifulSoup selectors to match the HTML structure of the target website.

## Contributing
Feel free to contribute to this repository by forking and submitting a pull request. For any major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)