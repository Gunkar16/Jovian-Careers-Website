from flask import Flask,render_template,jsonify

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': "Software Engineer",
        'location': "Noida, India",
        'salary': "Rs. 15,000,000"
    },
    {
        'id': 2,
        'title': "Data Scientist",
        'location': "Delhi, India",
        'salary': "Rs. 35,000,000"
    },
    {
        'id': 3,
        'title': "Frontend Engineer",
        'location': "Chandigarh, India",
        'salary': "Rs. 30,000,000"
    },
    {
        'id': 4,
        'title': "Backend Engineer",
        'location': "Bengaluru, India",
        'salary': "Rs. 20,000,000"
    }
]


@app.route("/")
def website():
    return render_template("index.html",jobs=JOBS)

@app.route("/api/jobs/")
def api():
    return jsonify(JOBS)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

