##############################################
# Programmer: Aaron Miller
# Fetch Rewards Project
# 8/6/22
# Description: This file houses the flask file for creating a flask web service and handling the front end of the application
##############################################

from urllib import request
import utils
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        rows = int(request.form["rows"])
        cols = int(request.form["cols"])

        corners = []
        corners.append((float(request.form["corner1-x"]), float(request.form["corner1-y"])))
        corners.append((float(request.form["corner2-x"]), float(request.form["corner2-y"])))
        corners.append((float(request.form["corner3-x"]), float(request.form["corner3-y"])))
        corners.append((float(request.form["corner4-x"]), float(request.form["corner4-y"])))

        sol = utils.find_image_points(rows, cols, corners)
        return render_template('solution.html', solution=sol)
    
    return render_template('main.html')

if __name__ == "__main__":
    app.run()
