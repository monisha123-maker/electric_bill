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
        name = request.form['name']
        MD = float(request.form['MD'])
        num1 = request.form['num1']
        num2 = request.form['num2']
        num3 = request.form['num3']
        num4 = float(request.form['num4'])
        Solar = request.form['Solar']
        yes = 'yes'
        no = 'no'
    #calculation IF statement  
        units = float(num3)-float(num2)
        if units==0 :
            total_amount = 'nil'
            if MD <=num4:
                G = 'Great! , You have no fine'
            elif MD > num4:
                G = 'oops! , you are charged fine '
                num4 = float(MD)
            if num4==1:
                sanction_load = float(1*60)
            elif num4>1:
                sanction_load = float(1*60)
                next_sanction_charge = float(num4-1)
                sanction_load2 = float(next_sanction_charge*70)
                total_sanction_load = float(sanction_load+sanction_load2)
            net_amount = total_sanction_load+1
            if Solar==yes:
                s = 'Great! , you have a discount for installation of solar'
                bill = float(net_amount-31.06)
            elif Solar==no:
                s = 'Sorry! , you have no discount'
                bill = float(net_amount)
            return render_template('app.html',G=G,name=name,units=units,total_amount=total_amount,total_sanction_load=total_sanction_load,bill=bill,s=s)

        if units<=30 :
            total_amount = float(30*3.7)
            if MD <=num4:
                G = 'Great! , You have no fine'
            elif MD > num4:
                G = 'oops! , you are charged fine '
                num4 = float(MD)
            if num4==1:
                sanction_load = float(1*60)
            elif num4>1:
                sanction_load = float(1*60)
                next_sanction_charge = float(num4-1)
                sanction_load2 = float(next_sanction_charge*70)
                total_sanction_load = float(sanction_load+sanction_load2)
            net_amount = total_amount+total_sanction_load+1
            if Solar==yes:
                s = 'Great! , you have a discount for installation of solar'
                bill = float(net_amount-31.06)
            elif Solar==no:
                s = 'Sorry! , you have no discount'
                bill = float(net_amount)
            return render_template('app.html',G=G,name=name,units=units,total_amount=total_amount,total_sanction_load=total_sanction_load,bill=bill,s=s)
            
        if units>30 :
            amount = float(30*3.7)
            next_amount = float(units-30)
            amount2 = float(next_amount*5.2)
            total_amount = float(amount+amount2)
            if MD <=num4:
                G = 'Great! , You have no fine'
            elif MD > num4:
                G = 'oops! , you are charged fine'
                num4 = float(MD)
            if num4==1:
                sanction_load = float(1*60)
            elif num4>1:
                sanction_load = float(1*60)
                next_sanction_charge = float(num4-1)
                sanction_load2 = float(next_sanction_charge*70)
                total_sanction_load = float(sanction_load+sanction_load2)
            
            net_amount = total_amount+total_sanction_load+1

            if Solar==yes:
                s = 'Great! , you have a discount for installation of solar'
                bill = float(net_amount-31.06)
            elif Solar==no:
                s = 'Sorry! , you have no discount'
                bill = float(net_amount)
            return render_template('app.html',G=G,name=name,units=units,total_amount=total_amount,total_sanction_load=total_sanction_load,bill=bill,s=s)

        

if __name__ == '__main__':
    app.run(debug=True)                
