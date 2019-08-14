import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from tools.report_utils import Report


def send_email(report_file):
    smtpserver = "smtp.qq.com"
    port = 465
    sender = "xxxxx@qq.com"     # 密码需要输入授权码。
    psw = "xxxxx"
    receiver = "18xxxxxx@163.com"

    with open(report_file, "rb") as f:
        mail_body = f.read()
    # 使用email构造邮件
    msg = MIMEMultipart()
    body = MIMEText(mail_body, _subtype="html", _charset="utf-8")
    msg["Subject"] = "自动化测试报告"
    msg["from"] = sender
    msg["to"] = receiver
    msg.attach(body)

    # 添加附件
    att = MIMEText(open(report_file, "rb").read(), "base64", "utf-8")
    att["Content-type"] = "application/octet-stream"
    att["Content-Disposition"] = "attachment;filename = 'report.html'"
    msg.attach(att)

    try:
        smtp = smtplib.SMTP_SSL(smtpserver, port)
    except:
        smtp = smtplib.SMTP()
        smtp.connect(smtpserver, port)

    smtp.login(sender, psw)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()
    print("邮件发送成功！")


if __name__ == "__main__":
    send_email(Report.get_report_file())