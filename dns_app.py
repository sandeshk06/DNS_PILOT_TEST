from flask import Flask,redirect,url_for,render_template,request
from dns_validator import *
from waitress import serve
from flask_wtf.csrf import CSRFProtect
from werkzeug.utils import secure_filename
import os
secret_key=os.urandom(12)

current_dir=os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(current_dir,'UPLOAD')


ALLOWED_EXTENSIONS = {'txt','text'}

app=Flask(__name__)



app.config['SECRET_KEY']=secret_key
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER





csrf = CSRFProtect(app)

@app.route('/',methods=['GET'])
def home():
                
    return render_template('home.html')

def allowed_file(filename):
    return '.' in filename and  filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS    
    
    
@app.route('/ip',methods=['POST','GET'])
def ip():
    
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        
        file = request.files['file']
        if file.filename == '':
            
            return redirect(request.url)
            
        
        if file and allowed_file(file.filename):
            
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            full_filename_path=os.path.join(app.config['UPLOAD_FOLDER'], filename)
            #check if file is blank
            if os.stat(full_filename_path).st_size ==0 :
                #file is empty
                print("File is empty")
            else:
                IP_LIST=[]
                with open(full_filename_path) as f:
                    
                    for line in f:
                       IP_LIST.append(line)
                       
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
    
     
    if request.method == 'POST':
       hostname_list=[]
       
       if 'file' not in request.files:
           
           return redirect(request.url)
       
       file = request.files['file']
       
       if file.filename == '':
           
           return redirect(request.url)
           
       
       if file and allowed_file(file.filename):
           
           filename = secure_filename(file.filename)
           file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
           full_filename_path=os.path.join(app.config['UPLOAD_FOLDER'], filename)
           
           #check if file is blank
           if os.stat(full_filename_path).st_size ==0 :
                print("file is empty")
           else:
    
    
        
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
