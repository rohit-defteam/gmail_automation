def MailSender(mail):
    try:
        import smtplib
        connection = smtplib.SMTP("SMTP.gmail.com",587)
        connection.starttls()
        connection.login(user = "",password = "")
        connection.sendmail(from_addr = "",to_addrs = email, msg = "Subject:Very Fresh Mail\n\n Fresh Mail")
        connection.close()
        return '1'
    except:
        return '0'