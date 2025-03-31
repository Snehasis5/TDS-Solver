import pdfplumber
import pandas as pd
import logging
from fastapi import UploadFile

def extract_biology_marks(pdf_file: UploadFile):
    logging.getLogger("pdfminer").setLevel(logging.ERROR)  # Suppress warnings
    
    filtered_tables = []
    current_group = None

    with pdfplumber.open(pdf_file.file) as pdf:  # Use .file instead of a file path
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                for line in text.split("\n"):
                    if "Student marks - Group" in line:
                        parts = line.split(" ")
                        try:
                            current_group = int(parts[-1])  # Extract last part as group number
                        except ValueError:
                            continue  # Skip invalid integers

                extracted_table = page.extract_table()
                if extracted_table:
                    for row in extracted_table[1:]:  # Skip headers
                        if current_group is not None:
                            filtered_tables.append([current_group] + row)  # Add group info

    # Convert extracted table data into a DataFrame
    columns = ["Group", "Maths", "Physics", "English", "Economics", "Biology"]
    df = pd.DataFrame(filtered_tables, columns=columns)

    # Convert numerical columns to appropriate data types
    for col in ["Group", "Maths", "Physics", "English", "Economics", "Biology"]:
        df[col] = pd.to_numeric(df[col], errors='coerce')

    # Filter students who scored 79 or more in English and belong to groups 1-25
    filtered_df = df[(df["English"] >= 79) & (df["Group"].between(1, 25))]

    # Calculate the total Biology marks of the filtered students
    total_biology_marks = filtered_df["Biology"].sum()
    return total_biology_marks
