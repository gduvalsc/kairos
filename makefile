VERSION=8.0
PORT=44380
IMAGE=kairos
#IMAGE=gdsc/kairos:$(VERSION)
MACHINE=kairos$(VERSION)
NETWORK=mynetwork

USERNAME=gduvalsc
PASSWORD=************
TOKEN=$$(curl -s -H "Content-Type: application/json" -X POST -d '{"username": "$(USERNAME)", "password": "$(PASSWORD)"}' https://hub.docker.com/v2/users/login/ | jq -r .token)

### Things to do before delivering a new image
# e) make a new branch under git with version number
# f) make deliver (suppose that make image has been done before)

image: ressources pydist
	cd buildimage && docker build -f kairos.docker -t $(IMAGE) .
	docker images

optimize:
	docker save -o /tmp/$(IMAGE).tar $(IMAGE)
	docker rmi $(IMAGE)
	docker load -i /tmp/$(IMAGE).tar
	rm /tmp/$(IMAGE).tar
	docker images

machine:
	docker create -it --name $(MACHINE) -h $(MACHINE) -p $(PORT):443 -v /Users/gdsc/Documents/kairos/$(VERSION)/data:/postgres/data -v /Users/gdsc/Documents/kairos/export:/export -v /Users/gdsc/Documents/kairos/$(VERSION)/autoupload:/autoupload $(IMAGE)
	docker network connect $(NETWORK) $(MACHINE)

monitoring:
	docker exec $(MACHINE) su - postgres -c 'psql -c "create database kairos"'
	docker exec $(MACHINE) su - postgres -c 'psql -d kairos -c "create extension plpython3u"'
	docker exec $(MACHINE) su - postgres -c 'psql -d kairos -c "create extension pgkairos"'

deliver:
	docker tag kairos gdsc/kairos:latest
	docker push gdsc/kairos:latest
	docker tag kairos gdsc/kairos:$(VERSION)
	docker push gdsc/kairos:$(VERSION)

start:
	docker start $(MACHINE)

sh:
	docker exec -it $(MACHINE) bash

stop:
	docker exec $(MACHINE) su - postgres -c 'pg_ctl stop'
	docker stop $(MACHINE)

abort:
	docker stop $(MACHINE)

rm:
	docker rm $(MACHINE)

boot:
	docker cp objects $(MACHINE):/tmp
	docker exec $(MACHINE) su - postgres -c 'pg_ctl stop'
	docker exec $(MACHINE) sh -c 'python3 -m pykairos --makeboot'
	docker cp $(MACHINE):/postgres/backups/pgboot.tar .

pydist:
	cd kairosx && python setup.py sdist
	cp kairosx/dist/* buildimage

quick: ressources pydist
	docker cp buildimage/resources.tar.gz $(MACHINE):/
	docker exec $(MACHINE) sh -c 'cd /; tar xzf resources.tar.gz; rm *.gz;'
	docker cp buildimage/pykairos* $(MACHINE):/kairosx
	docker exec $(MACHINE) sh -c 'cd /kairosx; tar xzf pykairos*; rm *.gz; cd pykairos*; pip3 install --upgrade .; cd ..;rm -fr pykairos*; rm -f /var/log/kairos/*.log'


ressources:
	rm -fr buildimage; mkdir buildimage
	rm -fr kairosx; mkdir kairosx
	cp -r resources  pykairos kairos.key kairos.crt index.html worker.py kairosx
	cp instantclient-basic-linux.zip instantclient-sdk-linux.zip oracle_fdw-2.2.1.tar.gz buildimage
	cp pgkairos-1.3-1.noarch.rpm buildimage
	cp pgboot.tar buildimage
	sed -e 's/@@VERSION@@/$(VERSION)/' client.js > kairosx/client.js
	sed -e 's/@@VERSION@@/$(VERSION)/' kairos > kairosx/kairos
	sed -e 's/@@VERSION@@/$(VERSION)/' setup.py > kairosx/setup.py
	sed -e 's/@@VERSION@@/$(VERSION)/' pykairos/__main__.py > kairosx/pykairos/__main__.py
	sed -e 's/@@VERSION@@/$(VERSION)/' kairos.docker > buildimage/kairos.docker
	tar czf buildimage/resources.tar.gz kairosx/kairos.key kairosx/kairos.crt kairosx/resources kairosx/index.html kairosx/client.js kairosx/kairos kairosx/worker.py

clean:
	rm -fr kairosx buildimage
	docker rmi $$(docker images -f 'dangling=true' -q)

nonreg:
	cd ../KAIROSTESTS && py.test --capture=fd -v startup.py
	cd ../KAIROSTESTS && py.test --capture=fd -v test.py

remove:
	curl "https://hub.docker.com/v2/repositories/gdsc/kairos/tags/$(VERSION)/" -X DELETE -H "Authorization: JWT ${TOKEN}"
