# Customer Segmentation & Sales Analytics 🛍️📊

This project demonstrates a full end-to-end customer analytics workflow, including data cleaning, exploratory analysis, RFM modeling, K-Means clustering, customer segmentation, and final insights visualization.
The goal is to help the business understand customer behavior, identify hight- value segments, and enable data-driven marketing, sales optimization, and rention strategies.

---

## Business Objective

The project aims to identify meaningful customer groups and support:

-Targeted and personalized marketing campaigns
-Customer retention and loyalty strategies
-Optimized promotions and pricing
-Customer lifecycle understanding
-Revenue growth and data-driven decision making

## Key Features

### 🔹 1. Data Cleaning

-Handling missing values
-Removing duplicates
-Fixing inconsistent formats (dates, prices, categories)
-Creating derived variables (e.g., sales_amount)
-Preparing the dataset for modeling and analysis

### 🔹 2. Exploratory Data Analysis (EDA)

-Purchase behavior trends
-Revenue distribution
-Top-selling product categories
-Customer lifecycle metrics
-Insights into patterns before segmentation

### 🔹 3. RFM Analysis  

RFM metrics were computed per customer:
| Metric        | Meaning                  |
| ------------- | ------------------------ |
| **Recency**   | Days since last purchase |
| **Frequency** | Number of purchases      |
| **Monetary**  | Total revenue generated  |

RFM provides behavioral insights and is used as input for clustering

### 🔹 4. Customer Segmentation (K-Clustering)

-Scaling and preprocessing of numerical features
-Evaluating optimal k using: Elbow Method - Silhouette Score
-Applying K-Means to generate customer segments
-Profiling each cluster for business interpretation   

### 🔹 5. Sales & Segment Dashboard (Power BI)
Includes:

-Segment performance
-Revenue per customer type
-RFM distribution
-Time-series purchasing trends
Data model optimized for BI

---

## 📂 Project Structure


```bash
customer-segmentation-sales-analytics/
│
├── data/
│   ├── raw/              # Raw input datasets
│   └── processed/        # Cleaned / transformed datasets
│
├── notebooks/
│   ├── 01_data_cleaning.ipynb
│   ├── 02_rfm_analysis.ipynb
│   ├── 03_clustering.ipynb
│   └── 04_powerbi_preparation.ipynb
│
├── src/                  # Python scripts (to be filled)
│   ├── data_preprocessing.py
│   ├── rfm.py
│   ├── clustering.py
│   └── visualization.py
│
├── reports/
│   └── figures/          # Visual outputs (Elbow, Silhouette, PCA, dashboards)
│
├── dashboards/           # Power BI dashboard folder
│
├── requirements.txt
└── README.md
```



---

## 🧰 Tools & Technologies
| Category        | Tools                                         |
| --------------- | --------------------------------------------- |
| Data Analysis   | Python (Pandas, NumPy), Excel                 |
| Modeling        | Scikit-learn                                  |
| Analytics       | RFM, Clustering, EDA                          |
| Visualization   | Power BI, Matplotlib, Seaborn                 |
| Version Control | Git & GitHub                                  |
| Project Skills  | KPI design, segmentation, insight development |
|

---

## Key Insights From Clustering

### Cluster 0 – High-Value / VIP Customers

-High frequency
-High monetary value
-Recent activity

Priority for loyalty programs and exclusive offers.

### Cluster 1 – Low-Value / Occasional Buyers

-Low purchase frequency
-Low monetary contribution

Engage through promotions, discounts, and onboarding flows.

### Cluster 2 – Loyal Mid-Tier Customers

-Good frequency
-Consistent spending

Ideal for upselling and product bundles.

### Cluster 3 – Churn-Risk Customers

-Very high recency (inactive)
-Low spending

Requires reactivation or win-back strategy

## How to Run the Project
How to Run the Project

## 1. Install requirements
pip install -r requirements.txt

## 2. Open notebooks
jupyter notebook

## 3. Run each step in order:

 1. 01_data_cleaning.ipynb
 2. 02_rfm_analysis.ipynb
 3. 03_clustering.ipynb
 4. 04_powerbi_preparation.ipynb
   
## 👩‍💻 About Me  
I’m **Irais Ontiveros**, an Industrial Engineer pursuing a **Master’s in Data Science** in Rome, Italy.

-Passionate about:
-Data analysis
-KPIs & reporting
-Dashboards & automation
-Business insights

📫 **Connect with me on LinkedIn:**  
[linkedin.com/in/irais-ontiveros-duran-7528b820b](https://linkedin.com/in/irais-ontiveros-duran-7528b820b)



