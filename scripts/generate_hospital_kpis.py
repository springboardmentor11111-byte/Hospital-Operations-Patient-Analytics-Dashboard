import pandas as pd
import os

# -----------------------------
# Load cleaned dataset
# -----------------------------
input_file = "data/processed/hospital_cleaned.csv"
output_file = "data/hospital_final_dataset.xlsx"

df = pd.read_csv(input_file)

print("=" * 50)
print("MEDTRACK DV - HOSPITAL KPI ENGINEERING")
print("=" * 50)

# -----------------------------
# KPI 1: Total Admissions
# -----------------------------
total_admissions = len(df)

# -----------------------------
# KPI 2: Occupancy Rate
# -----------------------------
occupancy_rate = (
    df["Occupied_Beds"].sum() /
    df["Total_Beds"].sum()
) * 100

# -----------------------------
# KPI 3: Average Length of Stay
# -----------------------------
average_los = df["Length_of_Stay"].mean()

# -----------------------------
# KPI 4: Readmission Rate
# -----------------------------
readmission_rate = (
    (df["Readmitted"] == "Yes").sum() /
    total_admissions
) * 100
# -----------------------------
# KPI 5: Bed Utilization Rate
# -----------------------------
bed_utilization = (
    df["Occupied_Beds"].mean() /
    df["Total_Beds"].mean()
) * 100

# -----------------------------
# KPI 6: Department Efficiency
# -----------------------------
department_efficiency = (
    df.groupby("Department")["Length_of_Stay"]
      .mean()
      .reset_index()
)

department_efficiency.columns = [
    "Department",
    "Average_Length_of_Stay"
]

# -----------------------------
# Save Final Dataset
# -----------------------------
os.makedirs("data", exist_ok=True)

with pd.ExcelWriter(output_file, engine="openpyxl") as writer:

    df.to_excel(
        writer,
        sheet_name="Hospital_Data",
        index=False
    )

    pd.DataFrame({
        "KPI": [
            "Total Admissions",
            "Occupancy Rate (%)",
            "Average Length of Stay",
            "Readmission Rate (%)",
            "Bed Utilization Rate (%)"
        ],
        "Value": [
            total_admissions,
            round(occupancy_rate, 2),
            round(average_los, 2),
            round(readmission_rate, 2),
            round(bed_utilization, 2)
        ]
    }).to_excel(
        writer,
        sheet_name="Hospital_KPIs",
        index=False
    )

    department_efficiency.to_excel(
        writer,
        sheet_name="Department_Efficiency",
        index=False
    )

print("\nHospital KPIs")
print("-" * 40)
print(f"Total Admissions       : {total_admissions}")
print(f"Occupancy Rate         : {occupancy_rate:.2f}%")
print(f"Average Length of Stay : {average_los:.2f}")
print(f"Readmission Rate       : {readmission_rate:.2f}%")
print(f"Bed Utilization Rate   : {bed_utilization:.2f}%")

print("\nExcel file created successfully!")
print(output_file)