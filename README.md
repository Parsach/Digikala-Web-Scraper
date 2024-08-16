Below is a structured `README.md` file based on the description you provided. This template includes all the necessary details about the app, how to install and use it, and how to contact you.

---

# Digikala Scraper

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)

## Table of Contents
- [About](#about)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contact](#contact)
- [License](#license)

## About

Digikala Scraper is a Python application designed to scrape data (text, images, etc.) from the Digikala website. The application can download and save all photos within a category or individually, and it includes functionality to identify objects in saved images and extract various parts of each product.

## Features

- **Scrape Data:** Collect product data from Digikala, including text and images.
- **Save Images:** Download and save images for each product in specified categories.
- **Object Detection:** Analyze saved images to find and extract specific parts of the product.

## Installation

To use this application, follow the steps below to install the necessary dependencies and set up the environment.

### Prerequisites

1. Python 3.x
2. WebDriver (e.g., ChromeDriver)
3. Required Python libraries listed in `requirements.txt`

### Steps

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/digikala-scraper.git
    cd digikala-scraper
    ```

2. Install the required libraries:

    ```bash
    pip install -r requirements.txt
    ```

3. Install the WebDriver for your preferred browser (e.g., [ChromeDriver](https://sites.google.com/chromium.org/driver/)).

## Usage

Follow the steps below to use the application:

1. **Scrape Product List:**

    - Replace the category URL in `product_list.py`.
    - Run the script:

    ```bash
    python product_list.py
    ```

    - **Output:** A text file containing a list of all products in the specified category.

2. **Process Images:**

    - Run `images.py` to read the product list and process each product:

    ```bash
    python images.py
    ```

    - **Output:** Creates a new text file for all images, organized by product number.

3. **Download Images:**

    - Run `saveimage.py` to download the images:

    ```bash
    python saveimage.py
    ```

## Contact

If you have any questions or suggestions, feel free to reach out:

- **Email:** Parsa.ch.1381@gmail.com

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Feel free to replace any placeholder text (like repository links) with your actual project details. This `README.md` should give users a clear understanding of what the project does and how to use it.
