from flask import Flask,redirect,url_for,render_template,request
from dns_validator import *
from waitress import serve
from flask_wtf.csrf import CSRFProtect
import os
secret_key=os.urandom(12)

app=Flask(__name__)
app.config['SECRET_KEY']=secret_key


csrf = CSRFProtect(app)

@app.route('/',methods=['GET'])
def home():
                
    return render_template('home.html')

@app.route('/ip',methods=['POST','GET'])
def ip():
    
    if request.method == 'POST':
        ip_address=request.form.get('address')
        IP_LIST=ip_address.split(",")
        failed_counter=0
        if IP_LIST:
            
            ip_status,hostname_list=ip_resolution_check(IP_LIST)
            for value in ip_status.values():
                if value =='FAILED' or value =='N/A':
                    failed_counter=failed_counter+1
            return render_template('show_ip_result.html',IP_STATUS=hostname_list,FAILED_COUNT=failed_counter)
    return render_template('ip.html')

@app.route('/name',methods=['POST','GET'])
def name():
    fqdn=request.form.get('hostname') 
    if request.method == 'POST':
        hostname_list=fqdn.split(",")
        failed_counter=0
        if hostname_list:
            IP_STATUS=hostname_resolution_check(hostname_list)
            for value in IP_STATUS.values():
                if value =='FAILED' or value =='N/A':
                    failed_counter=failed_counter+1

            return render_template('show_name_result.html',IP_STATUS=IP_STATUS,FAILED_COUNT=failed_counter)            
        else:
            return render_template('name.html')

    return render_template('name.html')




if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    #app.run(port=5000,debug=True)
    serve(app,port=5000,threads=100)
