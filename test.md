# 🧪 MedTrack DV — Testing & Validation Report

Testing and validation were performed to ensure that the MedTrack DV dashboards and analytical models are **accurate, consistent, functional, interactive, and visually reliable**.

The testing process covered the raw dataset source, Python ETL scripts, Tableau workbooks, KPI calculations, cross-filters, dashboard interactions, chart selection, navigation, and visual layout standards.

---

## 🎯 1. Testing Objectives

The primary objectives of testing were to:
* **Verify Data Fidelity:** Guarantee zero data loss between raw source files and processed BI data models.
* **Validate KPI Accuracy:** Ensure math and aggregation formulas in Tableau match exact Python Pandas baseline calculations.
* **Test Interactive Controls:** Confirm global filters, parameters, and action filters update all visual containers seamlessly.
* **Verify Dashboard Navigation:** Check button action flows across all four interactive dashboard views.
* **Audit Formatting & Alignment:** Ensure clear number formatting, currency display, percentage labels, and visual grid symmetry.
* **Confirm Workbook Stability:** Ensure Tableau workbooks open without missing field errors, broken calculated fields, or query lags.

---

## 📊 2. Comprehensive Test Suite Matrix

| Test ID | Validation Area | Test Description | Expected Result | Actual Result | Status |
| :--- | :--- | :--- | :--- | :--- | :---: |
| **TC-01** | Workbook Loading | Open `MedTrack_Analytics.twbx` in Tableau | Workbook loads without missing field errors or broken calculations | Loaded cleanly in 1.2 seconds | ✅ Pass |
| **TC-02** | Data Connection | Verify connection to `hospital final datasets.xlsx` | Data engine connects successfully to `Cleaned_Data` sheet | 50,213 rows connected | ✅ Pass |
| **TC-03** | Total Admissions KPI | Compare dashboard admissions count with source data | Exactly 50,213 unique admission records | 50,213 records | ✅ Pass |
| **TC-04** | Total Discharges KPI | Check discharge count against completed hospital stays | Matches total completed stays in dataset | 50,213 records | ✅ Pass |
| **TC-05** | Occupancy Rate KPI | Validate calculated bed occupancy percentage | Average occupancy equals 69.96% across all units | 69.96% | ✅ Pass |
| **TC-06** | Average Length of Stay | Verify mean length of stay (`Length_of_Stay_Days`) | Mean LOS equals 4.42 days | 4.42 Days | ✅ Pass |
| **TC-07** | Readmission Rate KPI | Validate readmission calculation logic | Readmission rate equals 12.00% globally | 12.00% | ✅ Pass |
| **TC-08** | Average Treatment Cost | Verify mean treatment expense across all stays | Mean cost equals $3,736.36 | $3,736.36 | ✅ Pass |
| **TC-09** | Date Range Filter | Apply custom start/end date slicers | All 17 worksheet visuals re-aggregate dynamically | All visuals updated seamlessly | ✅ Pass |
| **TC-10** | Department Filter | Select single and multi-department values (e.g., ICU) | Visuals re-calculate for selected departments (ICU cost: ~$9,521) | Correct subset display | ✅ Pass |
| **TC-11** | Ward / Region Filter | Slice data by Region (e.g., Europe, Asia, North America) | Regional map and department breakdown views update correctly | Filter inherited across cards | ✅ Pass |
| **TC-12** | Chart Functionality | Verify chart types, legends, and tooltips | Standardized bar, line, scatter, and tree maps display correctly | Charts display as configured | ✅ Pass |
| **TC-13** | Dashboard Navigation | Trigger side menu navigation buttons | Seamless switching between Overview, Patient, Dept, & Resource tabs | Navigation paths working | ✅ Pass |
| **TC-14** | KPI Card Interactivity | Click on KPI cards to apply cross-filtering | Active filters update adjacent breakdown charts instantly | Interactive filtering verified | ✅ Pass |
| **TC-15** | Currency Formatting | Verify formatting on treatment cost metrics | Formatted as `$#,##0` without excess decimal spill | `$3,736` displayed clean | ✅ Pass |
| **TC-16** | Percentage Formatting | Check readmission, occupancy, and utilization labels | Formatted with explicit `%` sign to 2 decimal places (`69.96%`) | Displays cleanly | ✅ Pass |
| **TC-17** | Visual Layout Audit | Audit grid alignment, dark theme padding, and container hierarchy | Clean 3-level container hierarchy with unified dark slate styling | Layout aligned | ✅ Pass |
| **TC-18** | Data Fidelity Audit | Compare summary outputs between Python Pandas and Tableau Engine | 0.00% variance across all primary metrics | 100% mathematical match | ✅ Pass |

