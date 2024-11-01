# 📧 Internship Mailing System – Automated Bulk Emailer for Internships

Welcome to the **Internship Mailing System**, a Python-based automated email solution designed to streamline the process of applying to multiple institutes, organizations, or professors for internships. This tool simplifies the hassle of personalized communication, enabling students to send **customized emails with attachments** (like resumes or cover letters) in just a few steps.

## 🚀 Key Features
- **Automated Personalized Emails:** Use templates to dynamically generate emails with placeholders like `{professor_name}`, `{institute_name}`, and `{department_name}`.
- **Bulk Email Sending:** Load recipient details from a CSV file and efficiently send emails to multiple institutes in one go.
- **Attachment Support:** Attach resumes, cover letters, or other documents to each email.
- **Error Handling:** Gracefully manage issues like missing files, invalid email addresses, and SMTP authentication failures.
- **Gmail SMTP Integration:** Secure email delivery through Gmail’s SMTP server with support for app passwords.

## 📂 Project Structure
`attachments/` – Place resumes or other files here for sending.<br>
`data/` – Includes CSV files with recipient data (e.g., professor names and emails).<br>
`templates/` – Contains customizable email templates.<br>
`check.py` - a small script to test your credentials outside the main project to check whether authentication is successful or not.<br>
`credentials.py` – Store email and app password securely.<br>
`main.py` – Core script for sending personalized emails.

## 🛠️ How It Works
1. **Customize the Email Template:** Modify the template in `templates/email_template.txt` with placeholders.
2. **Prepare the CSV File:** Add recipient data (e.g., names and emails) in `data/Internship_opportunities.csv`.
3. **Configure Credentials:** Add your Gmail credentials (email and app password) in `credentials.py`.
4. **Run the Script:** Execute `main.py` to start sending emails.

## 🔒 Security Note
- Use **Gmail App Passwords** for secure login (see [how to create an app password](https://myaccount.google.com/apppasswords)).
- **Do not share** your app password publicly or hard-code it in the script. Store it securely in `credentials.py`.

## 🎓 Use Case
This system is ideal for students in their **5th semester or beyond** to apply for internships at academic institutes and organizations. By using **personalized outreach**, it improves the chances of acceptance through professional communication.
<b>(NOT YET TESTED)</b>

## ⚠️ Disclaimer
This tool must be used **responsibly**. Ensure compliance with relevant **privacy policies** and **email regulations** (e.g., GDPR) to avoid sending unsolicited emails.

## 🪪 License
```text
Apache License 2.0

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```


