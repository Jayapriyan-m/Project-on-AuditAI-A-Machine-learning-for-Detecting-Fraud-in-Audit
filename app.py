from flask import Flask, request, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('rfc.pkl', 'rb'))


@app.route('/', methods=['GET', 'POST'])
def Riskpred():
    if request.method == "POST":
        Sector_score = request.form['sectorScore']
        PARA_A = request.form['paraA']
        Risk_A = request.form['riskA']
        PARA_B = request.form['paraB']
        Risk_B = request.form['riskB']
        TOTAL = request.form['total']
        numbers = request.form['numbers']
        Money_Value = request.form['moneyValue']
        Score_MV = request.form['scoreMv']
        District_Loss = request.form['districtLoss']
        History = request.form['historyScore']
        Score = request.form['score']
        Inherent_Risk = request.form['inherentRisk']
        Audit_Risk = request.form['auditRisk']
        
        pred = [
            [
                float(Sector_score), float(PARA_A), float(Risk_A), float(PARA_B), float(Risk_B),
                float(TOTAL), float(numbers), float(Money_Value), float(Score_MV), float(District_Loss),
                float(History), float(Score), float(Inherent_Risk), float(Audit_Risk)
            ]
        ]
        
        output = model.predict(pred)
        
        return "The Predicted Risk value is: " + str(output[0])
    
    return render_template('main.html')


if __name__ == "__main__":
    app.run(debug=True,port=5001)
