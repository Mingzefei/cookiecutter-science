.PHONY: data backup_data backup_results backup paper clean_data clean_results clean


# main targets
#
data:
	# TODO
	#

backup_data:
	@BACKUP_DIR_TIME="backup/data_$(shell date +%m%d%H%M%S)"
	mkdir -p $$BACKUP_DIR_TIME
	cp -r data $$BACKUP_DIR_TIME
	# TODO
	@echo "backup data in $$BACKUP_DIR_TIME"

backup_results:
	@BACKUP_DIR_TIME="backup/results_$(shell date +%m%d%H%M%S)"
	mkdir -p $$BACKUP_DIR_TIME
	cp -r results $$BACKUP_DIR_TIME
	# TODO
	@echo "backup results in $$BACKUP_DIR_TIME"

backup: backup_data backup_results

paper:
	cd reports && make clean && make

clean_data:
	cd data && rm -rf interim/* processed/* raw/*

clean_results:
	cd results && rm -rf *

clean: clean_data clean_results
	cd bin && rm -rf *
	cd reports && make clean



