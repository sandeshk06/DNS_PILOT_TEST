# DNS PILOT TEST
Used for testing domain name resolution.

DNS PILOT TEST is simple python flask web application used for checking resolution of forword and reverse entries.

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

#### Using Docker compose file:

git clone https://github.com/sandeshk06/DNS_PILOT_TEST.git

cd DNS_PILOT_TEST

docker-compose up -d

#### Verify: 

docker-compose ps >> check for container is running or not

Go to Browser and type : http://127.0.0.1:5000

