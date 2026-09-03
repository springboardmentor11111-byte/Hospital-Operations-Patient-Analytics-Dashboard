# MedTrack DV — Power BI Build Guide

Your project brief was written for **Tableau** (it says `.twbx`), but you're building this in
**Power BI** — every concept maps over directly, just with different tool names. This guide
gets you from the dataset to the 4-page dashboard shown in your screenshot.

## 0. About the dataset

You didn't have a hospital dataset on hand, so I **generated a realistic synthetic one**
(`hospital_admissions_dataset.csv`, 30,070 rows) shaped to match your screenshot's structure —
same 5 hospitals, 7 departments, 4 patient types, 6 regions, and a full year of 2024 admissions
with a similar monthly admissions curve. Be upfront about this if this is graded: it's not a
real public dataset, it's simulated to have realistic distributions and to plug directly into
every KPI and chart your brief calls for.

**If you'd rather use real data**, search Kaggle for "Hospital Patient Records" or "Healthcare
Dataset" — just make sure whatever you find has: an admission date, a discharge date, a
hospital/department, and a bed-capacity number per hospital. Everything below still applies,
you'd just swap the source file.

| Column | What it is |
|---|---|
| `Admission_ID`, `Patient_ID` | Row/patient identifiers |
| `Admission_Date`, `Discharge_Date` | Used for LOS, monthly trends, occupancy |
| `Hospital` | 5 hospitals (for the "Top 5 by Occupancy" table) |
| `Department` | 7 departments (General Medicine, Surgery, Pediatrics, Orthopedics, Cardiology, Emergency, ICU) |
| `Region` | 6 world regions (for the map visual) |
| `Patient_Type` | Inpatient / Outpatient / Emergency / Day Care |
| `Length_of_Stay_Days` | Discharge − Admission, used for Avg LOS and occupancy |
| `Readmitted_30Days` | True/False flag, drives Readmission Rate |
| `Total_Beds` | Bed capacity per hospital (constant per hospital, used for occupancy/utilization) |
| `Year`, `Month_Num`, `Month_Name` | For the monthly trend charts |

---

## 1. Load the data & apply the theme

1. **Get Data → Text/CSV** → `hospital_admissions_dataset.csv` → **Transform Data**
2. Fix types: `Admission_Date`/`Discharge_Date` → Date; `Length_of_Stay_Days`/`Total_Beds`/`Year`/`Month_Num` → Whole Number; `Readmitted_30Days` → True/False; everything else → Text
3. Model view → select `Month_Name` → **Column tools → Sort by column → Month_Num** (same fix as your last project)
4. **View → Themes → Browse for themes** → `MedTrack_DV_Theme.json`

---

## 2. DAX measures

```dax
Total Admissions = COUNTROWS(hospital_admissions_dataset)

Total Patient Days = SUM(hospital_admissions_dataset[Length_of_Stay_Days])

Total Bed Capacity = SUMX(DISTINCT(hospital_admissions_dataset[Hospital]), CALCULATE(MAX(hospital_admissions_dataset[Total_Beds])))

Days In Period = DATEDIFF(MIN(hospital_admissions_dataset[Admission_Date]), MAX(hospital_admissions_dataset[Admission_Date]), DAY) + 1

Occupancy Rate = DIVIDE([Total Patient Days], [Total Bed Capacity] * [Days In Period], 0)

Avg Length of Stay = AVERAGE(hospital_admissions_dataset[Length_of_Stay_Days])

Readmissions = CALCULATE([Total Admissions], hospital_admissions_dataset[Readmitted_30Days] = TRUE)

Readmission Rate = DIVIDE([Readmissions], [Total Admissions], 0)

Bed Utilization Rate = [Occupancy Rate]

Discharge Count = CALCULATE([Total Admissions], hospital_admissions_dataset[Discharge_Date] <= MAX(hospital_admissions_dataset[Discharge_Date]))
```

**Honest notes on 2 of these, worth knowing if asked:**
- `Bed Utilization Rate` is set equal to `Occupancy Rate` — in most real hospital reporting these are calculated differently (utilization often includes staffed-vs-unstaffed beds), but this dataset doesn't have that distinction, so I didn't fabricate a fake split.
- `Discharge Count` will read very close to `Total Admissions` because every record in this synthetic set already has a discharge date (no "still admitted" patients). Flag this the same way.

Format `Occupancy Rate`, `Readmission Rate`, `Bed Utilization Rate` as **percentage**. Format `Total Admissions`, `Discharge Count` with **thousands separator**.

---

## 3. Page-by-page build

