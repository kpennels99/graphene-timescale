# define the name of the virtual environment directory

.PHONY: all start logs stop drop

all: start ## default target

help: ## print help messages
	@sed -n 's/^\([a-zA-Z_-]*\):.*## \(.*\)$$/\1 -- \2/p' Makefile

start: ## startup containers
	docker-compose up -d

import: ## import and join data
	chmod +x ./docker_scripts/db_imports.sh 
	./docker_scripts/db_imports.sh

logs: ## View container logs 
	docker-compose logs -f --tail=20

stop: ## Stop all runniing containers
	docker-compose down
	
drop: ## Delete associate volumes when stopping containers
	docker-compose down -v

clean-cached-python: ## Delete all *.pyc files
	find . -type f -name '*.pyc' -delete