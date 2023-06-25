from flask import Flask,render_template,request
import requests
app = Flask(__name__)
api_key = "3f472bd6f46b69d48173f53952edbec6"
url = "http://data.fixer.io/api/latest?access_key=3f472bd6f46b69d48173f53952edbec6"
@app.route("/",methods = ["GET","POST"])
def index():
    if request.method == "POST":
        firtsCurrency = request.form.get("firstCurrency")
        secondCurrency = request.form.get("secondCurrency")

        amount = request.form.get("amount")

        response = requests.get(url)
        infos = response.json()
        firstValue = infos["rates"][firtsCurrency]
        secondValue = infos["rates"][secondCurrency]

        result = (secondValue/firstValue) * float(amount)
        currencyInfo = dict()

        currencyInfo["firstCurrency"] = firtsCurrency
        currencyInfo["secondCurrency"] = secondCurrency
        currencyInfo["amount"] = amount
        currencyInfo["result"] = result
        return render_template("index.html",info = currencyInfo)
    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)