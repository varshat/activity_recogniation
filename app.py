
# importing the necessary dependencies
from flask import Flask, render_template, request,jsonify
from flask_cors import CORS,cross_origin
import pickle

app = Flask(__name__) # initializing a flask app

@app.route('/',methods=['GET'])  # route to display the home page
@cross_origin()
def homePage():
    return render_template("index.html")

@app.route('/predict',methods=['POST','GET']) # route to show the predictions in a web UI
@cross_origin()
def index():
    if request.method == 'POST':
        try:
            #'avg_rss12', 'var_rss12', 'avg_rss13', 'var_rss13', 'avg_rss23','var_rss23'
            #  reading the inputs given by the user
            avg12=float(request.form['avg_rss12'])
            var12 = float(request.form['var_rss12'])
            avg13 = float(request.form['avg_rss13'])
            var13 = float(request.form['var_rss13'])
            avg23 = float(request.form['avg_rss23'])
            var23 = float(request.form['var_rss23'])
            filename = 'Logistic_Regression_model.pickle'
            loaded_model = pickle.load(open(filename, 'rb')) # loading the model file from the storage
            # predictions using the loaded model file
            prediction=loaded_model.predict([[avg12,var12,avg13,var13,avg23,var23]])
            print('prediction is', prediction)
            res = numbers_to_strings(prediction[0])
            # showing the prediction results in a UI
            return render_template('results.html',prediction=res)
        except Exception as e:
            print('The Exception message is: ',e)
            return 'something is wrong'
    # return render_template('results.html')
    else:
        return render_template('index.html')


# Function to convert number into string
# Switcher is dictionary data type here
def numbers_to_strings(argument):
    switcher = {
        0: "Bending Type 1",
        1: "Bending Type 2",
        2: "Cycling",
        3: "Lying",
        4: "Sitting",
        5: "Standing",
        6: "Walking",

    }
    # get() method of dictionary data type returns
    # value of passed argument if it is present
    # in dictionary otherwise second argument will
    # be assigned as default value of passed argument
    return switcher.get(argument, "nothing")


if __name__ == "__main__":
    #app.run(host='127.0.0.1', port=8001, debug=True)
	app.run(debug=True) # running the app