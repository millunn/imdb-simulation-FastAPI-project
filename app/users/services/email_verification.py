def send_email_login_alert(email) -> None:
    """Creates mail subject and body for a security alert mail upon log in, sends if it's called"""
    import smtplib
    import ssl
    from email.message import EmailMessage

    email_sender = "m7testpy@gmail.com"
    email_password = "vfsk dpsh piqi ztbg"
    email_receiver = email
    subject = "Security alert - Did you just log in?"
    body = f"Someone've just logged into your account! Please check activity log."
    em = EmailMessage()
    em["From"] = email_sender
    em["To"] = email_receiver
    em["Subject"] = subject
    em.set_content(body)
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
        try:
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender, email_receiver, em.as_string())
        except Exception as e:
            print(f"\n\nSending failed!\n\n{str(e)}\n\n")
            return False
    print("You've successfully sent an email!")
    return True


def send_confirmation_email(email) -> None:
    """Creates mail subject and body for a confirmation mail upon registration, sends if it's called"""
    import smtplib
    import ssl
    from email.message import EmailMessage

    email_sender = "m7testpy@gmail.com"
    email_password = "vfsk dpsh piqi ztbg"
    email_receiver = email
    subject = "Confirmation email"
    body = f"You've successfully created an account with email address - {email}."
    em = EmailMessage()
    em["From"] = email_sender
    em["To"] = email_receiver
    em["Subject"] = subject
    em.set_content(body)
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
        try:
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender, email_receiver, em.as_string())
        except Exception as e:
            print(f"\n\nSending failed!\n\n{str(e)}\n\n")
            return False
    print("You've successfully sent an email!")
    return True
