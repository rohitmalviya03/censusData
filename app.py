from atexit import register
import io
from flask import Flask,render_template,Response,request,send_file
import io
import base64
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import numpy as np
import seaborn as sns
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import io
import base64
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import matplotlib.pyplot as plt
import seaborn as sns
app = Flask(__name__)


df = pd.read_csv("censusdata.csv")
@app.route('/showdataset')
def showdataset():
    df = pd.read_csv("censusdata.csv")
    
    return render_template('dashboard.html',  tables=[df.to_html(classes='data')], titles=df.columns.values)

@app.route('/')
def index():
      return render_template('index.html')
@app.route('/getcity')
def getcity():
        State = request.form.get("State")
        District = request.form.get("District")
        print(State)
        status = df[df['State_name'] == State][['District_name']]
        print(status)
        return render_template('District.html',district=status)

    
class state(object):
    @app.route('/getregiondata' ,methods=['GET', 'POST'])
    def getregiondata():
        data= pd.read_csv("censusdata.csv")
        data.dtypes
    # df['date']=pd.to_datetime(df['date'])
    # df['Year'] = df['date'].dt.year
    # df['day'] = df['date'].dt.day
    # df['Week'] = df['date'].dt.week
    # df['Month']  = df['date'].dt.month_name()
    # df['dayname'] = df['date'].dt.day_name() 
        State = request.form.get("State")
        District = request.form.get("District")
        print(State)
        status = data[data['State_name'] == State][['Population','Male','Female']]
        edu=data[data['State_name']==State][['Secondary_Education', 'Higher_Education', 'Graduate_Education']]
        df[df['State_name'] == State][['District_name']]
        print(df['Distri bn   ct_name'])


        
        # District =data[(data.State_name==State)&(data.District_name==District)][['Population','Male','Female']]
        # print(status)
        # print(District)
    
    
        # df_2019=df[df['Year']=='2019']
    
        fig,ax=plt.subplots(figsize=(6,6))
        ax=sns.set(style="darkgrid")
        x=sns.lineplot(data= status)
        x.set_xlabel(State, fontsize = 15)
        # sns.lineplot(status.Deaths)
        canvas=FigureCanvas(fig)
        img = io.BytesIO()
        fig.savefig(img)
        img.seek(0)

        fig1,ax1=plt.subplots(figsize=(6,6))
        ax1=sns.set(style="darkgrid")
        
        sns.barplot(data= status)
        # sns.lineplot(status.Deaths)
        canvas=FigureCanvas(fig1)
        img1 = io.BytesIO()
        fig1.savefig(img1)
        img1.seek(0)

        fig2,ax2=plt.subplots(figsize=(6,6))
        ax2=sns.set(style="darkgrid")
        
        sns.barplot(data= edu)
        # sns.lineplot(status.Deaths)
        canvas=FigureCanvas(fig2)
        img2 = io.BytesIO()
        fig2.savefig(img2)
        img2.seek(0)          
        plot_url = base64.b64encode(img.getvalue()).decode('utf8')
        Districtgraph=base64.b64encode(img1.getvalue()).decode('utf8')
        edu=base64.b64encode(img2.getvalue()).decode('utf8')
        return render_template('us.html' , alg=status,plot_url=plot_url,Districtgraph=Districtgraph,edu=edu,District=df)




if __name__ == "__main__":
    app.run(debug=True)