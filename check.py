import smtplib

SENDER_EMAIL = "Enter your email"
APP_PASSWORD = "Enter your app password "

try:
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(SENDER_EMAIL, APP_PASSWORD)
        print("Authentication successful!")
except smtplib.SMTPAuthenticationError:
    print("Error: Authentication failed. Check your email and app password.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
