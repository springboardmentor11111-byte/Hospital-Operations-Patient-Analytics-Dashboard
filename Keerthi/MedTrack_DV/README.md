# MEDTRACK DV
## Hospital Operations & Patient Analytics Dashboard

MedTrack DV is a healthcare analytics project developed using Python and Power BI to analyze hospital operations and patient-related data.

The project was completed through four milestones.

---

## Milestone 1 – Data Collection and Preparation

In Milestone 1, hospital datasets were collected, explored, cleaned, and integrated.

### Datasets Used

- Patients
- Admissions
- Doctors
- Departments
- Billing
- Surgeries
- Medications
- Laboratory Results

### Work Done

- Explored dataset structure and data types
- Checked missing values and duplicates
- Cleaned and prepared the data
- Connected datasets using common IDs
- Created a consolidated hospital master dataset
- Performed feature engineering

### Features Created

- Admission Day
- Admission Month
- Admission Month Number
- Admission Quarter
- Admission Year
- Age Group
- Weekend Admission
- Stay Category

### Final Dataset

**5,000 rows × 34 columns**

### Tools Used

- Python
- Pandas
- NumPy
- Jupyter Notebook

---

## Milestone 2 – Dashboard Development

In Milestone 2, the prepared data was used to develop interactive Power BI dashboards.

### Work Done

- Created KPI cards
- Created charts and visualizations
- Created DAX measures
- Added filters and slicers
- Added dashboard navigation

### Four Dashboards

#### 1. Hospital Overview
- Total Admissions
- Average Length of Stay
- Occupancy Rate
- Total Revenue
- Monthly Admissions
- Department and Diagnosis analysis

#### 2. Patient Flow
- Total Discharges
- Long Stay %
- Admissions vs Discharges
- Length of Stay Distribution
- Weekend vs Weekday Admissions

#### 3. Department Analytics
- Total Admissions
- Average Length of Stay
- Occupancy Rate
- Total Revenue
- Patient Volume by Department
- Revenue by Department
- Stay Profile

#### 4. Resource Utilization
- Total Beds
- Occupied Beds
- Available Beds
- Department Resource Matrix
- Doctors by Department
- Resource-related analysis

### Filters Used

- Department
- Diagnosis
- Admission Date
- Gender
- Ward
- Bed Type
- Floor

---

## Milestone 3 – Dashboard Improvement

In Milestone 3, the dashboards developed in Milestone 2 were improved.

### Improvements Made

- Improved dashboard layout and alignment
- Improved KPI card colors and formatting
- Adjusted chart sizes and placement
- Improved titles and labels
- Added additional filters where required
- Improved color consistency
- Improved readability and usability

The main focus was to make the dashboards more clear, consistent, and user-friendly.

---

## Milestone 4 – Testing and Delivery

In Milestone 4, the completed dashboards were tested and prepared for final delivery.

### Work Done

- Validated KPI calculations
- Tested dashboard filters and slicers
- Tested dashboard navigation
- Tested chart interactions
- Tested Patient Flow analytics
- Checked admissions and discharge trends
- Prepared QA Checklist
- Prepared Dashboard Testing Report
- Prepared project documentation
- Organized project files
- Prepared the project for GitHub delivery

### Documentation

The project documentation includes:

- Dataset information
- KPI definitions
- Dashboard information
- User guide
- Testing and validation

---

## Project Structure

```text
MedTrack_DV/
│
├── README.md
├── dashboard/
├── data/
│   ├── raw/
│   └── cleaned/
├── notebooks/
├── scripts/
└── docs/
