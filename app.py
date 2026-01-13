from flask import Flask, make_response, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
        "id": 1,
        "title": "Junior+ Data Analyst",
        "company": "X5 RETAIL GROUP",
        "location": "Moscow, office",
        "salary": "150000 RUB",
    },
    {
        "id": 2,
        "title": "Middle Backend Developer",
        "company": "Mail.RU Group",
        "location": "Moscow, office",
        "salary": "210000 RUB",
    },
    {
        "id": 3,
        "title": "Middle+ AQA Python Engineer",
        "company": "Avito",
        "location": "Nizhny Novgorod, remote",
    },
    {
        "id": 4,
        "title": "SDET Python (Senior)",
        "company": "MAGNIT",
        "location": "Saint-Petersburg, office",
        "salary": "250000 RUB",
    },
]


@app.route(rule="/")
def get_homepage():
    return render_template(template_name_or_list="home.html", jobs=JOBS)


@app.route(rule="/api/jobs")
def list_json_jobs():
    return jsonify(JOBS)


@app.errorhandler(404)
def page_not_found(e):
    return "Page not found", 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
