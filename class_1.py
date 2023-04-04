from flask import Flask  # importing flask 
from flask import render_template # connecting flask code with html page 

app = Flask(__name__)   # giving entire flask software permission to app variable 


@app.route('/')   # default opens an tab in browser:
def task_1():
    return render_template('index.html')

@app.route('/second')
def tast_2():
    return render_template('second.html')



if __name__ == '__main__':
    app.run(debug=True)  # saving changes while server is in live :
