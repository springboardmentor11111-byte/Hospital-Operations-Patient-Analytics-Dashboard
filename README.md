# MedTrack DV – Hospital Operations & Patient Analytics Dashboard

> **A Tableau-based healthcare analytics dashboard for monitoring hospital operations, patient flow, department performance, and resource utilization.**

---

## 📌 Project Overview

**MedTrack DV** is a hospital operations and patient analytics project developed to transform hospital data into meaningful, interactive visual insights.

The project follows an end-to-end data analytics workflow:

**Data Collection → Data Cleaning → KPI Engineering → Dashboard Planning → Tableau Development → Testing & Validation**

The final solution provides interactive dashboards that help analyze hospital admissions, discharges, patient flow, department performance, and resource utilization.

---

## 🎯 Objectives

The primary objectives of the MedTrack DV project are to:

* Collect and prepare hospital operational data.
* Clean and validate the dataset for analysis.
* Engineer meaningful healthcare KPIs.
* Design an effective dashboard structure.
* Develop interactive Tableau dashboards.
* Analyze patient flow and hospital operations.
* Provide department-level insights.
* Monitor resource utilization.
* Validate dashboard accuracy and functionality.

---

## 🛠️ Technologies Used

| Technology           | Purpose                                 |
| -------------------- | --------------------------------------- |
| **Python**           | Data processing and KPI engineering     |
| **Pandas**           | Data cleaning and transformation        |
| **Jupyter Notebook** | Data analysis and preprocessing         |
| **Microsoft Excel**  | Dataset storage and validation          |
| **Tableau**          | Dashboard development and visualization |
| **Git & GitHub**     | Version control and project management  |
| **Markdown**         | Project documentation                   |

---

# 📊 Project Milestones

## Milestone 1 – Data Collection & Preparation

### Completed Activities

* Collected and organized the hospital dataset.
* Added the raw hospital dataset.
* Cleaned and transformed the data.
* Handled missing and inconsistent values.
* Prepared the final dataset for visualization.
* Created data collection and cleaning scripts.
* Validated the prepared dataset.

### Deliverables

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

# Milestone 2 – KPI Engineering & Dashboard Planning

## KPI Engineering

Hospital operational KPIs were defined and prepared for dashboard implementation.

### Key Performance Indicators

| KPI                        | Description                                                 |
| -------------------------- | ----------------------------------------------------------- |
| **Total Admissions**       | Total number of patient admissions                          |
| **Total Discharges**       | Total number of patients discharged                         |
| **Occupancy Rate**         | Percentage of available hospital capacity utilized          |
| **Average Length of Stay** | Average duration of patient hospitalization                 |
| **Readmission Rate**       | Percentage of patients readmitted within the defined period |

### Dashboard Planning

The dashboard structure was planned using:

* Dashboard storyboard
* KPI documentation
* Wireframe/prototype
* Visualization planning
* User interaction planning

### Deliverables

```text
milestone_2/
├── medtrack_prototype.twbx
├── dashboard_storyboard.pdf
└── KPI_documentation.md
```

---

# Milestone 3 – Dashboard Development

The final Tableau dashboards were developed based on the KPI requirements and dashboard prototype.

## 📈 Developed Dashboards

### 1. Hospital Overview

Provides a high-level view of hospital performance through:

* KPI cards
* Admissions
* Discharges
* Occupancy
* Average Length of Stay
* Readmission analysis
* Interactive filters

### 2. Patient Flow

Focuses on patient movement and hospital activity.

Includes:

* Admission trends
* Discharge trends
* Patient flow analysis
* Time-based trends
* Interactive filtering

### 3. Department Analytics

Provides department-level analysis of hospital operations.

Includes:

* Department-wise admissions
* Department performance
* Patient distribution
* Comparative analysis
* Department filters

### 4. Resource Utilization

Analyzes hospital resource usage.

Includes:

* Ward-level analysis
* Resource utilization
* Occupancy trends
* Utilization comparisons
* Interactive filtering

---

## 🎨 Dashboard Features

The MedTrack DV dashboards provide:

