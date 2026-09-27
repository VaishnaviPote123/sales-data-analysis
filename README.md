# 📊 Sales Data Analysis Dashboard

A Python-based **Sales Data Analysis and Interactive Dashboard** built using Pandas, NumPy, Matplotlib, Seaborn, and Streamlit.

The project analyzes retail sales data to identify sales trends, profitable categories, regional performance, top-selling products, customer segments, and the relationship between sales and profit.

## 🚀 Project Overview

The objective of this project is to analyze retail sales data and convert raw business data into meaningful insights using **data cleaning, exploratory data analysis (EDA), statistical analysis, and visualization**.

An interactive **Streamlit dashboard** is included to make the analysis easier to explore.

## 🛠️ Technologies Used

* **Python**
* **Pandas** – Data cleaning and analysis
* **NumPy** – Numerical operations
* **Matplotlib** – Data visualization
* **Seaborn** – Statistical visualization
* **Streamlit** – Interactive dashboard
* **Git & GitHub** – Version control

## 📁 Project Structure

```text
Sales Data Analysis/
│
├── app.py
├── sales_analysis.py
├── README.md
├── requirements.txt
│
└── data/
    └── superstore.csv
```

## 📌 Dataset

The project uses a retail **Superstore Sales Dataset** containing approximately **10,000+ sales records**.

The dataset contains information such as:

* Order ID
* Order Date
* Ship Date
* Ship Mode
* Customer ID
* Customer Name
* Segment
* City
* State
* Region
* Product ID
* Category
* Sub-Category
* Product Name
* Sales
* Quantity
* Discount
* Profit

## 🔍 Data Analysis Performed

### 1. Data Cleaning

* Checked dataset dimensions
* Checked missing values
* Checked duplicate records
* Converted date columns into datetime format
* Verified numerical columns
* Performed basic statistical analysis

### 2. Sales Analysis

* Total sales
* Total profit
* Total quantity sold
* Average sales
* Profit margin
* Sales by category
* Sales by region
* Sales by sub-category
* Sales by customer segment

### 3. Product Analysis

* Top 10 products based on sales
* Top products based on profit
* Product-level sales comparison

### 4. Time-Series Analysis

* Monthly sales analysis
* Sales trend over time
* Identification of high-sales months

### 5. Correlation Analysis

Analyzed the relationship between:

* Sales
* Profit
* Quantity
* Discount

## 📊 Dashboard Features

The Streamlit dashboard contains multiple views:

* 🏠 Home
* 📈 Sales Overview
* 📦 Category Analysis
* 🌎 Regional Analysis
* 🏆 Product Analysis
* 📅 Monthly Trends
* 👥 Customer & Shipping Analysis
* 🔗 Correlation Analysis

The dashboard also provides **Previous, Next, Home, and Next View navigation** for moving between different analysis sections.

## ▶️ How to Run the Project

### Step 1: Clone the Repository

```bash
git clone https://github.com/VaishnaviPote123/sales-data-analysis.git
```

### Step 2: Open the Project

```bash
cd sales-data-analysis
```

### Step 3: Install Required Libraries

```bash
pip install -r requirements.txt
```

### Step 4: Run the Streamlit Dashboard

```bash
streamlit run app.py
```

The dashboard will open in your browser.

## 📈 Key Insights

The analysis can be used to understand:

* Which product categories generate higher sales
* Which regions contribute more to revenue
* Which products have strong sales performance
* How sales change over time
* Which customer segments generate more sales
* How discounts affect profit
* The relationship between sales and profit

## 💡 Business Applications

This analysis can help businesses with:

* Sales performance monitoring
* Product performance analysis
* Regional sales planning
* Customer segmentation
* Profitability analysis
* Sales trend identification
* Data-driven decision making

## 🎯 Skills Demonstrated

This project demonstrates practical knowledge of:

* Python programming
* Pandas
* NumPy
* Data Cleaning
* Exploratory Data Analysis
* Data Visualization
* Statistical Analysis
* GroupBy and Aggregation
* Date-Time Analysis
* Streamlit Dashboard Development
* Git & GitHub

## 👩‍💻 Author

**Vaishnavi Pote**