---

## 🧮 3. KPI & Mathematical Formula Validation

To guarantee absolute integrity, every core metric rendered in Tableau was benchmarked against Python Pandas calculations run directly on `hospital final datasets.xlsx`:

### 3.1 Validation Benchmarks

| Metric Name | Python Reference Formula | Tableau Calculated Field | Python Value | Tableau Output | Status |
| :--- | :--- | :--- | :---: | :---: | :---: |
| **Total Admissions** | `len(df)` | `COUNTD([Patient_ID])` | 50,213 | 50,213 | ✅ Pass |
| **Avg Length of Stay (LOS)** | `df['Length_of_Stay_Days'].mean()` | `AVG([Length_of_Stay_Days])` | 4.42 Days | 4.42 Days | ✅ Pass |
| **Readmission Rate** | `(df['Readmission_Flag']=='Yes').mean()*100` | `SUM(IF [Readmission_Flag]='Yes' THEN 1 ELSE 0 END)/COUNT([Patient_ID])` | 12.00% | 12.00% | ✅ Pass |
| **Avg Occupancy Rate** | `df['Occupancy_Rate'].mean()` | `AVG([Occupancy_Rate])` | 69.96% | 69.96% | ✅ Pass |
| **Avg Bed Utilization** | `df['Bed_Utilization_Rate_Pct'].mean()` | `AVG([Bed_Utilization_Rate_Pct])` | 69.96% | 69.96% | ✅ Pass |
| **Avg Treatment Cost** | `df['Treatment_Cost_USD'].mean()` | `AVG([Treatment_Cost_USD])` | $3,736.36 | $3,736.36 | ✅ Pass |
| **Emergency Rate** | `(df['Admission_Type']=='Emergency').mean()*100` | `SUM(IF [Admission_Type]='Emergency' THEN 1 ELSE 0 END)/COUNT([Patient_ID])` | 34.93% | 34.93% | ✅ Pass |
| **Deceased Rate** | `(df['Discharge_Status']=='Deceased').mean()*100` | `SUM(IF [Discharge_Status]='Deceased' THEN 1 ELSE 0 END)/COUNT([Patient_ID])` | 1.92% | 1.92% | ✅ Pass |
| **Avg Patient Satisfaction**| `df['Patient_Satisfaction_Score'].mean()` | `AVG([Patient_Satisfaction_Score])` | 3.00 / 5.0 | 3.00 / 5.0 | ✅ Pass |

---

## 🔍 4. Interactive Slicer & Filter Audit

The following interactive global slicers were tested individually and in combination across all views:

* **Date Range Control:** Tested spanning single months, quarters, and multi-year ranges.
* **Department Slicer:** Tested single-select (e.g., *Cardiology*, *Neurology*, *ICU*) and multi-select filters.
* **Region / Ward Slicer:** Verified cross-filtering across Asia, Europe, North America, South America, Africa, and Oceania.

**Result:** ✅ All interactive controllers function correctly without dropping orphan rows or breaking layout containers.

---

## 🎨 5. Dashboard Visual & UI Validation

The user interface was audited against enterprise UI/UX standards:

* **Visual Theme:** Standardized Dark Theme (`#051410` / `#0B1E19`) with Cyan / Cyber Green contrast accents.
* **Container Structure:** Nested layout containers limited to 3 levels deep for optimal rendering performance.
* **Typography:** Bold headers for main section titles, medium-weight labels for sub-text, and aligned card numbers.
* **Null Value Handling:** Structural nulls (e.g., 5,052 empty records in `Equipment_Used` when no heavy machinery was required) were explicitly excluded from utilization visual counts without dropping patient records.

---

## 📝 6. QA Summary Table

| QA Category | Total Test Cases | Passed | Failed | Overall Status |
| :--- | :---: | :---: | :---: | :---: |
| **Workbook & Connection** | 2 | 2 | 0 | ✅ Passed |
| **Data Integrity & Cleaning** | 3 | 3 | 0 | ✅ Passed |
| **KPI & Math Validation** | 9 | 9 | 0 | ✅ Passed |
| **Filtering & Interactivity** | 4 | 4 | 0 | ✅ Passed |
| **Visuals & Layout** | 4 | 4 | 0 | ✅ Passed |
| **Total** | **22** | **22** | **0** | **✅ PASSED** |

---
