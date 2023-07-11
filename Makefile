fmt:
	black api/ listener/ publisher/ tests/ utils/
	isort api/ listener/ publisher/ tests/ utils/
	mypy api/ listener/ publisher/ tests/ utils/
