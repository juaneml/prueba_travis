dependences:
	echo "Makefile microservicio\n"
	echo "language: python version 3.7 \n"
	echo "install dependences"
	npm install -g n
	npm install pm2 -g
	pip3 install -r requirements.txt
	
test: 
	echo "run tests"
	cd ./test && pytest -v test.py
	cd ./test && coverage run --source=test test.py 
	cd ./test && coverage report -m
	cd ./test && coverage xml
codecov:
	bash <(curl -s https://codecov.io/bash) -t d0ba6a02-f9f7-44ab-b128-a82396d54280 -f coverage.xml

ini_ap:
	cd ./src && pm2 start 'gunicorn proyecto-dep-app:__hug_wsgi__' --name proyecto
	#cd ./src/ && pm2 start  'gunicorn proyecto-dep-app:__hug_wsgi__ -b 0.0.0.0:8000 -w 2' --name proyecto
	#pm2 start  'gunicorn proyecto-dep-app: -b 0.0.0.0:8000 -w 3' --name proyecto
status:
	echo "status proyecto"
	pm2 status proyecto

monitor:
	echo "monitor logs, custom metrics, application information"		
	pm2 monit

stop_app:
	echo "stop app"
	pm2 stop proyecto 

logs_repo:
	echo "logs repo"
	git log > logs_repo.txt


delete_app:
	echo "delete proyecto in pm2"
	pm2 delete proyecto

  	
