FROM fnndsc/python-poetry
WORKDIR .
COPY pyproject.toml /
COPY poetry.lock /
RUN poetry config virtualenvs.in-project true
RUN poetry install --no-root
COPY ./ /
# RUN poetry run pytest src/tests -s
CMD ["poetry", "run", "uvicorn", "src:app", "--host", "0.0.0.0", "--port=8000"]
