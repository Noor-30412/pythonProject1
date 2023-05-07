from flask import Flask
from flask_mail import Mail,Message
import csv
app = Flask(__name__)
mail = Mail(app)
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'bvenkataramana2852@gmail.com'
app.config['MAIL_PASSWORD'] = 'katntfpkkltsagsp'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.route("/")
def index():
    with open('office.csv','r') as f:
        reader = csv.reader(f)
        next(reader)
        for name,addr in reader:
            msg = Message(f'HELLO{name}THIS IS JUST AN INVITAION - FLASK MAIL',sender='bvenkataramana2852@gmail.com',recipients=[addr])
            msg.body='Hi! this is venky,Ur receiving mail from networking solutions we are moving to new office on 20th jan 2022 to guntur.we are inviting to you..'
            mail.send(msg)
            print(f'Sent to {name}')
if __name__ == "__main__":
    app.run()