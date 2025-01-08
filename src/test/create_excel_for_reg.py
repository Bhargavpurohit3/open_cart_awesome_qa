import pandas as pd
import os

# Ensure the directory exists
directory = r"C:\Users\puroh\PycharmProjects\open_cart_awesomeQA_ui_project\src"
if not os.path.exists(directory):
    os.makedirs(directory)

# Define the file path with the .xlsx extension
file_path = r"C:\Users\puroh\PycharmProjects\open_cart_awesomeQA_ui_project\src\Register_Test_Data.xlsx"

# Define the data
data = {
    "First Name": ["John", "Alice", "Robert", "Emily", "Michael"],
    "Last Name": ["Doe", "Smith", "Brown", "Davis", "Johnson"],
    "E-Mail": ["john.doe@example.com", "alice.smith@example.com", "robert.brown@example.com",
               "emily.davis@example.com", "michael.johnson@example.com"],
    "Telephone": ["1234567890", "9876543210", "1122334455", "5566778899", "7788996655"],
    "Your Password": ["Password123!", "Alice@2023", "Robert#456", "EmilyD@78", "Mike_Pass1"],
    "Password Confirm": ["Password123!", "Alice@2023", "Robert#456", "EmilyD@78", "Mike_Pass1"],
    "Newsletter": ["Subscribe", "No", "Subscribe", "No", "Subscribe"],
}

# Convert the data into a DataFrame
df = pd.DataFrame(data)

# Save the DataFrame to an Excel file
df.to_excel(file_path, index=False)

print(f"File saved successfully at {file_path}")
