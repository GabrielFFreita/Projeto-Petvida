from flask import Flask, render_template
import mysql.connector as sql

app = Flask(__name__)

def conectar():
    return sql.connector.connect(
        host='localhost',
        port='3407',
        user='root',
        password='root',
        database='banco_fgs'
    )


@app.route("/")
def home():
    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True)