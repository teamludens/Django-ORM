update-dependencies:
	poetry update
	poetry export -f requirements.txt > requirements/local.txt --without-hashes --dev
	poetry export -f requirements.txt > requirements/production.txt --without-hashes
