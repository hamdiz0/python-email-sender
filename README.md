# python-email-sender
### A simple command-line Python script to send plain-text emails to multiple recipients using Gmail SMTP.

## ⚙️ Features
- Send the same email to **multiple recipients**.  
- Supports sending from **multiple Gmail accounts**, each with its own App Password.  
- Uses **Gmail’s SMTP server** with secure SSL.  
- Customizable subject line and content file.  

## 🧩 Prerequisites
- Python **3.8+** installed.
- A **Gmail account** with:
  - **2-Step Verification enabled**.
  - A generated **App Password** (create one at: https://myaccount.google.com/apppasswords).

## 📁 File Requirements
You will need the following files:

#### 1. Email content file
- A plain text file that contains the message body you want to send.  
  [example](./example_content.txt)

#### 2. Email recipient list file
- A plain text file containing **one recipient email address per line**.  
  [example](./example_recipients.txt)

#### 3. ( Sender email + app password ) file  
- A plain text file where **each line contains:** sender email address with its corresponding generated app password.
  [example](./example_senders.txt)

## ⚙️ Arguments
| Flag | Long Option  | Required | Description |
|------|-------------  |-----------|-------------|
| `-ep` | `--emailAndAppPassword` | ✅ | File containing sender Gmail + App Password (one per line: `email,appPassword`) |
| `-c`  | `--content`             | ✅ | Path to the file containing the email body |
| `-r`  | `--emails`              | ✅ | Path to the file containing recipient emails |
| `-s`  | `--subject`             | ❌ | Email subject (defaults to empty string) |

## 🚀 Usage

```sh
python3 send_mail.py \
-ep "path_to_email_and_app_passwords.txt" \
-c "path_to_example_content.txt" \
-r "path_to_example_recipients.txt" \
-s "subject of the mail"
```
