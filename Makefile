
.PHONY: format
format:
	bash ./scripts/format.sh

db_start:
	@docker start authmanager_db_1
	@docker cp init.sql authmanager_db_1:init.sql
	@echo "Executing databases...wait for 15 seconds"
	@sleep 15
	@docker exec -i authmanager_db_1 sh -c 'mysql -uroot < init.sql'
	@docker-compose up
