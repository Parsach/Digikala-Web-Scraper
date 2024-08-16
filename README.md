---

# Digikala Scraper

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)

## Table of Contents
- [About](#about)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
  - [Step 1: Scrape Product List](#step-1-scrape-product-list)
  - [Step 2: Process Images](#step-2-process-images)
  - [Step 3: Download Images](#step-3-download-images)
  - [Step 4: Object Detection with Jupyter Notebook](#step-4-object-detection-with-jupyter-notebook)
- [Configuration](#configuration)
- [Examples](#examples)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [Contact](#contact)
- [License](#license)

## About

**Digikala Scraper** is a Python application designed to scrape data (text, images, etc.) from the Digikala website. You can download and save images from any category or specific products. Additionally, this app features object detection, enabling you to identify and extract specific parts of products from the saved images using a Jupyter Notebook.

## Features

- **Comprehensive Scraping:** Extract detailed product information from Digikala, including text descriptions and images.
- **Batch Image Download:** Download images for entire product categories or individual items.
- **Object Detection and Extraction:** Use a Jupyter Notebook for advanced image processing to detect and extract specific parts of products from saved images.
- **Customizable:** Easily modify the script to target different categories or specific product attributes.

## Installation

To get started with Digikala Scraper, set up your Python environment and install the required dependencies.

### Prerequisites

- Python 3.x
- WebDriver (e.g., ChromeDriver)
- Jupyter Notebook
- Required Python libraries (listed in `requirements.txt`)

### Steps

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/your-username/digikala-scraper.git
    cd digikala-scraper
    ```

2. **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Set Up WebDriver:**
   
   Download and install the WebDriver corresponding to your preferred browser (e.g., [ChromeDriver](https://sites.google.com/chromium.org/driver/)). Ensure that the WebDriver is in your system's PATH.

4. **Install Jupyter Notebook:**

    If you don't have Jupyter Notebook installed, you can install it using pip:

    ```bash
    pip install notebook
    ```

## Usage

Follow these steps to scrape product data, process images, download them, and perform object detection:

### Step 1: Scrape Product List

- Open `product_list.py`.
- Replace the placeholder with your desired category URL.
- Run the script to generate a text file containing all products in the specified category:

```bash
python product_list.py
```

**Output:** A text file with a list of product URLs from the chosen category.

### Step 2: Process Images

- Run `images.py` to read the previously generated text file and process each product URL:

```bash
python images.py
```

**Output:** A text file organizing image URLs by product number.

### Step 3: Download Images

- Execute `saveimage.py` to download all images listed in the text file created by `images.py`:

```bash
python saveimage.py
```

**Output:** Images are downloaded and saved into folders, each named after the corresponding product.

### Step 4: Object Detection with Jupyter Notebook

- Open the Jupyter Notebook provided in the repository (`object_detection.ipynb`).

- Follow the instructions in the notebook to load the saved images and perform object detection. The notebook is designed to help you detect and extract specific parts of the products, such as logos, labels, or other distinctive features.

- You can run the notebook using the following command:

```bash
jupyter notebook object_detection.ipynb
```

**Output:** The notebook will process the images and allow you to visualize and save the detected objects.

## Configuration

If you need to customize the behavior of the scraper, you can modify the following settings:

- **Category URL:** Replace the placeholder URL in `product_list.py` with the Digikala category URL you want to scrape.
- **Output Directories:** Adjust the output directories in `images.py` and `saveimage.py` if needed.
- **Object Detection Parameters:** Modify the object detection parameters in the Jupyter Notebook to suit your needs.

## Examples

Here are a few examples of how the Digikala Scraper can be used:

- **Example 1:** Scrape all smartphones in the mobile category and download their images.
- **Example 2:** Use the Jupyter Notebook to detect and extract specific features from the saved images.

```python
# Example command to scrape the mobile category
python product_list.py --url "https://www.digikala.com/search/category-mobile/"
```

## Troubleshooting

If you encounter issues while using the scraper, consider the following:

- **WebDriver Issues:** Ensure that your WebDriver version matches your browser version.
- **Jupyter Notebook Issues:** Make sure you have all the required Python packages installed. Check the notebook's instructions for additional dependencies.
- **Missing Dependencies:** Double-check that all required libraries are installed using `pip install -r requirements.txt`.
- **Unexpected Behavior:** Review the log files generated during script execution to diagnose issues.

## Contributing

Contributions are welcome! If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a Pull Request.

Please refer to the [CONTRIBUTING.md](link-to-contributing-guide) for more details.

## Contact

If you have any questions, suggestions, or need further assistance, feel free to contact me:

- **Email:** Parsa.ch.1381@gmail.com

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
