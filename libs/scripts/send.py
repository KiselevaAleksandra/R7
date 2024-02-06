import smtplib
import csv
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
from os.path import basename

def send():
    smtp_host = 'smtp.gmail.com'
    login, password = 'zakazchik0111@gmail.com', 'bgrohpwhwgbwvktl'
    recipients_emails = ['lexkslv@gmail.com']

    a = 'Здравствуйте!\nПрошу обеспечить права доступа в систему Р7-офис для пользователя - '
    c = 'согласно роли '
    d = 'С уважением, Киселева Александра.'
    title = 'Подтверждение прав доступа для Р7-офиса'

    with open("C:/Users/aleks/Desktop/dip/result/Users.csv") as r_file:
        file_reader = csv.reader(r_file, delimiter=";")

        for row in file_reader:

            body = a + row[0] + ' (' + row[1] + ') ' + c + row[2] + '.' + '\n\n' + d
            msg = MIMEText(body, 'plain', 'utf-8')
            msg['Subject'] = Header(title, 'utf-8')
            msg['From'] = login
            msg['To'] = ", ".join(recipients_emails)

            s = smtplib.SMTP(smtp_host, 587, timeout=10)
            try:
                s.starttls()
                s.login(login, password)
                s.sendmail(msg['From'], recipients_emails, msg.as_string())
            finally:
                s.quit()
            print('. ')

    print('Заявки на права доступа успешно созданы.\n')

    a = 'Здравствуйте!\nПрошу выделить для проекта "Внедрение корпоративной платформы совместной работы" серверное оборудование с необходимыми параметрами. Информация во вложении.\n\n'
    b = 'С уважением, Киселева Александра.'
    body = a + b
    title = 'Выделение серверного оборудования'

    msg = MIMEMultipart()
    msg['Subject'] = Header(title, 'utf-8')
    msg['From'] = login
    msg['To'] = ", ".join(recipients_emails)

    msg.attach(MIMEText(body, 'plain', 'utf-8'))

    with open("C:/Users/aleks/Desktop/dip/result/Infr.csv", "rb") as f:
        part = MIMEApplication(
            f.read(),
            Name=basename("Infr.csv")
        )

    msg.attach(part)
    s = smtplib.SMTP(smtp_host, 587, timeout=10)
    try:
        s.starttls()
        s.login(login, password)
        s.sendmail(msg['From'], recipients_emails, msg.as_string())
    finally:
        s.quit()
    print('. ')

    print('Заявка на выделение оборудования успешно создана.\n')
