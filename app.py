from Flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#ENV = 'dev'
ENV = 'prod'

if ENV== 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123456@localhost/databasename'
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] ='postgres://dpnsjvnfohxnbe:0d696bcfe4f2ddbb7c668e81176495b4f0204aafbaf6e3483d7da373082e80e1@ec2-23-22-156-110.compute-1.amazonaws.com:5432/d4pb7s5vdspj5m'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class database(db.Model):
    __tablename__ = 'data'
    id = db.Column(db.Integer, primary_key=True)
    column1 = db.Column(db.String(200), unique=True)
    column2 = db.Column(db.String(200), unique=True)

    def __init__(self, column1, column2):
        self.column1 = column1
        self.column2 = column2

@app.route('/')
def index():
    return render_template("index.html")


''' 
how to do post request / Form

 @app.route(/submit, methods=['POST'])
 def submit():
     if request.method==POST:
         field1 = request.form[FIELD1]
         field2 = request.form[FIELD2]
         print(field1, field2)
         if field1== '' or field2 =='':
             return render_template('index.html', message="please enter required fields")
         if db.session.query(Feedback).filter(Feedback.field1 ==field1).count() ==0:
            data = Feedback(field1, field2)
            db.session.add(data)
            db.session.commit()
            return render_template(success.html))
         return render_template('index.html', message="Already Submitted")

'''

if __name__ == "__main__":
    app.debug = True
    app.run()