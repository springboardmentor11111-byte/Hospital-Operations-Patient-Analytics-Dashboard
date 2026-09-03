# Hospital-Operations-Patient-Analytics-Dashboard

## 🎯 Project Objective

The objective of MedTrack-DV is to develop an interactive hospital analytics dashboard that helps analyze:

* Hospital admissions and discharges
* Patient flow
* Hospital performance KPIs
* Department-level analytics
* Resource utilization
* Patient and operational trends

---

# Milestone 1 — Data Collection & Data Preparation

### Description

Milestone 1 focuses on collecting, organizing, cleaning, and preparing the hospital dataset for further analysis and visualization.

### Work Completed

* Collected and organized the hospital dataset.
* Created the raw hospital dataset.
* Performed data cleaning and preprocessing.
* Handled data inconsistencies and missing values.
* Prepared the cleaned dataset for analysis.
* Created the final dataset used for KPI engineering and Tableau development.

### Files Added

```text
data/
├── hospital_raw_data.csv
├── hospital_cleaned.csv
└── hospital_final_dataset.xlsx

scripts/
├── data_collection.py
└── hospital_cleaning.ipynb
```

---

# Milestone 2 — KPI Engineering & Dashboard Planning

### Description

Milestone 2 focuses on transforming the prepared hospital data into meaningful performance indicators and creating the initial dashboard design and prototype.

### Work Completed

* Developed hospital performance KPIs.
* Created KPI calculations using Python.
* Prepared data for Tableau visualization.
* Created the initial Tableau dashboard prototype.
* Designed the dashboard storyboard.
* Documented KPI definitions and calculation methods.
* Planned the structure and visualization requirements for the final dashboards.

### Key KPIs

* Total Admissions
* Total Discharges
* Occupancy Rate
* Average Length of Stay
* Readmission Rate
* Patient Flow
* Department Performance
* Resource Utilization

### Files Added

```text
milestone_2/
├── medtrack_prototype.twbx
├── dashboard_storyboard.pdf
└── KPI_documentation.md
```

---

# Milestone 3 — Tableau Dashboard Development

### Description

Milestone 3 focuses on developing the final interactive Tableau dashboards based on the KPIs and dashboard design created during Milestone 2.

### Work Completed

* Developed the MedTrack-DV Tableau dashboard.
* Implemented KPI cards and analytical visualizations.
* Created multiple dashboard views.
* Added patient flow analysis.
* Added department-level analytics.
* Added resource utilization analysis.
* Organized dashboard screenshots and supporting documentation.
* Prepared the final Tableau workbook files.

### Dashboard Modules

**Hospital Overview**

Provides an overall view of hospital performance using key KPIs and summary visualizations.

**Patient Flow**

Analyzes admissions, discharges, and patient movement trends.

**Department Analytics**

Provides department-wise analysis of hospital operations and patient activity.

**Resource Utilization**

Provides insights into the utilization of available hospital resources.

### Files Added

```text
milestone_3/
├── dashboard/
│   ├── MedTrack_DV.twbx
│   └── medtrack_dashboard_v1.twbx
│
├── screenshots/
│   ├── hospital_overview.png
│   ├── patient_flow.png
│   ├── department_analytics.png
│   └── resource_utilization.png
│
└── documentation/
    └── milestone_3_overview.md
```

---

# 📊 Overall Development Flow

The project follows the complete development workflow:

**Data Collection**

↓

**Data Cleaning & Preparation**

↓

**KPI Engineering**

↓

**Dashboard Storyboard & Prototyping**

↓

**Tableau Dashboard Development**

↓

**Hospital Analytics & Visualization**

---

# 📁 Project Structure

```text
MedTrack-DV/
│
├── README.md
│
├── data/
│   ├── hospital_raw_data.csv
│   ├── hospital_cleaned.csv
│   └── hospital_final_dataset.xlsx
│
├── scripts/
│   ├── data_collection.py
│   ├── hospital_cleaning.ipynb
│   └── generate_hospital_kpis.py
│
├── milestone_2/
│   ├── medtrack_prototype.twbx
│   ├── dashboard_storyboard.pdf
│   └── KPI_documentation.md
│
├── milestone_3/
│   ├── dashboard/
│   │   ├── MedTrack_DV.twbx
│   │   └── medtrack_dashboard_v1.twbx
│   │
│   ├── screenshots/
│   │   ├── hospital_overview.png
│   │   ├── patient_flow.png
│   │   ├── department_analytics.png
│   │   └── resource_utilization.png
│   │
│   └── documentation/
│       └── milestone_3_overview.md
│
└── docs/
    └── Milestone_3_Dashboard_Development_DETAILED.pdf
```

---

## 🚀 Final Outcome

The completed work delivers an end-to-end **Hospital Operations & Patient Analytics Dashboard** solution, integrating data preparation, KPI engineering, dashboard planning, and interactive Tableau visualization.

The final MedTrack-DV dashboard provides a centralized view of hospital operations and patient analytics to support better understanding of hospital performance and operational trends.
