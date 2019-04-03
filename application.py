from flask import Flask
from flask_mail import Mail, Message

app =Flask(__name__)
mail=Mail(app)

app.config.update(
	DEBUG=True,
	#EMAIL SETTINGS
	MAIL_SERVER='smtp.gmail.com',
	MAIL_PORT=465,
	MAIL_USE_SSL=True,
	MAIL_USERNAME = 'chivydisc@gmail.com',
	MAIL_PASSWORD = 'if(!$polarBear)$plainFlour=1204;'
	)

mail=Mail(app)

@app.route("/")
def index():
	msg = Message(
              'Hello',
	       sender='chivydisc@gmail.com',
	       recipients=
               ['chivy1204@gmail.com'])
	msg.body = "đây là mail tự động vui lòng không trả lời"
	mail.send(msg)
	return "Sent"

if __name__ == "__main__":
    app.run()