# DNS PILOT TEST
Used for testing domain name resolution.

DNS PILOT TEST is simple python flask web application used for checking dns name resolution. [ IP to Hostname && Hostname to IP ]

#### Prerequisites:

1. Python3
2. git

#### Python Packege :  

1. waitress 
2. flask_wtf 
3. flask

#### Installation

pip3 install waitress flask_wtf flask

#### How TO run : 

git clone https://github.com/sandeshk06/DNS_PILOT_TEST.git

cd DNS_PILOT_TEST

nohup python3 dns_app.py &


#### Using Docker:

git clone https://github.com/sandeshk06/DNS_PILOT_TEST.git

cd DNS_PILOT_TEST

docker build . -t  dns_pilot_test_v01

docker run -d --name dns_pilot_test -p 5000:5000  dns_pilot_test_v01

#### Verify:
docker ps 

#### Using docker-compose file:

git clone https://github.com/sandeshk06/DNS_PILOT_TEST.git

cd DNS_PILOT_TEST

docker-compose up -d

#### Verify: 

docker-compose ps >> check for container is running or not

 Go to Browser and type : http://127.0.0.1:5000

![Screenshot_2021-11-30 DNS LOOKUP](https://user-images.githubusercontent.com/16614184/144071314-43011264-0111-412e-8c7f-ac1050fdcd9f.png)

### Checking for IP  resolution
![Screenshot_2021-11-30 DNS LOOKUP(1)](https://user-images.githubusercontent.com/16614184/144071593-92e408d3-df6f-4a28-af0e-0a106cab97e9.png)

### Result
![Screenshot_2021-11-30 DNS LOOKUP(2)](https://user-images.githubusercontent.com/16614184/144071804-88afd3c1-ff54-46cf-90ce-12166800b8b2.png)

### Checking for hostname resolution
![Screenshot_2021-11-30 DNS LOOKUP(3)](https://user-images.githubusercontent.com/16614184/144071993-fb1155f3-54e9-4aef-9934-68353bf33ce5.png)

### Result
![Screenshot_2021-11-30 DNS LOOKUP(5)](https://user-images.githubusercontent.com/16614184/144072058-b4e6aacd-ae8a-4717-a00b-7f0f6b831c8a.png)



