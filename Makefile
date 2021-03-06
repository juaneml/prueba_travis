dependences:
	@echo "Makefile microservicio\n"
	@echo "language: python version 3.7 \n"
	@echo "install dependences"

	#npm install npm@latest -g
	npm install npm-install-all -g
	npm install pm2 -g
	pip3 install -r requirements.txt

test: 
	@echo "run tests"
	cd ./test && pytest --cov=test	test.py test_app.py
	cd ./test && coverage run -p --source=test test.py 
	cd ./test && coverage report -m
	cd ./test && coverage xml 
	#--omit=/usr/local/lib/python3.7/* -p test.py 
	cd ./test && coverage run -p --source=test_app test_app.py 
	cd ./test && coverage report -m
	cd ./test && coverage xml -o coverage1.xml
	cd ./test && coverage combine
	cd ./test && coverage xml
	
	  #--omit=/usr/local/lib/python3.7/* -p  
	#cd ./test; coverage combine
	#cd ./test && coverage html 
	##xml

codecov:
	#bash <(curl -s https://codecov.io/bash) -t d0ba6a02-f9f7-44ab-b128-a82396d54280 -f coverage.xml
	cd ./test && bash <(curl -s https://codecov.io/bash) -t d083f686-8673-49f1-8b91-24afe8872f17 -f coverage.xml


ini_ap:
	@echo "Iniciamos la appp puerto 80000"
	cd ./src; pm2 start 'gunicorn proyecto_app:__hug_wsgi__ -b 0.0.0.0:8000' --name proyecto

status:
	@echo "status proyecto"
	pm2 status proyecto

monitor:
	@echo "monitor logs, custom metrics, application information"		
	pm2 monit

stop_app:
	@echo "stop app"
	pm2 stop proyecto 

logs_repo:
	@echo "logs repo"
	git log > logs_repo.txt


delete_app:
	@echo "delete proyecto in pm2"
	pm2 delete proyecto

  	
