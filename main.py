import threading
from flask import render_template
from config import app
import mysql.connector

# Database connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="testdatabase"
)
    
# ----- FLASK | BASIC HTML ROUTES ----- #
# -- Routes in Flask define the URLs where the application's functions are executed. -- #
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/cv")
def cv():
    return render_template("cv.html")

@app.route("/gamedev")
def gamedev():
    return render_template("game-dev.html")

@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")

@app.route("/photography")
def photography():
    cursor = db.cursor()
    cursor.execute("SELECT image_url FROM images")
    images = [row[0] for row in cursor.fetchall()]
    cursor.close()
    return render_template("photography.html", images=images)
# ----- FLASK | HTML ROUTES ----- #

def run_flask(): # Defining run_flask function
    app.run(host="0.0.0.0", port=5000)
    
if __name__ == "__main__": # Actually running our flask application.
    app.run(debug=True)
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.start()