import pandas as pd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from credentials import SENDER_EMAIL, APP_PASSWORD
import os
import re
import time

# Load the email template with error handling
def load_template():
    try:
        with open('templates/email_template.txt', 'r') as file:
            return file.read()
    except FileNotFoundError:
        print("Error: Email template not found.")
        return "Default email content."

# Generate personalized email content
def generate_email_content(professor_name, institute_name, department):
    template = load_template()
    return template.format(
        professor_name=professor_name,
        institute_name=institute_name,
        department=department,
        related_courses="AI, Machine Learning, and Data Science"
    )

# Validate email address
def is_valid_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

# Send email function with error handling
def send_email(recipient_email, subject, body, attachments=[]):
    msg = MIMEMultipart()
    msg['From'] = SENDER_EMAIL
    msg['To'] = recipient_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    for file in attachments:
        try:
            with open(file, 'rb') as f:
                attach = MIMEApplication(f.read(), Name=file)
                attach['Content-Disposition'] = f'attachment; filename="{file}"'
                msg.attach(attach)
        except FileNotFoundError as e:
            print(f"Warning: {e}. Skipping attachment: {file}")

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(SENDER_EMAIL, APP_PASSWORD)
            server.send_message(msg)
            print(f"Email successfully sent to {recipient_email}")
    except smtplib.SMTPAuthenticationError:
        print("Error: Authentication failed. Check your credentials.")
    except Exception as e:
        print(f"Failed to send email to {recipient_email}. Error: {e}")

# Main function to load CSV data and send emails
def main():
    try:
        data = pd.read_csv('data/Internship_opportunities.csv')
    except FileNotFoundError:
        print("Error: CSV file not found.")
        return
    except pd.errors.EmptyDataError:
        print("Error: CSV file is empty.")
        return

    for index, row in data.iterrows():
        if not is_valid_email(row['Email']):
            print(f"Invalid email: {row['Email']}. Skipping...")
            continue

        professor_name = row['User'].split(',')[0]
        institute_name = row['User']
        department = "Computer Science and Engineering"

        email_content = generate_email_content(professor_name, institute_name, department)

        send_email(
            recipient_email=row['Email'],
            subject="An Early Testing Email for Auto mailing system",
            body=email_content,
            attachments=['attachments/fun.pdf']
        )
        time.sleep(2)

if __name__ == "__main__":
    main()
