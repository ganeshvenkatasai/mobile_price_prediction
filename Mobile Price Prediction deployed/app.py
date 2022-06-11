from flask import Flask, render_template, request
import pickle
import numpy as np



app = Flask(__name__)


@app.route('/')
def man():
   return render_template('app.html')

@app.route('/predict', methods=['POST'])
def home():


    df1=''
    df3=''
    df5=''
    df7=''
    df8=''
    df9=''
    df10=''
    df11=''
    df12=''
    df13=''
    df14=''
    df15=''
    df16=''
    df17=''


    try:
        data1 = request.form['a']
    except:
        df1='(Default value)'
        data1 = 4000
    try:
        data3 = request.form['c']
    except:
        df3='(Default value)'
        data3 = 2
    try:
        data5 = request.form['e']
    except:
        df5='(Default value)'
        data5 = 8
    try:
        data7 = request.form['g']
    except:
        df7='(Default value)'
        data7 = 64
    try:
        data8 = request.form['h']
    except:
        df8='(Default value)'
        data8 = 1
    try:
        data9 =request.form['i']
    except:
        df9='(Default value)'
        data9 = 165
    try:
        data10 = request.form['j']
    except:
        df10='(Default value)'
        data10 = 8
    try:
        data11 = request.form['k']
    except:
        df11='(Default value)'
        data11 = 48
    try:
        data12 = request.form['l']
    except:
        df12='(Default value)'
        data12 = 1920
    try:
        data13 = request.form['m']
    except:
        df13='(Default value)'
        data13 = 1080
    try:
        data14 = request.form['n']
    except:
        df14='(Default value)'
        data14 = 8
    try:
        data15 = request.form['o']
    except:
        df15='(Default value)'
        data15 = 50.8
    try:
        data16 = request.form['p']
    except:
        df16='(Default value)'
        data16 = 28.5
    try:
        data17 = request.form['q']
    except:
        df17='(Default value)'
        data17 = 10

    df=[df1,df3,df5,df7,df8,df9,df10,df11,df12,df13,df14,df15,df16,df17]








    data2=1
    data4=1
    data6=1
    data18=1
    data19=1
    data20=1
    li2='yes'
    li4='yes'
    li6='yes'
    li18='yes'
    li19='yes'
    li20='yes'

    if (request.form['b']=='1'):
        data2=1
    if (request.form['b']=='0'):
        data2=0
    if (request.form['d']=='1'):
        data4=1
    if (request.form['d']=='0'):
        data4=0
    if (request.form['f']=='1'):
        data6=1
    if (request.form['f']=='0'):
        data6=0
    if (request.form['r']=='1'):
        data18=1
    if (request.form['r']=='0'):
        data18=0
    if (request.form['s']=='1'):
        data19=1
    if (request.form['s']=='0'):
        data19=0
    if (request.form['t']=='1'):
        data20=1
    if (request.form['t']=='0'):
        data20=0


    text =np.array([[data1, data2, data3, data4, data5, data6, data7, data8, data9, data10, data11, data12, data13, data14, data15,
      data16, data17, data18, data19,data20]],dtype='float32')
    model = pickle.load(open('iri.pkl', 'rb'))
    data = model.predict(text)
    data=np.ceil(data*10000)[0]


    if (data2==0):
        li2='Not available'
    if (data2==1):
        li2='Available'

    if (data4==0):
        li4='Not available'
    if (data4==1):
        li4='Available'

    if (data6==0):
        li6='Not available'
    if (data6==1):
        li6='Available'

    if (data18==0):
        li18='Not available'
    if (data18==1):
        li18='Available'

    if (data19==0):
        li19='Not available'
    if (data19==1):
        li19='Available'

    if (data20==0):
        li20='Not available'
    if (data20==1):
        li20='Available'




    li=[data1, li2, data3, li4, data5, li6, data7, data8, data9, data10, data11, data12, data13, data14, data15,
      data16, data17, li18, li19,li20]


    return  render_template( 'after.html',data=data,datas=li,d=df)


if __name__ == "__main__":
    app.run(debug=True)













