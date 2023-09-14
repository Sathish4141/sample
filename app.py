from flask import Flask


app = Flask(__name__)

@app.route('/read')
def reading():
    data = {"msg":"working successfully"}
    return data


@app.run("/create")
def creating(request):
    data = request.get_json()
    return data



if __name__ == "__main__":
    app.run(debug=True)