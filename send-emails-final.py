import smtplib
from email.message import EmailMessage

# Email configuration
smtp_server = 'smtpout.secureserver.net'  # Replace with your SMTP server address
smtp_port = 465  # Replace with your SMTP server port (587 is the default for TLS)
smtp_username = 'shikhar@detmo.in'  # Replace with your email address
smtp_password = 'ExUz_bK7iZP7S2r'  # Replace with your email password
sender_email = 'shikhar@detmo.in'  # Replace with your email address

# List of recipients
recipients = ['john.pettit@arclin.com', 'sbutterick@stayapt.com', 'megan.delancellotti@life-house.com', 'pamela.rozell@riveroakscc.net', 'JettaDezonia@vistar.com', 'MollyMcKenna@mail.com', 'markgilbert@gmail.com', 'Marc.Moritz@auma.com', 'Murat.Yildirim@leuze.com']
cc_recipients = ['shikhar@detmo.in', 'abhishek@detmo.in']
recipientFirstNames = [ 'John ', 'Shirley ', 'Megan ', 'Pamela ', 'Jetta ', 'Molly ', 'Mark ', 'Marc', 'Murat']

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

Following on my previous email, as they tend to slip through the cracks. I wanted to see if you/your team is planning to bring analytics, AI, machine learning and business intellgence into your supplier base management.

At detmoi, we provide supply chain services like business process optimization in procurement analytics and inventory analytics(demand planning, cash flow improvement) etc. We do this by identifing cost saving opportunities in your existing vendor management processes and provide analytical, data driven framework for accurate and fast decision making.

Important note - Moreover, we are more than happy to offer you a NO-COST current  business processes evalaution and identify problem areas. We only ask you to move forward with us if you are impressed by our work. This is applicable for any of your colleagues/clients/partners, in your industry, if they encounter any such-vendor management challenges

We hope it can be helpful to your business and we look forward to any opportunities and your cooperation.

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
