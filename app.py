# from flask i want to import flask ,render_template,request
from flask import Flask, render_template, request,jsonify

#declare the app
app = Flask(__name__)

#start an app route
@app.route('/')
#declare a function
def main():
    return render_template('app.html')

#form submission route
@app.route('/send', methods=['POST'])
def send():
    if request.method == 'POST':
        # start pulling out data from input form input
        num1 = request.form['num1']
        num2 = request.form['num2']
        num3 = request.form['num3']
    #calculation IF statement  
        units = float(num3)-float(num2)
        if units<=100:
            surcharge=25
            amount = float(units*0.90)
            net_amount = amount+surcharge
            return render_template('app.html',amount=amount , surcharge=surcharge,net_amount=net_amount )
        elif units>100 and units<=300:
            surcharge=35
            amount = float(units*1.50)
            net_amount = amount+surcharge
            return render_template('app.html',amount=amount, surcharge=surcharge,net_amount=net_amount )
        elif units>300 and units<=500:
            surcharge=45
            amount=float(units*2.75)
            net_amount = amount+surcharge
            return render_template('app.html',amount=amount,surcharge=surcharge, net_amount=net_amount)
        else:
            units>500
            surcharge=100
            amount=float(units*4.50)
            net_amount = amount+surcharge
            return render_template('app.html',amount=amount ,surcharge=surcharge, net_amount=net_amount)

        

if __name__ == '__main__':
    app.run(debug=True)                
