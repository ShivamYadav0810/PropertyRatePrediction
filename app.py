from flask import Flask, render_template, request
app = Flask(__name__)
from flask import Flask,render_template,url_for,request
import pandas as pd 
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import sklearn.externals as extjoblib
import joblib
import pickle
from sklearn.linear_model import Lasso
from sklearn.model_selection import train_test_split
import pandas as pd
from datetime import date
import requests

filename = 'property_model.pkl'
clf = pickle.load(open(filename, 'rb'))

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/predict',methods=['POST'])
def predict():
	if request.method == 'POST':
		li=[]
		area = request.form['area']
		li.append(float(area))
		Type = request.form['type']
		if Type=="0":
			li.append(0)
		elif Type=="1":
			li.append(1)
		bhk = request.form['bhk']
		li.append(float(bhk))
		per_sqft = request.form['per_sqft']
		li.append(float(per_sqft))
		parking = request.form['parking']
		li.append(float(parking))
		status = request.form['status']
		if status=="0":
			li.append(0)
		elif status=="1":
			li.append(1)
		bathroom = request.form['bathroom']
		li.append(float(bathroom))
		transaction = request.form['transaction']
		if transaction=="0":
			li.append(0)
		elif transaction=="1":
			li.append(1)
		furnishing = request.form['furnishing']
		if furnishing=="0":
			li.append(0)
		elif furnishing=="1":
			li.append(1)
		elif furnishing=="2":
			li.append(2)
		my_prediction = clf.predict([li])
		print(type(my_prediction[0]))

		

	return render_template('predict.html',prediction = my_prediction[0]/10)
 
if __name__ == '__main__':
	app.run(debug=True)