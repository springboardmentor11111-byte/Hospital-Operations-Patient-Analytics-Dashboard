# KPI Definitions

## Project

**MedTrack DV – Hospital Operations & Patient Analytics Dashboard**

## Objective

The purpose of this document is to define the key performance indicators used in the Power BI dashboards.

## KPIs Used

### 1. Total Admissions

**Definition:**
Shows the total number of unique hospital admissions.

**DAX Formula:**

```DAX
Total Admissions =
DISTINCTCOUNT(Hospital[Admission_ID])
```

**Used In:**

* Hospital Overview
* Department Analytics

### 2. Average Length of Stay

**Definition:**
Shows the average number of days patients stayed in the hospital.

**Used In:**

* Hospital Overview
* Department Analytics

### 3. Occupancy Rate

**Definition:**
Shows the percentage of hospital bed capacity being utilized.

**Used In:**

* Hospital Overview
* Department Analytics

### 4. Total Revenue

**Definition:**
Shows the total billing amount recorded in the hospital data.

**DAX Formula:**

```DAX
Total Revenue =
SUM(Hospital[Total])
```

**Used In:**

* Hospital Overview
* Department Analytics

### 5. Total Discharges

**Definition:**
Shows the number of records with a recorded discharge date.

**DAX Formula:**

```DAX
Total Discharges =
COUNT(Hospital[Discharge_Date])
```

**Used In:**

* Patient Flow

### 6. Long Stay %

**Definition:**
Shows the percentage of patients classified as having a long hospital stay.

**Stay Categories:**

* **Short:** 1–3 days
* **Medium:** 4–7 days
* **Long:** More than 7 days

**Used In:**

* Patient Flow

### 7. Total Beds

**Definition:**
Shows the total number of hospital beds included in the resource data.

**Used In:**

* Resource Utilization

### 8. Occupied Beds

**Definition:**
Shows the number of hospital beds marked as occupied.

**Used In:**

* Resource Utilization

### 9. Available Beds

**Definition:**
Shows the number of hospital beds marked as available.

**Used In:**

* Resource Utilization

## KPI Summary

| KPI                    | Dashboard                               |
| ---------------------- | --------------------------------------- |
| Total Admissions       | Hospital Overview, Department Analytics |
| Average Length of Stay | Hospital Overview, Department Analytics |
| Occupancy Rate         | Hospital Overview, Department Analytics |
| Total Revenue          | Hospital Overview, Department Analytics |
| Total Discharges       | Patient Flow                            |
| Long Stay %            | Patient Flow                            |
| Total Beds             | Resource Utilization                    |
| Occupied Beds          | Resource Utilization                    |
| Available Beds         | Resource Utilization                    |

## Conclusion

These KPIs provide a quick overview of hospital admissions, patient stay, revenue, patient discharges, and bed utilization. They are presented through Power BI KPI cards and supported by interactive charts, filters, and slicers.
