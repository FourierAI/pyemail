# Oemail
## a simple python tool to send email.
## Install
```code
pip install oemail
```
## Usage
1. open POP3/SMTP service
2. save your auth_code 
3. enjoy it
```python
from oemail import oemail
sender = "xxxxx@google.com"
receiver = "yyyyyy@google.com"
subject = "Happy New year!"
content = "Happy New year!xxxxx"
auth_code = auth_code

email.send_email(sender, receiver, subject, content, auth_code)
```