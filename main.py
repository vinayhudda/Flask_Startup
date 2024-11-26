from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

# Creating names object
names = {"tim":{"age":19, "gender":"male"},
         "bill":{"age":70, "gender":"male"}}

# Making a Resource class that will allow us to handle get/put request
class HelloWorld(Resource):
    def get(self, name):
        #return {"name" : "name"}
        return names[name]

    def post(self):
        return{"data":"Posted"}


# Registring get request as a resource (Accessed By : http://127.0.0.1:5000/helloworld )
api.add_resource(HelloWorld, "/helloworld/<string:name>")


if __name__ == "__main__":
    app.run(debug=True)