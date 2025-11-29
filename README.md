# Customer Segmentation & Sales Analytics 🛍️📊


This project delivers an end-to-end analytics workflow combining RFM segmentation, clustering, sales insights, and dashboard reporting.
It simulates a real-world business case where a retail company wants to better understand customer behavior and apply data-driven strategies.
  

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

Cluster 0: High-value, loyal, frequent buyers

Cluster 1: At-risk customers with decreasing activity

Cluster 2: New or one-time buyers

Cluster 3: Value-driven customers with moderate spend

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



