import pandas as pd
def calculate_total_margin(file_path):
    # Load the Excel file
    df = pd.read_excel(file_path)
    
    # Convert 'Date' column to datetime format
    df['Date'] = pd.to_datetime(df['Date'], format='%Y/%m/%d', errors='coerce')
    
    # Define target date in proper datetime format
    target_date = pd.Timestamp('2023-04-03 00:29:00')
    
    # Filter for 'Iota' sales in the 'USA' before the target date
    df_filtered = df[
        (df['Date'] < target_date) & 
        (df['Product/Code'].str.contains('Iota', case=False, na=False, regex=True)) & 
        (df['Country'].str.upper().str.startswith('US'))  # Handle variations like USA, US, U.S.
    ]
    
    # Convert 'Sales' and 'Cost' to numeric after removing ' USD'
    df_filtered['Sales'] = df_filtered['Sales'].str.replace(' USD', '', regex=True).astype(float)
    df_filtered['Cost'] = df_filtered['Cost'].str.replace(' USD', '', regex=True).astype(float)
    
    # Calculate margin
    df_filtered['Margin'] = df_filtered['Sales'] - df_filtered['Cost']
    
    # Compute total margin
    total_margin = df_filtered['Margin'].sum()
    
    return total_margin
