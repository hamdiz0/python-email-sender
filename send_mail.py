import smtplib
import argparse
from email.message import EmailMessage

# Argument parsing
parser = argparse.ArgumentParser()
parser.add_argument("-u", "--user", required=True, help="user's email address")
parser.add_argument("-s", "--subject", required=False, help="email subject", default="")
parser.add_argument("-p", "--password",required=True, help="gmail app password")
parser.add_argument("-c", "--content", required=True, help="file containing email content")
parser.add_argument("-r", "--emails", required=True, help="file containing emails addresses")
args = parser.parse_args()

# Read email content and recipient addresses
with open(args.content, "r") as f:
    content = f.read()
with open(args.emails, "r") as f:
    emails = [line.strip() for line in f]
 
# Send emails
for email in emails:
    msg = EmailMessage()
    msg.set_content(content)
    msg["Subject"] = args.subject
    msg["From"] = args.user
    msg["To"] = email
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(args.user, args.password)
        smtp.send_message(msg)
        print(f"Email sent to {email} ✅ \n")