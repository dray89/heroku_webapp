from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")


''' 
how to do post request

 @app.route(/submit, methods=['POST'])
 def submit():
     if request.method==POST:
         field1 = request.form[FIELD1]
         field2 = request.form[FIELD2]
         print(field1, field2)
         if customer== '' or dealer =='':
             return render_template('index.html', message="please enter required fields")
         return render_template(success.html))
'''

if __name__ == "__main__":
    app.debug = True
    app.run()