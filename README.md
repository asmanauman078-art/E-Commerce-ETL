# E-Commerce Products ETL Pipeline and Exploratory Data Analysis

## 1. Project Overview

The E-Commerce Products ETL Pipeline and Exploratory Data Analysis project is designed to extract product data from the DummyJSON Products API, transform and validate the data, and load the cleaned data into a CSV file.

The project also provides an interactive Flask-based dashboard where users can explore products, search and filter categories, view statistical summaries, and analyze data through visualizations.

## 2. Project Objectives

- Extract product information from an external API.
- Clean and transform raw product data.
- Validate product information using Pydantic.
- Store cleaned data in CSV format.
- Perform Exploratory Data Analysis (EDA).
- Generate data visualizations using Matplotlib.
- Develop an interactive dashboard using Flask.

## 3. Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Flask | Web application and dashboard |
| Requests | API integration |
| Pandas | Data cleaning and analysis |
| Pydantic | Data validation |
| Matplotlib | Data visualization |
| HTML | Dashboard structure |
| CSS | Dashboard styling |
| JavaScript | Search, filtering and dynamic data |
| DummyJSON API | Product data source |

## 4. Data Source

**API:** https://dummyjson.com/products

The API provides product information, including:
- Product ID
- Product Title
- Price
- Category
- Rating
- Stock
- Brand
- Thumbnail Image

## 5. ETL Workflow

### Extract
Product data is fetched from the DummyJSON Products API using the Python Requests library.

### Transform
The extracted data is cleaned by selecting relevant fields and assigning default values where necessary.

### Validate
Pydantic is used to validate product fields and their data types.

### Load
The validated product data is converted into a Pandas DataFrame and saved as a CSV file.

**Output:** `outputs/products.csv`

## 6. Exploratory Data Analysis (EDA)

Pandas is used to analyze the cleaned product dataset.

The analysis includes:

- Dataset information
- Product category counts
- Average product price
- Most expensive product
- Product price distribution
- Product rating distribution

## 7. Data Visualizations

Three visualizations are generated using Matplotlib:

1. Products by Category — Bar Chart
2. Product Price Distribution — Histogram
3. Product Rating Distribution — Histogram

Charts are saved in the `reports/` directory.

## 8. Dashboard Features

- Interactive product dashboard
- Product search functionality
- Category filtering
- Total products statistics
- Average price statistics
- Average rating statistics
- Product images and details
- EDA charts display
- CSV download functionality

## 9. Project Folder Structure

```text
E-Commerce-ETL/
│
├── app.py
├── analysis.py
├── README.md
│
├── templates/
│   └── index.html
│
├── static/
│   ├── style.css
│   └── script.js
│
├── outputs/
│   └── products.csv
│
├── reports/
│   ├── category_chart.png
│   ├── price_chart.png
│   └── rating_chart.png
│
└── venv/
```

## 10. Installation and Execution

### Step 1: Install Required Libraries

```bash
pip install flask requests pandas pydantic matplotlib
```

### Step 2: Run the Flask Application

```bash
python app.py
```

### Step 3: Generate Product CSV

Open the following URL in your browser:

http://127.0.0.1:5000/api/products

This fetches, transforms, validates, and saves product data.

### Step 4: Generate EDA Reports

Stop the Flask server using `Ctrl + C`, then run:

```bash
python analysis.py
```

This generates the three visualization charts inside the reports folder.

### Step 5: Open the Dashboard

Run the Flask application again:

```bash
python app.py
```

Open:

http://127.0.0.1:5000

## 11. Expected Outputs

- Cleaned product dataset in CSV format.
- Product analysis results in the terminal.
- Three visualization charts.
- Interactive Flask dashboard.
- Downloadable CSV dataset.

## 12. Conclusion

This project demonstrates the implementation of an ETL pipeline using Python. It combines API integration, data transformation, validation, data storage, exploratory data analysis, and visualization in a single e-commerce analytics application.