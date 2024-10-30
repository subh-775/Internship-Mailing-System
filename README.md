# 📧 Internship Mailing System – Automated Bulk Emailer for Internships

Welcome to the **Internship Mailing System**, a Python-based automated email solution designed to streamline the process of applying to multiple institutes, organizations, or professors for internships. This tool simplifies the hassle of personalized communication, enabling students to send **customized emails with attachments** (like resumes or cover letters) in just a few steps.

## 🚀 Key Features
- **Automated Personalized Emails:** Use templates to dynamically generate emails with placeholders like `{professor_name}`, `{institute_name}`, and `{department_name}`.
- **Bulk Email Sending:** Load recipient details from a CSV file and efficiently send emails to multiple institutes in one go.
- **Attachment Support:** Attach resumes, cover letters, or other documents to each email.
- **Error Handling:** Gracefully manage issues like missing files, invalid email addresses, and SMTP authentication failures.
- **Gmail SMTP Integration:** Secure email delivery through Gmail’s SMTP server with support for app passwords.

<h1>📂 Project Structure</h1>
`credentials.py` – Store email and app password securely.
`templates/` – Contains customizable email templates.
`attachments/` – Place resumes or other files here for sending.
`data/` – Includes CSV files with recipient data (e.g., professor names and emails).
`main.py` – Core script for sending personalized emails.

</h1>🛠️ How It Works</h1>
<b>Customize the Email Template</b> – Modify the template in `templates/email_template.txt` with your desired placeholders.
<b>Prepare the CSV File</b> – Add recipient information in `data/Internship_opportunities.csv`.
<b>Configure Credentials</b> – Add your Gmail credentials (email and app password) in `credentials.py`.
<b>Run the Script</b> – Execute `main.py` to start sending emails.

<h1>🔒 Security Note</h1>
Use <b>Gmail App Passwords</b> for secure login.
Avoid sharing your app password publicly; store it in `credentials.py` securely.

<h1>🎓 Use Case</h1>
Designed for students in their 5th semester or beyond to apply for internships in academic institutes and organizations, this system helps personalize outreach and increase acceptance chances through professional communication.

<h1>⚠️ Disclaimer</h1>
This tool should be used responsibly. Ensure that you comply with relevant privacy policies and email regulations (like GDPR) to avoid sending unsolicited emails.
