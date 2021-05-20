from flask import Flask, request ,render_template , jsonify
from pymongo import MongoClient

app=Flask("myapp")
@app.route('/form')
def myform():
    return render_template("form.html")
    


@app.route('/result',methods=['POST'])
def mydata():
    if request.method=='POST':
#       global data1
       name=request.form.get('z1')
       age=request.form.get('z2')
       area=request.form.get('z3')
       spo2=request.form.get('z4')
       o2=request.form.get('z5')
       positive=request.form.get('z6')
       mob=request.form.get('z7')
       bg=request.form.get('z8')
       requirements=request.form.get('z9')
       


       db=[
         {
        "Patient Name": name,
        "Patient Age": age,
        "Area / Location": area,
        "SPO2 Level": spo2,
        "Is patient on oxygen cylinder? Yes / No": o2,
        "COVID-19 Result (+ve/-ve/Awaiting)": positive,
        "Attender's Mobile Number": mob,
        "Blood Group": bg,
        "Requirements": requirements
          }
            ]
       client= MongoClient("mongodb://127.0.0.1:27017")
       client['covid']['Requirements'].insert(db)

 

    return render_template("notify.html")





app.run(port=1234,debug=True)