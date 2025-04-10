import os
import pandas as pd
from fpdf import FPDF
from email.message import EmailMessage
import smtplib


EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS" , "r73018594@gmail.com")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD" , "tqwldrxjjvnzqstg")
SMTP_SERVER = os.getenv("SMTP_SERVER", "smtp.gmail.com")
SMTP_PORT = int(os.getenv("SMTP_PORT", 587))

# Debug check for environment variables
if not EMAIL_ADDRESS or not EMAIL_PASSWORD:
    print("❌ ERROR: EMAIL_ADDRESS or EMAIL_PASSWORD not set in .env")
    exit()

# Create payslips folder
os.makedirs("payslips", exist_ok=True)

# Load Excel file
file_path = r"C:\Users\uncommonstudent\PycharmProjects\PythonProject\Employees.xlsx.xlsx"
print("Found file:", os.path.exists(file_path))
if not os.path.exists(file_path):
    print("❌ ERROR: Excel file not found.")
    exit()

df = pd.read_excel(file_path)
df.columns = df.columns.str.strip()  # Clean headers

# Payslip generator
def generate_payslip(emp):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    # Set title
    pdf.set_fill_color(0, 102, 204)  # Blue background
    pdf.set_text_color(255, 255, 255)  # White text
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(0, 10, "Payslip - Uncommon IT", ln=True, align='C', fill=True)

    pdf.ln(10)

    # Reset text color for content
    pdf.set_text_color(0, 0, 0)
    pdf.set_font("Arial", size=12)

    # Compute Net Salary
    basic_salary = int(emp['Basic Salary'])
    allowances = int(emp['Allowances'])
    deductions = int(emp['Deductions'])
    net_salary = basic_salary + allowances - deductions

    # Employee info with borders
    details = [
        ("Employee ID", emp['Employee ID']),
        ("Name", emp['Name']),
        ("Basic Salary", f"${basic_salary}"),
        ("Allowances", f"${allowances}"),
        ("Deductions", f"${deductions}"),
        ("Net Salary", f"${net_salary}")
    ]

    for label, value in details:
        pdf.set_font("Arial", 'B', 12)
        pdf.cell(50, 10, label, border=1)
        pdf.set_font("Arial", size=12)
        pdf.cell(0, 10, str(value), border=1, ln=True)

    filename = f"payslips/{emp['Employee ID']}.pdf"
    pdf.output(filename)
    return filename

    #net_salary = int(emp['Basic Salary']) + int(emp['Allowances']) - int(emp['Deductions'])
    #lines = [
       # f"Employee ID: {emp['Employee ID']}",
       # f"Name: {emp['Name']}",
       # f"Basic Salary: ${emp['Basic Salary']}",
       # f"Allowances: ${emp['Allowances']}",
       # f"Deductions: ${emp['Deductions']}",
       # f"Net Salary: ${net_salary}"
   # ]

    #for line in lines:
        #pdf.cell(200, 10, txt=line, ln=True)

    #filename = f"payslips/{emp['Employee ID']}.pdf"
    #pdf.output(filename)
    #return filename

# Email sender
def send_email(to_email, filename, name):
    msg = EmailMessage()
    msg['Subject'] = "Your Payslip for This Month"
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = to_email
    msg.set_content(f"Dear {name},\n\nPlease find attached your payslip for this month.\n\nBest regards,\nHR")

    with open(filename, "rb") as f:
        msg.add_attachment(f.read(), maintype='application', subtype='pdf', filename=os.path.basename(filename))

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.ehlo()
            server.starttls()
            server.ehlo()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)
        return True
    except Exception as e:
        print(f"❌ Email send error for {name}: {e}")
        return False

# Main loop
for _, emp in df.iterrows():
    try:
        payslip_file = generate_payslip(emp)
        sent = send_email(emp['Email'], payslip_file, emp['Name'])
        if sent:
            print(f"✅ Sent payslip to {emp['Name']} at {emp['Email']}")
    except Exception as e:
        print(f"❌ Error processing {emp['Name']}: {e}")
