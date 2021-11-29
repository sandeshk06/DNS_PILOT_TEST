#!/usr/bin/python3
import subprocess
import ipaddress
import socket
import threading
import logging

def valid_ip(address):
    try:
        ipaddress.ip_address(address)
        return True
    except:
        return False

def get_ipresolver_output(ip,IP_STATUS,HOSTNAME):
    try:
        
        STATUS=valid_ip(ip)
        if STATUS == True:
            command="nslookup "+str(ip)+" > /dev/null;echo $? "
            output=subprocess.getoutput(command)
            if output == '0':
                IP_STATUS[ip]="O.K"

                #get hostname from given ip
                hostname=socket.gethostbyaddr(ip)[0]
                HOSTNAME[ip]=hostname

            else:
                IP_STATUS[ip]="FAILED"
                HOSTNAME[ip]="FAILED"
        
        else:
            IP_STATUS[ip]="N/A"
            HOSTNAME[ip]="N/A"
    

    except Exception as e:
        IP_STATUS[ip]="N/A"
        HOSTNAME[ip]="N/A"

def get_nameresolver_output(hostname,IP_LIST):
    try:
        command="nslookup "+str(hostname)+" > /dev/null;echo $? "
        output=subprocess.getoutput(command)
        if output == '0':

            #get ip from given hostname
            ip=socket.gethostbyname(hostname)
            IP_LIST[hostname]=ip

        else:
            IP_LIST[hostname]="FAILED"
    
    except Exception as e:
        logging.error(e)
        IP_LIST[hostname]="FAILED"
        
    
def ip_resolution_check(IP_LIST):
    IP_STATUS={}
    HOSTNAME={}    
        
    try:
        for ip in  IP_LIST:
               
            t=threading.Thread(target=get_ipresolver_output,args=(ip,IP_STATUS,HOSTNAME))
            t.start()
            t.join()
                
        
        return  IP_STATUS,HOSTNAME       
    except Exception as e:
        logging.error(e)
        IP_STATUS={}
        HOSTNAME={}
        return  IP_STATUS,HOSTNAME 
    
    
def hostname_resolution_check(HOSTNAME_LIST):
    try:
        IP_LIST={}        
        for hostname in  HOSTNAME_LIST:
            if hostname =='':
                IP_LIST[" "]="FAILED"
            else:    
                t=threading.Thread(target=get_nameresolver_output,args=(hostname,IP_LIST))    
                t.start()
                t.join()
                    
        return  IP_LIST
            
    except Exception as e:
        logging.error(e)
        IP_LIST={}
            
        return IP_LIST
            
            
