import smtplib
from email.mime.text import MIMEText
from email.header import Header


def send_email(sender, receiver, subject, mes, auth_code):
    """
    Send an email using the specified SMTP server.

    Args:
        sender (str): The email address of the sender.
        receiver (str): The email address of the receiver.
        subject (str): The subject of the email.
        mes (str): The message content of the email.
        auth_code (str): The authorization code for the sender's email account.

    Returns:
        None

    Raises:
        smtplib.SMTPException: If there is an error sending the email.
    """

    message = MIMEText(mes, 'plain', 'utf-8')   # 邮件内容
    message['From'] = Header(f"Sender<{sender}>")  # 发送者
    message['To'] = Header(f"Receiver<{receiver}>")  # 接收者
    message['Subject'] = Header(subject, 'utf-8') # 邮件主题

    try:
        server = smtplib.SMTP_SSL('smtp.qq.com', 465)
        server.login(sender, auth_code)
        server.sendmail(sender, receiver, message.as_string())
        print("邮件发送成功")
        server.close()
    except smtplib.SMTPException:
        print("Error: 无法发送邮件")


if __name__ == '__main__':

    sender = 'xxxxxx'  # 发送邮箱
    receiver = 'xxxxxx'  # 接收邮箱
    auth_code = "xxxxxx"  # 授权码
    
    send_email(sender=sender, receiver=receiver, subject="测试邮件", mes="这是一封测试邮件", auth_code=auth_code)