fmt:
	black api/ listener/ publisher/ tests/
	isort api/ listener/ publisher/ tests/
	mypy api/ listener/ publisher/ tests/
