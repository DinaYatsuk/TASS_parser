# TASS News Scraper

This repository contains a set of Python scripts for scraping and processing news articles from the [TASS website](https://tass.ru/tag/ssha). The project uses Selenium for web scraping and BeautifulSoup for parsing HTML content.

## Features

- **Web Scraping**: Automates scrolling through web pages to load and collect links to news articles.
- **HTML Parsing**: Extracts information such as title, lead, content, and tags from the articles.
- **Parallel Processing**: Uses multiprocessing to efficiently process a large number of links.
- **Output**: Saves the scraped data as a CSV file for further analysis.

## File Descriptions

### 1. `link_scrapper.py`
Contains functions for automating the scraping of news article links:
- **`initialize_driver`**: Initializes a Selenium WebDriver.
- **`navigate_to_url`**: Navigates to a specified URL.
- **`scroll_page`**: Scrolls through the page to load all content dynamically.
- **`get_links`**: Extracts links to news articles from the page.
- **`process_website`**: Combines all steps to return a list of article links.

### 2. `parsing.py`
Handles the parsing of individual news articles:
- **`processing_links`**: Extracts key information (title, lead, content, and tags) from a given article link using BeautifulSoup.

### 3. `main.py`
The entry point of the application:
- Uses `link_scrapper.py` to collect article links.
- Processes the links in parallel using `parsing.py`.
- Saves the parsed data to a CSV file (`corpus_usa.csv`).

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/tass-news-scraper.git
   cd tass-news-scraper
   ```

2. **Install dependencies**:
   Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

   **Dependencies**:
   - Selenium
   - BeautifulSoup4
   - Requests
   - Pandas
   - TQDM

3. **Set up a WebDriver**:
   Download the appropriate WebDriver (e.g., ChromeDriver) for your browser version and add it to your PATH.

## Usage

1. **Run the script**:
   Execute the main script to start scraping and parsing:
   ```bash
   python main.py
   ```

2. **Output**:
   The parsed data will be saved in a file named `corpus_usa.csv` in the current directory.

## Notes

- **WebDriver Compatibility**: Ensure your WebDriver matches the browser version installed on your system.
- **Dynamic Content Loading**: The scraper dynamically scrolls through the page to load all articles.
- **Error Handling**: Articles with missing information will be skipped, and an error message will be printed to the console.

## Contributing

Contributions are welcome! Feel free to submit a pull request or open an issue for suggestions and improvements.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.


This `README.md` provides an overview of the project, setup instructions, usage details, and other important information for potential contributors or users.
