from flask import Flask, render_template, request, redirect, session  
app = Flask(__name__)   
app.secret_key = "whatever"

#http://127.0.0.1:5001/

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process', methods=["POST"])
def process():
    session["numStraw"] = int(request.form["numStraw"])
    session["numRasp"] = int(request.form["numRasp"])
    session["numApple"] = int(request.form["numApple"])
    session["items"] = int(request.form["numStraw"]) + int(request.form["numRasp"]) + int(request.form["numApple"]) #Adding the items all together
    session["studentName"] = request.form["studentName"] #grabbing the Students name and ID
    session["studentId"] = request.form["studentId"]
    print("\n================\n",session,"\n================\n")
    return redirect("/checkout") # once the information is stored in session send them the checkout app route

@app.route('/checkout')
def checkout():
    return render_template("checkout.html") #display the html page

@app.route('/<path:path>') #went to the wrong site.
def wrong_path(path):
    return "<h1 style='text-align:center;'>Wrong extension<h1>"

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True, port=5001)    # Run the app in debug mode.