* 📌 KPI cards
* 📊 Interactive charts
* 🔎 Dynamic filters
* 📅 Date-based filtering
* 🏥 Department filtering
* 🛏️ Ward-level filtering
* 📈 Trend analysis
* 🔄 Dashboard navigation
* 📋 Data-driven insights
* 📐 Consistent number and percentage formatting

---

# 🧪 Testing & Validation

The developed dashboards were tested to ensure accuracy, consistency, functionality, and usability.

### Testing Areas

| Test Area             | Validation                                      |
| --------------------- | ----------------------------------------------- |
| Tableau Workbook      | Workbook opens and loads correctly              |
| KPI Accuracy          | KPI values verified against source data         |
| Data Consistency      | Dashboard values match prepared dataset         |
| Date Filters          | Date filtering works correctly                  |
| Department Filters    | Department filtering works correctly            |
| Ward Filters          | Ward filtering works correctly                  |
| Dashboard Interaction | Interactive elements function correctly         |
| Navigation            | Dashboard navigation works correctly            |
| Charts                | Visualizations display correctly                |
| Formatting            | Numbers and percentages are formatted correctly |
| Layout                | Dashboard elements are properly aligned         |

### Testing Documentation

Detailed testing and validation information is available at:

```text
milestone_3/validation/dashboard_testing.md
```

---

# 📸 Dashboard Screenshots

Screenshots of the completed dashboards are available in:

```text
milestone_3/screenshots/
```

### Available Screenshots

* `hospital_overview.png`
* `patient_flow.png`
* `department_analytics.png`
* `resource_utilization.png`

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
│   │
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
│   ├── documentation/
│   │   └── milestone_3_overview.md
│   │
│   └── validation/
│       └── dashboard_testing.md
│
└── docs/
    └── Milestone_3_Dashboard_Development_DETAILED.pdf
```

---

# 🔄 Project Workflow

```text
┌──────────────────────────────┐
│ Milestone 1                  │
│ Data Collection & Cleaning   │
└──────────────┬───────────────┘
               ↓
┌──────────────────────────────┐
│ Milestone 2                  │
│ KPI Engineering & Planning  │
└──────────────┬───────────────┘
               ↓
┌──────────────────────────────┐
│ Milestone 3                  │
│ Tableau Dashboard Development│
└──────────────┬───────────────┘
               ↓
┌──────────────────────────────┐
│ Testing & Validation         │
└──────────────┬───────────────┘
               ↓
┌──────────────────────────────┐
│ Final MedTrack DV Dashboard  │
└──────────────────────────────┘
```

---

# 📦 Deliverables

The project includes the following deliverables:

### Data

* Raw hospital dataset
* Cleaned hospital dataset
* Final analysis-ready dataset

### Data Processing

* Data collection script
* Data cleaning notebook
* KPI engineering script

### Dashboard Planning

* KPI documentation
* Dashboard storyboard
* Tableau prototype

### Dashboard Development

* Final Tableau workbook
* Dashboard version 1 workbook
* Dashboard screenshots

### Documentation

* Milestone documentation
* Testing and validation documentation
* Detailed project report

---

# ✅ Project Completion Status

| Milestone                                          | Status      |
| -------------------------------------------------- | ----------- |
| Milestone 1 – Data Collection & Preparation        | ✅ Completed |
| Milestone 2 – KPI Engineering & Dashboard Planning | ✅ Completed |
| Milestone 3 – Dashboard Development                | ✅ Completed |
| Testing & Validation                               | ✅ Completed |
| Documentation                                      | ✅ Completed |
| Final Deliverables                                 | ✅ Ready     |

---

# 🚀 Final Status

**MedTrack DV – Hospital Operations & Patient Analytics Dashboard**

The project has successfully completed **Milestones 1, 2, and 3**, including data preparation, KPI engineering, dashboard planning, Tableau development, testing, and validation.

The final project is **ready for review, evaluation, and merge**.

---

## 👩‍💻 Project

**Project:** MedTrack DV – Hospital Operations & Patient Analytics Dashboard
**Domain:** Healthcare Analytics / Data Visualization
**Tools:** Python, Pandas, Jupyter Notebook, Excel, Tableau
**Platform:** GitHub

---
