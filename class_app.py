from flask import Flask,request
from flask_restful import Api,Resource


app = Flask(__name__)
api = Api(app)
class Employee(Resource):
    def get(self):
        data = {"message":"working succesfully"}
        return data

    def post(self):
        data = request.get_json()
        return data

api.add_resource(Employee,"/employee")
if __name__ == '__main__':
    app.run(debug=True)