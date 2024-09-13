def email():
    from sendgrid import SendGridAPIClient
    from sendgrid.helpers.mail import (Mail, Attachment, FileContent, FileName, FileType, Disposition)
    out_csv_file_path = '/home/thangnc/stock_data/stock_price.csv'
    import base64
    message = Mail(
        from_email='ainoodle.tech@gmail.com',
        to_emails='thangnch@gmail.com;thang.nc@shb.com.vn',
        subject='Your file is here!',
        html_content='<img src="https://miai.vn/wp-content/uploads/2022/01/Logo_web.png"> Dear Customer,<br>Welcome to Mi AI. Your file is in attachment<br>Thank you!'
    )

    with open(out_csv_file_path, 'rb') as f:
        data = f.read()
        f.close()
    encoded_file = base64.b64encode(data).decode()

    attachedFile = Attachment(
        FileContent(encoded_file),
        FileName('data.csv'),
        FileType('text/csv'),
        Disposition('attachment')
    )
    message.attachment = attachedFile

    try:
        sg = SendGridAPIClient("Send Grid Token here")
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
        print(datetime.now())
    except Exception as e:
        print(e.message)

    return True