from flask import Flask, request, render_template
from distutils.log import debug
from fileinput import filename
from flask import *  
import cv2
import numpy as np
from skimage import io

app = Flask(__name__)
@app.route('/')  
def main():  
    return render_template("index.html")

@app.route("/success",methods = ["GET","POST"])
def gfg():
    if request.method == "POST":
        name = request.form.get("name")
        img1 = request.form.get("img")
        img = cv2.imread(img1)
        f = 1
        if img is None:
            f = 0
        if(f):
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(img, name, (230, 200), font, 2.3, (0, 0, 255), 2, cv2.LINE_AA)
            cv2.imwrite("new.jpg", img)
    if(f):
        return "Successful Check your directory"
    else :
        return "You didn't upload the image"




if __name__=='__main__':
    app.run(debug=True)