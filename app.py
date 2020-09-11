from flask import Flask,jsonify
app = Flask(__name__)

@app.route('/electric_bill',methods=['GET,POST'])
def electric_bill(sno,name,old,new):
    if request.methode == 'GET':
        if len(electric_bill)>0:
            return jsonify(electric_bill)
        else:
            'Nothing found',404

    sno=5
    name='moni'
    old=2
    new=2
    units = new-old
    if units<=100:
        amount=units*0.90
        surcharge=25
    elif units>100 and units<=300:
        amount=units*1.50
        surcharge=35
    elif units>300 and units<=500:
        amount=units*2.75
        surcharge=45
    else:
        units>500
        amount=units*4.50
        surcharge=100

    net_amount = amount+surcharge
    print('Electrical information is:')
    print('name of the customer=',name)
    print('older reading=',old)
    print('newer reading=',new)
    print('total no of units=',units)
    print('total payable amount=',netamount)

    return jsonify('electric_bill')
    
if __name__ == '__main__':
    app.run(debug=True)

