import imaplib
import email
import re
import time

class EmailOTPFetcher:
    def __init__(self, username, app_password):
        self.username = username
        self.app_password = app_password

    def fetch_otp(self, sender="zomato", wait_timeout=30):
        try:
            mail = imaplib.IMAP4_SSL("imap.gmail.com")
            mail.login(self.username, self.app_password)
            
            print(f"Connected to email '{self.username}'. Waiting for '{sender}' OTP...")
            end_time = time.time() + wait_timeout
            
            while time.time() < end_time:
                mail.select("inbox")
                status, messages = mail.search(None, f'(FROM "{sender}")')
                if status == "OK" and messages[0]:
                    mail_ids = messages[0].split()
                    latest_email_id = mail_ids[-1]
                    status, msg_data = mail.fetch(latest_email_id, "(RFC822)")
                    msg = email.message_from_bytes(msg_data[0][1])
                    body = self._get_body(msg)
                    
                    # Search for 6-digit OTP
                    match = re.search(r'\b\d{6}\b', body)
                    if match:
                        return match.group(0)
                        
                time.sleep(4)
                
            print("OTP fetch timeout reached.")
            return None
        except Exception as e:
            print(f"IMAP Error: {e}")
            return None

    def _get_body(self, msg):
        body = ""
        if msg.is_multipart():
            for part in msg.walk():
                if part.get_content_type() == "text/plain":
                    body = part.get_payload(decode=True).decode(errors='ignore')
                    break
        else:
            body = msg.get_payload(decode=True).decode(errors='ignore')
        return body

if __name__ == "__main__":
    # Test script directly
    fetcher = EmailOTPFetcher("kthewok@gmail.com", "svsn olug djum ljen")
    otp = fetcher.fetch_otp()
    if otp:
        print(f"Successfully caught OTP: {otp}")
