# Medical Term Lookup Tool
terms = {
    "BP": "Blood Pressure",
    "HR": "Heart Rate",
    "BMI": "Body Mass Index",
    "CNS": "Central Nervous System",
    "DM": "Diabetes Mellitus",
    "HTN": "Hypertension",
    "COPD": "Chronic Obstructive Pulmonary Disease",
    "TB": "Tuberculosis",
  "TPR": "Temperature, Pulse, Respiration",
    "O2 Sat": "Oxygen Saturation",
    "PRN": "As Needed (Pro re nata)",
    "STAT": "Immediately (Statim)",
    "Dx": "Diagnosis",
    "Tx": "Treatment",
    "Hx": "History",
    "Sx": "Symptoms",
    "SOB": "Shortness of Breath",
    "CHF": "Congestive Heart Failure",
    "MI": "Myocardial Infarction",
    "CVA": "Cerebrovascular Accident",
    "URI": "Upper Respiratory Infection",
    "ER": "Emergency Room",
    "OR": "Operating Room",
    "ICU": "Intensive Care Unit",
    "GI": "Gastrointestinal",
    "ENT": "Ear, Nose, and Throat",
    "PT": "Physical Therapy",
    "OT": "Occupational Therapy",
    "PO": "By Mouth (Per os)",
    "IV": "Intravenous",
    "IM": "Intramuscular",
    "SC": "Subcutaneous",
    "QID": "Four Times a Day (Quater in die)",
    "TID": "Three Times a Day (Ter in die)",
    "BID": "Twice a Day (Bis in die)",
    "QD": "Every Day (Quaque die)", # Note: QD is often discouraged due to confusion with QID
    "NPO": "Nothing by Mouth (Nil per os)",
    "VS": "Vital Signs"
}
abbreviation = input("Enter a medical abbreviation (e.g. BP, BMI): ").upper()
meaning = terms.get(abbreviation)
if meaning:
    print(f"{abbreviation} stands for: {meaning}")
else:
    print("Sorry, abbreviation not found.")
