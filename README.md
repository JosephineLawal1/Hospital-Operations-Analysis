
# Care Continuity & Provider Workload Analysis  
### Operational Analytics Project Using Patient Encounter Data  
**Author:** Josephine  
**Role:** Healthcare Data Analyst  
**Last Updated:** June 2026  

---

## 📌 Project Overview

This project analyzes **provider workload**, **care continuity**, and **operational efficiency** using a patient encounter dataset.  
The goal is to identify:

- Workload imbalances across providers  
- Fragmented care patterns  
- Misalignment between staffing and patient demand  
- High-utilizer patient groups  
- Operational bottlenecks affecting throughput and patient experience  

This project demonstrates real-world healthcare analytics skills including SQL, Python, data modeling, operational KPIs, and dashboard design.

---

## 🏥 Business Problem

Hospitals struggle with:

- Uneven provider workloads  
- Long wait times during peak hours  
- Poor continuity of care  
- Inefficient scheduling  
- High-utilizer patients driving disproportionate demand  

This project provides a **data-driven framework** to optimize staffing, improve continuity, and enhance operational performance.

---

## 🎯 Objectives

1. **Measure provider workload**  
   - Encounters per provider  
   - Encounter duration  
   - Utilization index  
   - Peak workload hours  

2. **Evaluate continuity of care**  
   - UPC (Usual Provider Continuity)  
   - Number of unique providers per patient  
   - Fragmentation patterns  

3. **Analyze operational flow**  
   - Encounter volume by hour/day  
   - Staffing vs. demand alignment  
   - Wait-time proxies  

4. **Identify high-utilizer patients**  
   - Encounter frequency  
   - Care fragmentation  
   - Provider assignment patterns  

---

## 📂 Repository Structure

care-continuity-provider-workload/
│
├── data/
│   └── patient_encounters.csv
│
├── notebooks/
│   ├── 01_data_cleaning.ipynb
│   ├── 02_provider_workload_analysis.ipynb
│   ├── 03_continuity_of_care.ipynb
│   ├── 04_operational_insights.ipynb
│   └── 05_dashboard_dataset.ipynb
│
├── sql/
│   ├── provider_workload.sql
│   ├── continuity_of_care.sql
│   ├── encounter_volume.sql
│   └── high_utilizers.sql
│
├── dashboard/
│   ├── powerbi_wireframe.txt
│   └── tableau_wireframe.txt
│
├── reports/
│   ├── Care_Continuity_Operational_Report.md
│   └── Executive_Summary.md
│
└── src/
├── utils.py
├── preprocessing.py
├── workload_metrics.py
├── continuity_metrics.py
└── visualization.p


---

## 🧠 Key Metrics

### **Provider Workload**
- Encounters per provider  
- Average encounter duration  
- Utilization index  
- Workload distribution (Pareto analysis)  

### **Continuity of Care**
- UPC (Usual Provider Continuity)  
- Unique providers per patient  
- Continuity score distribution  

### **Operational Flow**
- Encounter volume by hour/day  
- Staffing vs. demand mismatch  
- Wait-time proxy metrics  

### **High-Utilizer Identification**
- ≥4 encounters in 90 days  
- Provider consistency  
- Encounter clustering  

---

## 🛠️ Tools & Technologies

- **Python:** pandas, numpy, matplotlib, seaborn  
- **SQL:** Window functions, aggregations, time-based analysis  
- **Power BI / Tableau:** Dashboard design  
- **Jupyter Notebooks:** Reproducible analysis  
- **GitHub:** Version control & documentation  

---

## 📊 Dashboard (Power BI / Tableau)

The dashboard includes:

- Provider workload heatmap  
- Encounter volume by hour/day  
- Continuity of care score distribution  
- High-utilizer patient tracker  
- Staffing vs. demand alignment chart  

Wireframes are included in the `dashboard/` folder.

---

## 📈 Example SQL Queries

### Provider Workload
```sql
SELECT 
    provider_id,
    COUNT(*) AS encounter_count,
    AVG(DATEDIFF(minute, start_time, end_time)) AS avg_encounter_duration
FROM encounters
GROUP BY provider_id; 
```
## 📊 Example SQL: Continuity of Care (UPC Score)

```sql
WITH provider_counts AS (
    SELECT 
        patient_id,
        doctor_id,
        COUNT(*) AS encounters_with_provider
    FROM encounters
    GROUP BY patient_id, doctor_id
),
totals AS (
    SELECT 
        patient_id,
        SUM(encounters_with_provider) AS total_encounters,
        MAX(encounters_with_provider) AS max_provider_encounters
    FROM provider_counts
    GROUP BY patient_id
)
SELECT 
    patient_id,
    CAST(max_provider_encounters AS FLOAT) / total_encounters AS continuity_score
FROM totals;
```
---

## 📄 Reports

The reports/ folder includes:
   - 4‑page operational business report
   - Executive summary
   - Recommendations for leadership
---

## 🚀 How to Run the Project

1. Clone the repository
2. Place the patient encounter dataset in data/
3. Run notebooks in order:
   - 01_data_cleaning.ipynb
   - 02_provider_workload_analysis.ipynb
   - 03_continuity_of_care.ipynb
   - 04_operational_insights.ipynb
4. Generate dashboard dataset using 05_dashboard_dataset.ipynb
5. Build dashboard in Power BI or Tableau

---

📬 Contact
For questions or collaboration:
Josephine — Healthcare Data Analyst  
San Antonio, TX

<p align="left">
  <img src="https://img.shields.io/badge/Python-3.8+-blue?logo=python&logoColor=white" alt="Python Badge"/>
  <img src="https://img.shields.io/badge/SQL-Analytics%20SQL-orange?logo=postgresql&logoColor=white" alt="SQL Badge"/>
  <img src="https://img.shields.io/badge/Power%20BI-Dashboards-F2C811?logo=powerbi&logoColor=black" alt="Power BI Badge"/>
  <img src="https://img.shields.io/badge/Tableau-Visualization-005F9E?logo=tableau&logoColor=white" alt="Tableau Badge"/>
  <img src="https://img.shields.io/badge/Healthcare%20Analytics-Operational%20Insights-brightgreen" alt="Healthcare Analytics Badge"/>
</p>
