from flask import Flask
from flask import flash, render_template, request, url_for, session, redirect
from account import Account, app






@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == 'POST':
        account_number = request.form['account_number']
        
        account = Account.query.filter_by(account_number=account_number).first()
        if account.pin == int(request.form['pin']):
            return redirect(url_for('menu',account_number=account_number))

    return render_template('login.html')


@app.route("/menu/<int:account_number>/")
def menu(account_number):
    account = Account.query.filter_by(account_number=account_number).first()
    return render_template('menu.html', balance=account.balance, account_number=account_number)


#--------------------------------------------------------
