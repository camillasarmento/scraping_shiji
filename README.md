# scraping_shiji

How to Execute the Scraping Script

## Getting Started

### Install Python
* Download and install Python from python.org.
* During installation, ensure you check the box "Add Python to PATH".

### Install Required Libraries
* Open a terminal or command prompt.
* Install the necessary Python libraries by running:
```
pip install beautifulsoup4 requests
```

###  Save the Script
* Copy the provided code into a file and save it as scraper.py in a folder of your choice.

### Run the Script
Open the terminal or command prompt.
Navigate to the folder where scraper.py is saved. For example:
bash
```
cd path\to\your\script
```
* Run the script by typing:
```
python scraper.py
```
### Output File
* The script will generate a file named data.csv in the same folder as the script.
* This file contains the scraped data in a tabular format with the following columns:
  * Section: The category of the item (e.g., "Customer Support", "Products").
  * Address: The email or URL for the item.
  * Name: The name or description of the item.

### Open the CSV File
* Open data.csv using any spreadsheet software, such as Microsoft Excel, Google Sheets, or a text editor.

### Common Issues and Troubleshooting
* ModuleNotFoundError: No module named 'requests' or 'beautifulsoup4':
    * Ensure you’ve installed the required libraries using: 
```
pip install requests beautifulsoup4
```
* Script Does Not Run:
  * Ensure you are using the correct command (python scraper.py) in the terminal and that you are in the correct directory.
* Empty data.csv:
    * If the output file is empty, check that the website's structure has not changed. You can debug by adding print() statements in the code to inspect the data being scraped.




