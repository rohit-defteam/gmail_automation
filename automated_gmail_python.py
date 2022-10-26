def MailSender(mail):
    try:
        import smtplib
        connection = smtplib.SMTP("SMTP.gmail.com",587)
        connection.starttls()
        connection.login(user = "sender@email.com",password = "password")
        connection.sendmail(from_addr = "sender@email.com",to_addrs = 'reciever@email.com', msg = "Subject:Very Fresh Mail\n\n Fresh Mail")
        connection.close()
        return '1'
    except:
        return '0'