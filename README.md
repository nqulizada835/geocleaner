# GeoCleaner

A lightweight Python package for cleaning and standardizing US street addresses before geocoding or mapping.  
It focuses on parsing, formatting, and basic validation of address strings.

---

## Features

- **Parses US addresses** from various formats (with or without commas)
- **Standardizes addresses** to a consistent format:  
  `Street, City, State ZIP`
- **Validates state abbreviations** and basic address structure
- **Optional geocoding** (requires `geopy`)

---

## Installation

Install the package using pip:pip install geocleaner



Or, for development, install in editable mode from the project root:pip install -e .


---

## Usage

from geocleaner.core import clean_location
print(clean_location("   new york  "))  


---

## Contributing

Contributions are welcome!  
Please open an issue or submit a pull request on GitHub.

---

## License

[MIT License](LICENSE) 
