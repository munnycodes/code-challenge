# Van Gogh Paintings Parser

## Overview
This project is a web scraper designed to extract details about Vincent van Gogh's paintings from an HTML file containing a Google search results page. It utilizes Selenium to parse the document and extract relevant painting data, including:

- `name`
- `date` (through the `extensions` array)
- Google `link`
- Thumbnail image URL

The extracted data is saved in a structured JSON format.

## Features
- Parses an HTML file containing Google search results for Van Gogh paintings
- Extracts painting details using Selenium
- Saves the output as a structured JSON file
- Runs in a headless Firefox browser for efficiency

## Prerequisites
Ensure you have the following installed on your system:
- Python 3.8+
- Firefox browser
- Geckodriver (required by Selenium to control Firefox)

## Installation

1. Clone this repository

2. Create a virtual environment (optional but recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate  
   ```

3. Install the required dependencies:
   ```bash
   pip3 install -r requirements.txt
   ```

## Usage

1. Place the target HTML file (`van-gogh-paintings.html`) in the project directory.
2. Run the parser script:
   ```bash
   python3 parser.py
   ```
3. The extracted data will be saved as `actual-array.json`.

## Project Structure
```
.
├── parser.py               # Main script for parsing the HTML file
├── requirements.txt        # List of dependencies
├── van-gogh-paintings.html # Local HTML file
├── actual-array.json       # Output file containing extracted painting data
├── expected-array.json     # File containing expected output
├── README.md               # Project documentation
```

## Testing
To verify functionality, run the test suite:
```bash
python test_parser.py
```

## Dependencies
The project uses the following libraries:
- `selenium` for web scraping
- `json` for data serialization
- `pathlib` for file path handling

For a full list of dependencies, refer to `requirements.txt`.

## Notes
- The script is designed to work with a specific structure of Google's search results page. If the structure changes, the class names used for extraction (`carousel_item_class_name`, `title_class_name`, etc.) may need updating.
- The scraper does not make external HTTP requests; it operates on a locally saved HTML file.

## License
This project is licensed under the MIT License.

## Author
munnycodes
