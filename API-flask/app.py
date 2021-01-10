import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
<<<<<<< HEAD
=======
    '''
    For rendering results on HTML GUI
    '''
>>>>>>> 41df540936945f933efcd64a15ea6fbddddf219b
    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = round(prediction[0], 2)

    return render_template('index.html', prediction_text='Rank predicted : {}'.format(output))

if __name__ == '__main__':
    model = pickle.load(open("model.pickle", "rb"))
    app.run(debug=True, host='0.0.0.0')