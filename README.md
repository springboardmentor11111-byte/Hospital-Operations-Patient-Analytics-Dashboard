# MedTrack DV — Hospital Operations & Patient Analytics Dashboard

A 4-page Power BI dashboard suite for hospital administrators — admissions, patient flow,
department efficiency, and resource utilization, built on 61,619 patient admission records.

## Repository Structure

```
MedTrack_DV/
├── scripts/
│   ├── hospital_cleaning.ipynb
│   └── hospital_cleaning_extended.ipynb
├── data/
│   ├── raw/
│   │   ├── hospital_raw_data.csv
│   │   └── hospital_department_resources_raw.csv
│   └── cleaned/
│       ├── hospital_admissions_dataset.csv
│       ├── hospital_department_resources.csv
│       └── hospital_cleaned_extended.csv
├── dashboard/
│   ├── MedTrack_DV.pbix
│   ├── MedTrack_DV_Theme_HighContrast.json
│   └── assets/
│       ├── medtrack_dv_logo_full.png
│       ├── medtrack_dv_logo_badge_dark.png
│       ├── medtrack_dv_logo_badge_light.png
│       ├── kpi_icon_total_admissions.png
│       ├── kpi_icon_occupancy_rate.png
│       ├── kpi_icon_avg_length_of_stay.png
│       ├── kpi_icon_readmission_rate.png
│       ├── kpi_icon_bed_utilization_rate.png
│       └── kpi_icon_discharge_count.png
├── docs/
│   ├── MedTrack_DV_Build_Guide.md
│   ├── MedTrack_DV_Presentation.pptx
│   ├── MedTrack_DV_Live_Demo_Script.md
│   └── QA_Checklist.md
└── README.md
```

## What goes where, and why

### `/scripts` — the cleaning pipeline
- **`hospital_cleaning.ipynb`** — cleans the original raw admissions export (fixes mixed
  date formats, inconsistent text casing, mixed boolean encodings, duplicate rows).
- **`hospital_cleaning_extended.ipynb`** — the full pipeline: cleans admissions **and**
  the staffing/equipment resource data, then merges both into the final analysis-ready
  dataset. This is the one to point to if asked "show me your data cleaning process."

### `/data` — every dataset, raw and cleaned, kept separate
- **`raw/`** — the messy source files, kept exactly as "received" (with mixed formats,
  typos, duplicates) so the cleaning notebooks have something real to run against.
- **`cleaned/`** — the outputs. `hospital_cleaned_extended.csv` is the one that actually
  feeds the dashboard (it has the merged Staff_Count/Equipment_Count columns); the other
  two are intermediate/reference outputs.

### `/dashboard` — the Power BI deliverable itself
- **`MedTrack_DV.pbix`** — save your Power BI file here with this name before committing.
- **`MedTrack_DV_Theme_HighContrast.json`** — the custom dark theme, so anyone rebuilding
  the report gets the exact same color palette without you having to redo it.
- **`assets/`** — every logo and icon used inside the report.

### `/docs` — everything for presenting and reviewing the project
- **Build Guide** — the field-mapping and DAX-measure reference.
- **Presentation** — your PPT for the panel overview.
- **Live Demo Script** — narration for the live walkthrough.
- **QA Checklist** — see below, worth adding since your milestone doc explicitly asks for one.

## Setup / Reproduction Steps
1. Open `dashboard/MedTrack_DV.pbix` in Power BI Desktop.
2. If reconnecting the data source: point it at `data/cleaned/hospital_cleaned_extended.csv`.
3. To regenerate the cleaned data from scratch: open `scripts/hospital_cleaning_extended.ipynb`
   in Google Colab, upload the two files from `data/raw/`, and run all cells.

## Tools Used
Power BI Desktop · DAX · Power Query (M) · Python (pandas) · Google Colab
