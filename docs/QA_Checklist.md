# MedTrack DV — QA Checklist

Use this to verify the dashboard before final submission. Check each box only after you've
actually clicked/tested it — don't assume.

## Data Integrity
- [ ] `hospital_cleaned_extended.csv` loads into Power BI with no import errors
- [ ] Row count matches expectation: 61,619 rows
- [ ] No unexpected blank/null cells in key columns (Hospital, Department, Admission_Date)
- [ ] `Month_Name` sorts Jan → Dec, not alphabetically, in every chart that uses it

## KPI Accuracy
- [ ] Total Admissions on Hospital Overview matches `COUNTROWS` of the full table when all filters are "All"
- [ ] Occupancy Rate, Readmission Rate, and Bed Utilization Rate are formatted as **percentages**, not raw decimals
- [ ] Total Bed Capacity is formatted as a **whole number**, not a percentage
- [ ] Every KPI on Department Analytics' summary table matches the equivalent chart on the same page

## Filters & Interactivity
- [ ] All 4 slicers (Admission_Date, Hospital, Department, Region) default to "All" on every page — no slicer left stuck on a single value
- [ ] Selecting a filter on one page updates every visual on that page
- [ ] Slicers are synced across all 4 pages (View → Sync slicers), or intentionally not synced if that's a deliberate design choice
- [ ] Clearing all filters returns every KPI to its full-dataset value

## Navigation
- [ ] Every sidebar button (Hospital Overview / Patient Flow / Department Analytics / Resource Utilization) navigates to the correct page
- [ ] Default page tabs are hidden (View → Page navigator off) so only the custom sidebar controls navigation

## Visual Design
- [ ] All chart titles are accurate — no leftover "by Month_Name and Month_Num" duplicate-axis titles
- [ ] Axis labels, legends, and slicer dropdown text are all legible against the dark background
- [ ] Theme colors are consistent across all 4 pages

## Known Limitations (document, don't hide)
- [ ] Staffing and Equipment data are synthetic, generated with a documented ratio rule — not real hospital records
- [ ] The full dataset is synthetic (no real hospital data was used), generated to match a reference dashboard's structure
- [ ] Equipment Utilization % reuses the same occupancy-style formula as Bed Utilization — a simplifying assumption, not a precise clinical metric

## Final Sign-off
- [ ] Opened the `.pbix` file on a second device (or had someone else open it) to confirm it works outside your own machine
- [ ] All numbers in the PPT/presentation match what the live dashboard currently shows
