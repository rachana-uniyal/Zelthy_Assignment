import smtplib, ssl

class Email :
	def __init__(self, sender_email,recipient,password,subject,body):
		self.Port = 587
		self.Smtp_server  = "smtp.gmail.com"
		self.Sender_email = sender_email
		self.Recipient = recipient
		self.Password = password
		self.Subject = subject
		self.Body = body
		self.context = ssl.create_default_context()

	def send_email(self):
		if not self.Recipient:
			return 0
		try :
			server = smtplib.SMTP(self.Smtp_server, self.Port)
			server.starttls(context=self.context)
			server.login(self.Sender_email, self.Password)
			message = 'Subject: {}\n\n{}'.format(self.Subject, self.Body)
			server.sendmail(self.Sender_email, self.Recipient , message)
		except:
			return 2
		return 1


sender_email = "demo87094@gmail.com"
subject = input("Subject? ")
body = input("Body? ")
recipient = input("Recipient? ")	
password = "demo@49078"

my_email = Email(sender_email,recipient,password,subject,body)
check = my_email.send_email()
if check ==0:
	print("Recipient cann't be empty")
elif check == 2:
	print("Recipient Email is invalid")
else:
	print("mail sent")



