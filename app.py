from flask import Flask, redirect, render_template, url_for
#from dash import Dash, html, dcc
import pandas as pd


#app = Dash(__name__)


app = Flask(__name__)

@app.route("/phenoMine")
def home():
    # Change path of the file according your OS. Mine is Windows
    df = pd.read_excel(".\\static\\data\\PhenotypeData_Pritam.xlsx")
    
    df= df.fillna("NaN")
    
    jsonDF = df.to_dict(orient='records')
    
    dfColumns = df.columns.values
    print(dfColumns)

        
    a = [i.split(" ") for i in dfColumns]
    
    return render_template("PhenoMine.html", dataFrame = jsonDF, columnsdf=a )

#@app.route("/")
#def variant():
#    return render_template("variant.html")

if __name__ == "__main__":
    app.run(debug=True,port=5987)