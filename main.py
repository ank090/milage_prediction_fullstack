from flask import Flask,render_template,request
import pickle

app=Flask(__name__)
reg = pickle.load(open('./static/regressor.pkl','rb'))
sc = pickle.load(open('./static/scaler.pkl','rb'))
result=None

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict',methods=['GET','POST'])
def predict():
    if request.method=="POST":

     result=reg.predict(sc.transform([[int(request.form.get("cylinder")),(16.387*int(request.form.get("disp"))),int(request.form.get("hp")),(2.205*int(request.form.get("weight"))),(0.618*int(request.form.get("acc"))),int(request.form.get("year")),int(request.form.get("origin"))]]))
     return render_template('predict_page.html',Milage=(result*0.425143707))
    return render_template('predict_page.html')



if __name__=="__main__":
    app.run(debug=True)