# Customer Segmentation & Sales Analytics 🛍️📊

This project demonstrates a full end-to-end customer analytics workflow, including data cleaning, RFM analysis, clustering using K-Means, segmentation interpretation, and visualization.

The goal is to help a company better understand customer behavior, identify high-value segments, and provide actionable insights for marketing and sales teams.

---

## Business Objective

-Identify high-value customers, understand purchasing patterns, and build customer segments that support:

- Targeted marketing campaigns
- Improved retention strategies
- Optimized sales and promotions
- Customer lifecycle understanding
- Revenue growth initiatives

## Key Features

### 🔹 1. Data Cleaning  
 - Handling missing values
 - Removing duplicates
 - Standardizing formats
 - Preparing the dataset for modeling

### 🔹 2. Exploratory Data Analysis (EDA)
- Purchase behavior trends
- Revenue distribution  
- CTop-selling categories  
- Customer lifecycle metrics  

### 🔹 3. RFM Analysis  
- **Recency:** How recently a customer purchased  
- **Frequency:** How often they purchase  
- **Monetary Value:** How much they spend

 Used for pre-segmentation and business insights.

### 🔹 4. Customer Segmentation (Clustering)
- K-Means clustering  
- Optimal k using Elbow & Silhouette methods
- BSegment profiling
- Marketing recommendations   

### 🔹 5. Sales & Segment Dashboard (Power BI)
- Segment performance  
- Revenue by customer type  
- RFM distribution  
- Time-series trends  

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

## Key Insights

Cluster 0: Represents the most valuable customers (high frequency & monetary, recent activity)

Cluster 1: Includes occasional low-value buyers

Cluster 2: includes loyal mid-tier customers

Cluster 3: Represents churn-risk customers with long inactivity.

These insights support pricing strategies, loyalty programs, and targeted marketing.

## How to Run the Project
How to Run the Project

## 1. Install requirements
pip install -r requirements.txt

## 2. Open notebooks
jupyter notebook

## 3. Run each step in order:
   1.Data Cleaning
   2.RFM Analysis
   3.Clustering
   4.Export for Dashboard
   
## 👩‍💻 About Me  
I’m **Irais Ontiveros**, an Industrial Engineer pursuing a **Master’s in Data Science** in Rome, Italy.

-Passionate about:
-Data analysis
-KPIs & reporting
-Dashboards & automation
-Business insights

📫 **Connect with me on LinkedIn:**  
[linkedin.com/in/irais-ontiveros-duran-7528b820b](https://linkedin.com/in/irais-ontiveros-duran-7528b820b)



