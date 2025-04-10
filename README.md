Payslip Generator and Emailer
This Python project automates the creation and distribution of employee payslips. It reads employee data from an Excel file, generates a PDF payslip for each employee, and sends the payslip as an email attachment.

Overview
Input: Employee details stored in an Excel file (e.g., Employee ID, Name, Basic Salary, Allowances, Deductions, Email).

Processing:

Reads and cleans data from the Excel file.

Computes the net salary for each employee.

Generates a PDF payslip using the FPDF library.

Output:

A PDF payslip for each employee saved in the payslips directory.

Each PDF is emailed to the respective employee using SMTP (configured here for Gmail).

Prerequisites
Make sure you have the following installed on your system:

Python 3.x

The following Python packages (can be installed via pip):

pandas

openpyxl (if required for Excel file reading)

fpdf

smtplib (part of the standard library)

email (part of the standard library)

You can install the required packages using:

bash
Copy
Edit
pip install pandas openpyxl fpdf
Configuration
Before running the script, update or create an environment file (e.g., .env) in the project directory with the following variables (or modify the default values in the code):

EMAIL_ADDRESS: The email address used to send the payslips.

EMAIL_PASSWORD: The password or app-specific password for the sending email.

SMTP_SERVER: The SMTP server to be used (default is Gmail's smtp.gmail.com).

SMTP_PORT: The port number (default is 587 for TLS).

Example .env file content:

ini
Copy
Edit
EMAIL_ADDRESS=your-email@example.com
EMAIL_PASSWORD=your-email-password
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
Note: The current code uses default values if these environment variables are not set. It is strongly recommended to use environment variables for security reasons.

File Structure
graphql
Copy
Edit
PythonProject/
├── Employees.xlsx.xlsx   # Excel file with employee data
├── GIT.py                # Main Python script
├── payslips/             # Directory where PDF payslips will be saved (automatically created)
└── README.md             # This file
How It Works
Excel File Load:
The code checks if the specified Excel file exists and loads the data using pandas. It ensures that headers are cleaned (trailing/leading spaces removed).

Payslip Generation:
For each employee record, the generate_payslip() function creates a PDF document with:

A title (with a colored background) indicating "Payslip - Uncommon IT".

Employee details such as Employee ID, Name, Basic Salary, Allowances, Deductions, and Net Salary.

The net salary is computed using the formula:

ini
Copy
Edit
net_salary = basic_salary + allowances - deductions
The PDF is saved in the payslips folder with the filename based on the Employee ID.

Email Dispatch:
The send_email() function composes an email for each employee:

Sets up a subject, sender, recipient, and body.

Attaches the corresponding PDF payslip.

Connects to the SMTP server (Gmail by default), logs in, and sends the email.

Error Handling:
If there are any issues during PDF generation or email sending, the code catches the exception and logs a descriptive error message.

Running the Code
Ensure the necessary libraries are installed.

Confirm that the Excel file exists at the specified path.

Update your environment variables as needed.

Run the Python script from your IDE (e.g., PyCharm) or via the command line:

bash
Copy
Edit
python GIT.py
After execution, check the payslips folder for the generated PDFs and your email inbox (or test email account) for the sent payslips.

Troubleshooting
File Not Found:
If you see a message like Excel file not found., verify the file path in the code is correct.

Environment Variables:
If the email is not sent, ensure the EMAIL_ADDRESS and EMAIL_PASSWORD values are correctly set. Using app-specific passwords (especially for Gmail) may be necessary.

Conversion Errors:
Errors during salary computation (e.g., converting strings to integers) often indicate that the Excel file might include header rows or non-numeric data. Ensure that the Excel file is formatted correctly.

Security Considerations
Email Credentials:
Do not hardcode sensitive information like email credentials directly into your script. Use environment variables or a secure configuration method.

Testing:
Before sending live emails, test the script with a small sample dataset and send emails to a test account.

License
Include your licensing information here if applicable.

