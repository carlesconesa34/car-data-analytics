# 🚗 Car Data Analytics

A data analytics project that performs exploratory data analysis (EDA) on a car price dataset and visualizes insights through an interactive Power BI dashboard.

---

## 📋 Table of Contents

- [About the Project](#about-the-project)
- [Dataset](#dataset)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Exploratory Data Analysis](#exploratory-data-analysis)
- [Power BI Dashboard](#power-bi-dashboard)
- [License](#license)

---

## About the Project

This project analyzes a dataset containing information about 2,000 vehicles, covering technical, commercial, and usage characteristics. The goal is to answer five key business questions through an interactive Power BI dashboard:

1. **Which brand offers the best HP/Price ratio?**
2. **How does fuel type influence the sale price?**
3. **How does price depreciate based on year and mileage?**
4. **What is the profile of the most expensive vs. most affordable cars?**
5. **Does the number of previous owners affect the price?**

---

## Dataset

The dataset contains **2,000 records** and **11 variables**:

| Variable | Type | Description |
|---|---|---|
| `Car_ID` | Integer | Unique vehicle identifier |
| `Brand` | Text | Vehicle brand |
| `Model_Year` | Integer | Year of manufacture |
| `Engine_Size` | Decimal | Engine displacement (litres) |
| `Fuel_Type` | Text | Type of fuel |
| `Transmission` | Text | Type of transmission |
| `Mileage` | Integer | Vehicle mileage (km) |
| `Doors` | Integer | Number of doors |
| `Owner_Count` | Integer | Number of previous owners |
| `Horsepower` | Integer | Engine power (HP) |
| `Price` | Decimal | Sale price (€) |

**Key stats:**
- Price range: €18,912 – €72,268 (avg. €46,170)
- Mileage range: 5,036 – 199,904 km (avg. 100,737 km)
- Model years: 2005 – 2023
- Brands: Toyota, Hyundai, Tesla, Honda, Ford, BMW

---

## Project Structure

```
car-data-analytics/
│
├── data/
│   └── car_price_dataset.csv       # Raw dataset
│
├── src/
│   └── eda.py                      # Exploratory Data Analysis script
│
├── dashboard/
│   └── car_price_dashboard.pbix    # Power BI dashboard
│
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

---

## Getting Started

### Prerequisites

- Python 3.8+
- Power BI Desktop

### Installation

1. Clone the repository:

```bash
git clone https://github.com/carlesconesa34/car-data-analytics.git
cd car-data-analytics
```

2. Create and activate a virtual environment:

```bash
python -m venv .venv

# Windows
.venv\Scripts\activate.bat

# macOS/Linux
source .venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

### Run the EDA

```bash
python src/eda.py
```

---

## Exploratory Data Analysis

The EDA script (`src/eda.py`) performs the following steps:

- **Data loading** — loads the dataset using Pandas
- **First inspection** — checks shape, column types and sample rows
- **Data quality** — verifies there are no null values or duplicate records
- **Descriptive statistics** — generates summary stats for numerical variables
- **Categorical analysis** — counts distribution of brands, fuel types, transmission and doors

**Key findings:**
- The dataset is clean: 0 null values, 0 duplicates
- All categorical variables are well balanced across their categories
- High price variability (€18,912 – €72,268) suggests meaningful differentiating factors
- High mileage dispersion makes it relevant to analyze its relationship with price

---

## Power BI Dashboard

The dashboard (`car_price_dashboard.pbix`) is built in Power BI Desktop and consists of a single page with the following visuals:

| Visual | Question answered |
|---|---|
| Clustered bar chart — HP/Price by brand | Q1 — Best HP/Price ratio per brand |
| Clustered bar chart — Average price by fuel type | Q2 — Fuel type vs. price |
| Scatter plot — Mileage vs. Price (by year) | Q3 — Price depreciation |
| Clustered bar chart — Max & min price by brand | Q4 — Most expensive vs. most affordable profile |
| Line chart — Average price by owner count | Q5 — Impact of previous owners on price |

**DAX measures used:**

```dax
averagePrice    = AVERAGE(car_price_dataset[Price])
totalCars       = COUNTROWS(car_price_dataset)
averageHorsepower = AVERAGE(car_price_dataset[Horsepower])
averageMileage  = AVERAGE(car_price_dataset[Mileage])
ratioHPPrice    = DIVIDE(AVERAGE(car_price_dataset[Horsepower]), AVERAGE(car_price_dataset[Price]))
maxPrice        = MAX(car_price_dataset[Price])
minPrice        = MIN(car_price_dataset[Price])
```

> **Note:** When loading the CSV in Power BI, make sure to set the locale to **English (United States)** so that decimal points are read correctly.

---

## License

Distributed under the Apache 2.0 License. See [`LICENSE`](LICENSE) for more information.