# 🏥 Healthcare Operations Analytics  
Improving patient flow, reducing wait times, and strengthening operational performance through data.

## 📌 Project Overview
This project analyzes a large health data to understand how patients move through the hospital system and where operational inefficiencies occur. The goal is to translate raw encounter data into insights that support better staffing, smoother patient flow, and improved patient experience.

The dataset includes demographics, visit types, timestamps, wait times, satisfaction scores, and department‑level information—providing a full view of the patient journey from arrival to outcome.

---

## 🎯 Business Objectives
- Identify trends in patient demand across months, visit types, and departments  
- Quantify wait time issues and pinpoint where delays originate  
- Evaluate service efficiency and patient satisfaction  
- Understand how staffing patterns align with patient load  
- Recommend operational improvements grounded in data  

---

## 📊 Key Performance Indicators (KPIs)
- **Monthly & Yearly Patient Volume** – demand trends and seasonality  
- **Visit Type Mix** – Emergency, Walk‑in, Scheduled  
- **Average Wait Time** – overall and by department  
- **% of Patients Waiting > 30 Minutes** – service efficiency  
- **Hourly Arrival Patterns** – peak and off‑peak periods  
- **Department‑Hour Bottlenecks** – where delays cluster  
- **Patient Satisfaction Score** – experience metric  
- **Admission Rate** – by department and visit type  
- **Shift‑Based Load** – patient volume per doctor shift  

---

## 🧹 Data Preparation
The raw dataset required several corrections and standardizations before analysis. Key steps included:

- Converting date/time fields into usable formats  
- Standardizing inconsistent gender entries  
- Handling missing department and doctor identifiers  
- Preserving null satisfaction scores to avoid bias  
- Validating the 15‑month encounter range  

These steps ensured the dataset was reliable enough for operational analysis.

---

## 🛠️ Tools & Technologies
- **SQL** – primary engine for analysis  
- **Python / Pandas** – optional for extended EDA  
- **Power BI / Tableau** – dashboarding and visualization  
- **Git & GitHub** – version control  
- **Markdown** – documentation  

---

## 🔍 Analytical Approach

### 1. Exploratory Data Analysis
- Reviewed structure, missingness, and distributions  
- Verified encounter timelines  
- Assessed department and visit type patterns  

### 2. Operational SQL Analysis
- **Patient Volume Trends:** steady monthly volume with year‑over‑year growth  
- **Visit Types:** balanced distribution with Emergency slightly leading  
- **Wait Times:** consistently elevated across departments  
- **Service Efficiency:** a notable share of patients wait beyond 30 minutes  
- **Hourly Patterns:** mild peaks but no extreme surges  
- **Department‑Hour Bottlenecks:** delays cluster at specific intersections  
- **Satisfaction Scores:** generally low and consistent across departments  
- **Admission Rates:** similar across departments (~48–51%)  
- **Wait Time vs Admission:** longer waits correlate but do not drive admissions  
- **Shift Analysis:** night shift physicians handle disproportionately higher loads  


---
## Dashboard - Tableau

---

## 💡 Key Insights
- High wait times are a system‑wide issue rather than isolated to one department  
- Operational strain is driven by specific department‑hour combinations  
- Emergency visits form the largest and most unpredictable segment  
- Staffing patterns do not fully align with patient arrival patterns  
- Patient satisfaction is consistently low, suggesting experience gaps  

---

## 🚀 Recommendations
- **Reduce wait times** by optimizing triage and intake workflows  
- **Target bottlenecks** at specific department‑hour intersections  
- **Rebalance staffing** to match real demand patterns  
- **Improve processes before expanding capacity** to avoid unnecessary resource costs  


---

## 📬 Contact
**Josephine Lawal**
Data Operation analyst
https://github.com/JosephineLawal1
For collaboration or questions, feel free to reach out.
