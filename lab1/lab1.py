from flask import Flask, render_template , redirect

app = Flask(__name__)
data=[{"id":1,"name":"mahmoud"}
    ,{"id":2,"name":"mohammed"}
    ,{"id":3,"name":"ahmed"}
    ,{"id":4,"name":"ali"}
    ,{"id":5,"name":"khaled"}]
   

@app.route('/')
def home():
    return render_template('home.html',data=data)

@app.route('/search/<int:id>')
def search(id):
    student=None
    for items in data:
         if items['id']==id:
             student=items
             break
    return render_template('search.html',student=student)


if __name__ == '__main__':
    app.run(debug=True)
