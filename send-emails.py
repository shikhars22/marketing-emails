import smtplib
from email.message import EmailMessage

# Email configuration
smtp_server = 'smtpout.secureserver.net'  # Replace with your SMTP server address
smtp_port = 465  # Replace with your SMTP server port (587 is the default for TLS)
smtp_username = 'shikhar@detmo.in'  # Replace with your email address
smtp_password = 'ExUz_bK7iZP7S2r'  # Replace with your email password
sender_email = 'shikhar@detmo.in'  # Replace with your email address

# List of recipients
recipients = ['shikhars22@gmail.com', 'shikhar@ddfao.in', 'abhishek@detmo.in']
cc_recipients = ['shikhar@detmo.in', 'abhishek@detmo.in']
recipientFirstNames = ['Shikhar', 'Shikhar', 'Abhishek']

# Connect to the SMTP server and send the email
try:
    server = smtplib.SMTP_SSL(smtp_server, smtp_port)
    # server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
    server.login(smtp_username, smtp_password)
    i=0
    for recipient in recipients:
        # Email content
        subject = 'Do you think your supply chains needs data-driven efficiency, optimization and streamlined processes?'
        body = f'''
Hi {recipientFirstNames[i]},
        
My partner and I were reviewing your company profile and felt that your organization is making great strides in your industry.
You have excellent offerings, and we understand that you need a robust and lean supply chain to achieve such feats.

We bring over a decade of experience and success stories in diverse industries, specializing in optimizing supply chain operations. With a proven track record and a personal and tailored approach, we can help you streamline and enhance your strategic commodity sourcing.

Can we have a short call to discuss your supply chains and understand the challenges you are facing?

Our website --> https://detmo.in/

Shikhar
https://detmo.in/

        '''

        # Create the email message
        msg = EmailMessage()
        msg.set_content(body)
        msg['Subject'] = subject
        msg['From'] = sender_email
        msg['To'] = recipient
        msg['Cc'] = ', '.join(cc_recipients)
        try:
            server.send_message(msg)
            print(f'Email sent successfully to {recipient}!')
            i=i+1
        except:
            print(f'Email not sent successfully to {recipient}!')
            i=i+1
            continue

except Exception as e:
    print('Error: Unable to send email.')
    print(e)
finally:
    server.quit()  # Close the SMTP server connection
