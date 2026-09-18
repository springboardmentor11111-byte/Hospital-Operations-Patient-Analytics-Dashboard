# KPI Definitions

## MedTrack DV – Hospital Operations & Patient Analytics Dashboard

This document defines the key performance indicators (KPIs) used in the MedTrack DV Power BI dashboards.

The KPIs are used to analyze hospital admissions, patient stay, revenue, discharges, and hospital resources.

---

## 1. Total Admissions

### Definition

Total Admissions represents the total number of unique hospital admissions recorded in the hospital data.

### DAX Formula

```DAX
Total Admissions =
DISTINCTCOUNT(Hospital[Admission_ID])Used In
Hospital Overview
Department Analytics
## 2. Average Length of Stay
Definition

Average Length of Stay represents the average number of days patients stayed in the hospital.

Calculation

The average is calculated using the Length_of_Stay field.

Used In
Hospital Overview
Department Analytics
3. Occupancy Rate
Definition

Occupancy Rate represents the percentage of hospital bed capacity being utilized.

Purpose

It is used to understand the level of hospital bed utilization.

Used In
Hospital Overview
Department Analytics
4. Total Revenue
Definition

Total Revenue represents the total amount recorded in the hospital billing data.

DAX Formula
Total Revenue =
SUM(Hospital[Total])
Used In
Hospital Overview
Department Analytics
5. Total Discharges
Definition

Total Discharges represents the number of patients with a recorded discharge date.

DAX Formula
Total Discharges =
COUNT(Hospital[Discharge_Date])
Used In
Patient Flow
6. Long Stay %
Definition

Long Stay % represents the percentage of patients whose length of stay falls into the Long Stay category.

Stay Categories

The Length_of_Stay value is categorized as follows:

Category	Length of Stay
Short	1–3 days
Medium	4–7 days
Long	More than 7 days
Purpose

This KPI helps identify the proportion of patients with longer hospital stays.

Used In
Patient Flow
7. Total Beds
Definition

Total Beds represents the total number of hospital beds available in the resource data.

Purpose

It provides an overall view of the hospital's bed capacity.

Used In
Resource Utilization
8. Occupied Beds
Definition

Occupied Beds represents the number of beds marked as occupied in the available resource data.

Purpose

It helps understand the number of beds currently being utilized.

Used In
Resource Utilization
9. Available Beds
Definition

Available Beds represents the number of beds marked as available in the resource data.

Purpose

It helps understand the number of beds available for use.

Used In
Resource Utilization
Feature Used for Stay Analysis
Stay Category

The Stay Category was created from the Length_of_Stay field to group patients according to their duration of hospital stay.

Categories
Short: 1–3 days
Medium: 4–7 days
Long: More than 7 days
Purpose

The category is used in the Patient Flow and Department Analytics dashboards to understand patient stay patterns.

KPI Summary
KPI	Purpose	Dashboard
Total Admissions	Measures unique hospital admissions	Hospital Overview, Department Analytics
Average Length of Stay	Measures average patient stay duration	Hospital Overview, Department Analytics
Occupancy Rate	Measures hospital bed utilization	Hospital Overview, Department Analytics
Total Revenue	Measures total recorded billing revenue	Hospital Overview, Department Analytics
Total Discharges	Measures recorded patient discharges	Patient Flow
Long Stay %	Measures percentage of long-stay patients	Patient Flow
Total Beds	Measures total bed capacity	Resource Utilization
Occupied Beds	Measures occupied beds	Resource Utilization
Available Beds	Measures available beds	Resource Utilization
DAX Measures Used
Total Admissions
Total Admissions =
DISTINCTCOUNT(Hospital[Admission_ID])
Total Revenue
Total Revenue =
SUM(Hospital[Total])
Total Discharges
Total Discharges =
COUNT(Hospital[Discharge_Date])
Purpose of KPIs

The KPIs provide a quick summary of important hospital metrics and allow users to monitor:

Patient admissions
Patient discharges
Patient stay duration
Hospital occupancy
Revenue
Bed availability
Bed utilization

These KPIs are combined with charts, filters, and slicers in Power BI to support interactive hospital data analysis.
