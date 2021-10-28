from sendmail import MailSender
plaintext = "Hello Bobby, \n" \
            "I'm just testing my new BOBBY email sending system here.\n" \
            "Thank you"
ourmailsender = MailSender('bobbykboseoffice@gmail.com', 'password', ('smtp.gmail.com', 587))
ourmailsender.set_message(plaintext, "This is a test", "For my Project")
ourmailsender.set_recipients(['bobbykboseoffice.com'])
ourmailsender.connect()
ourmailsender.send_all()
