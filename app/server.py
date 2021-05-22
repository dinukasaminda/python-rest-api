# print(confusion_matrix(y_test, y_pred))
# print(classification_report(y_test, y_pred))


import flask
from flask import request, jsonify

import my_actions

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/run_script', methods=['POST'])
def runScript():
    data = request.get_json()

    # you can get post data from data variable
    print(data)

    result = my_actions.run_script(data)

    # if(data["ageType"] == "adult"):
    #     pred= app.run_script(data["breed"],[data["input"]])
    #     result = {
    #         "output":pred,
    #         "input":data
    #     }
    # else :
    #     pred= puppy.predictOutput(data["breed"],[data["input"]])
    #     result = {
    #         "output":pred,
    #         "input":data
    #     }
    return jsonify({"result":result,"status":"ok"})


app.run(port=5200,host= '0.0.0.0')