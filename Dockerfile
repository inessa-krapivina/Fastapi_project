FROM fnndsc/python-poetry
WORKDIR .
COPY pyproject.toml poetry.lock /
RUN poetry config virtualenvs.in-project true
RUN poetry install --no-root
COPY crm / /
# RUN poetry run pytest src/tests -s
CMD ["poetry", "run", "uvicorn", "src:app", "--host", "0.0.0.0"]
