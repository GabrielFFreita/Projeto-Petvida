from flask import Flask, render_template
import mysql.connector as sql

app = Flask(__name__)

def conectar():
        return sql.connect(
        host='localhost',
        port='3407',
        user='root',
        password='root',
        database='database_petvida'
    )

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)