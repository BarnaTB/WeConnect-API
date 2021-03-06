import flask
from flask import Flask, redirect
from . views.user.views import userBlueprint
from . views.business.views import businessBlueprint
from . views.reviews.views import reviewBlueprint
from flasgger import Swagger
from flasgger import swag_from

app = Flask(__name__)
app.register_blueprint(userBlueprint)
app.register_blueprint(businessBlueprint)
app.register_blueprint(reviewBlueprint)

#create the swagger template
template = {
    "swagger": "2.0",
    "info": {
        "title":
        "WeConnect API with data structures",
        "description":
        "WeConnect provides a platform that brings businesses and individuals together. This platform creates awareness for businesses and gives the users the ability to write reviews about the businesses they have interacted with.", "version":"1.0.0"},
    "schemes": ["http", "https"],
    "specs_route":"/apidocs/"
}

#swagger docs instanciation
swagger = Swagger(app, template=template)

@app.route('/')
def index():
    return redirect('/apidocs/')

# if __name__ == '__main__':
#     app.run(debug=True)