### Page 1 — Hospital Overview
- **6 KPI cards**: `Total Admissions`, `Occupancy Rate`, `Avg Length of Stay`, `Readmission Rate`, `Bed Utilization Rate`, `Discharge Count`
- **Admissions Trend (Monthly)**: Line chart → Axis `Month_Name` (sorted) → Value `Total Admissions`
- **Occupancy Rate Trend (Monthly)**: Line chart → Axis `Month_Name` → Value `Occupancy Rate`
- **Readmission Rate Trend (Monthly)**: Line chart → Axis `Month_Name` → Value `Readmission Rate`
- **Admissions by Patient Type**: Donut chart → Legend `Patient_Type` → Values `Total Admissions`
- **Admissions by Department**: Bar chart → Axis `Department` → Values `Total Admissions`
- **Avg Length of Stay by Department**: Bar chart → Axis `Department` → Values `Avg Length of Stay`
- **Readmission Rate by Department**: Bar chart → Axis `Department` → Values `Readmission Rate`
- **Admissions by Region**: **Filled Map** or **Shape Map** → Location `Region` → Values `Total Admissions`
- **Monthly Admissions vs Discharges**: Clustered column → Axis `Month_Name` → Values `Total Admissions`, `Discharge Count`
- **Top 5 Hospitals by Occupancy Rate**: Table or bar chart → Axis `Hospital` → Values `Occupancy Rate`, sorted descending, **Top N filter = 5**

### Page 2 — Patient Flow
- Admission trends (reuse Admissions Trend chart, different framing)
- Discharge tracking: Line/area chart → Axis `Month_Name` → Value `Discharge Count`
- Patient movement analysis: Sankey-style or stacked bar → `Patient_Type` by `Department`
- Average stay analysis: reuse Avg LOS by Department, add a card for overall `Avg Length of Stay`
- Peak patient load monitoring: Line chart with a **reference line** at average → Axis `Month_Name` → Value `Total Admissions`

### Page 3 — Department Analytics
- Department performance analysis: Table with `Department`, `Total Admissions`, `Avg Length of Stay`, `Readmission Rate` side by side
- Patient volume by department: Column chart (reuse)
- Readmission by department: Bar chart (reuse)
- Department efficiency comparison: Scatter chart → X `Avg Length of Stay`, Y `Readmission Rate`, size `Total Admissions`, category `Department` — this is the one genuinely new visual on this page and a good "insight" chart
- Treatment capacity analysis: Bar chart → Axis `Department` → Values `Total Patient Days` vs a bed-capacity reference line

### Page 4 — Resource Utilization
- Bed utilization analysis: Gauge → Value `Bed Utilization Rate`, Max 1
- Staff allocation monitoring: **not available in this dataset** — there's no staffing column. Either omit this visual or add a synthetic `Staff_Count` column if your instructor specifically requires it (tell me and I'll add one with a documented rule)
- Equipment utilization tracking: same limitation — no equipment data exists in hospital admission records; flag this as a scope note in your documentation deliverable
- Capacity planning insights: Bar chart → Axis `Hospital` → Values `Occupancy Rate` vs `Total Bed Capacity`
- Resource availability analysis: Card/table → `Total Bed Capacity` − `Total Patient Days`-derived beds-in-use, by hospital

---

## 4. Matching the visual style

| Element | Hex |
|---|---|
| Page background | `#020914` |
| Card background | `#07161F` |
| Sidebar | `#020914` |
| Teal (primary KPI icons) | `#308F96` |
| Green (positive trend) | `#69A349` |
| Pink/red (readmission, negative) | `#C0447A` |
| Blue (bed utilization) | `#4C6FBF` |
| Orange (discharge) | `#D98E3C` |

- Sidebar nav ("1. Hospital Overview", "2. Patient Flow", "3. Department Analytics", "4. Resource Utilization") — same button + bookmark technique as your freelancer dashboard
- KPI cards: colored circular icon on the left of each card (Insert → Icons, or a colored circle shape + a Unicode/PNG icon), number + label to the right, small up/down arrow with % vs prior year in green/red — that arrow isn't a native card feature, so it's a text box with conditional formatting via a measure comparing this period to the prior year (`CALCULATE([Total Admissions], SAMEPERIODLASTYEAR(...))`)
- Top filter bar: 4 slicers — `Date Range` (use a date slicer, "between"), `Hospital`, `Department`, `Region`

---

## 5. Deliverables mapping (for your milestone documentation)

Your brief lists Tableau-specific deliverable names. Here's the Power BI equivalent for each:

| Brief asks for | Power BI equivalent |
|---|---|
| `hospital_raw_data.csv` | `hospital_admissions_dataset.csv` (provided) |
| `data_collection.py` | The Python generation script (ask if you want this file too) |
| `hospital_cleaned.csv` | Same file — already clean, 0 missing values |
| `hospital_cleaning.ipynb` | Optional — can provide a short notebook documenting the (synthetic) cleaning steps if your milestone requires the artifact |
| `hospital_final_dataset.xlsx` | Export the Power BI model's fact table, or save the CSV as .xlsx |
| `generate_hospital_kpis.py` | The DAX measures in section 2 above, screenshotted from Power BI |
| `dashboard_storyboard.pdf` | The 4 mockups I can generate (like the freelancer project) before you build |
| `medtrack_prototype.twbx` / `MedTrack_DV.twbx` | Your final `.pbix` file |
| QA Checklist / Testing Report | A short doc validating each KPI number against a manual filter — ask and I'll draft a template |

---

Want me to generate the visual mockups for these 4 pages next (like I did for the freelancer dashboard), or go straight into building Page 1 in Power BI?
