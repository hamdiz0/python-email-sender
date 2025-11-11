# python-email-sender
### A simple command-line Python script to send plain-text emails to multiple recipients using Gmail SMTP.


## ⚙️ Features
- Send the same email to multiple recipients listed in a file.  
- Uses **Gmail’s SMTP server** with secure SSL.  
- Customizable subject line and content file.  
- Lightweight — no external dependencies required (uses Python standard library).

## 🧩 Prerequisites

- Python **3.8+** installed.
- A **Gmail account** with:
  - **2-Step Verification enabled**.
  - A generated **App Password** (create one at: [https://myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords)).

## 📁 File Requirements
You will need the following files:
#### 1. Email content file
- A plain text file that contains the message body you want to send. [example](./example_content.txt)
#### 2. Email recipient list file
- A plain text file containing one recipient email address per line. [example](./example_recipients.txt)

## ⚙️ Arguments
| Flag | Long Option  | Required | Description |
|------|--------------|-----------|-------------|
| `-u` | `--user`     | ✅ | Sender Gmail address (your account) |
| `-p` | `--password` | ✅ | Gmail App Password (16-character password) |
| `-c` | `--content`  | ✅ | Path to the file containing the email body |
| `-r` | `--emails`   | ✅ | Path to the file containing recipient emails (one per line) |
| `-s` | `--subject`  | ❌ | Email subject (defaults to an empty field) |

## 🚀 Usage

```sh
python3 send_mail.py \
  -u "your_email@gmail.com" \
  -p "your_app_password" \
  -c "path to example_content.txt" \
  -r "path to example_recipients.txt" \
  -s "subject of the mail"
```
