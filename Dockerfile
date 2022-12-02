FROM fnndsc/python-poetry
WORKDIR .
COPY pyproject.toml poetry.lock /
RUN poetry config virtualenvs.in-project true
RUN poetry install --no-dev
COPY src/ /src/
CMD ["poetry", "run", "uvicorn", "src:app", "--host", "0.0.0.0"]
