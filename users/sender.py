import smtplib
from email.mime.text import MIMEText


def mail_sender(to, theme, message):
    """Функция по отправке сообщений пользователю"""

    file_content = message

    msg = MIMEText(file_content)
    msg['Subject'] = theme
    msg['From'] = 'Dm1tr1y11@yandex.ru'
    msg['To'] = to

    smtp_server = 'smtp.yandex.ru'
    smtp_port = 465
    smtp_username = 'Dm1tr1y11@yandex.ru'
    # smtp_password = 'h!W(S@m1VDLi'  # обычный пароль
    smtp_password = 'gqwfrlxxruwacfgz'  # пароль приложения яндекс

    s = smtplib.SMTP_SSL(smtp_server, smtp_port)
    s.login(smtp_username, smtp_password)
    s.sendmail('Dm1tr1y11@yandex.ru', [to], msg.as_string())

    s.quit()
