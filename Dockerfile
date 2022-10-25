FROM fnndsc/python-poetry
WORKDIR .
COPY pyproject.toml /
COPY poetry.lock /
RUN poetry config virtualenvs.in-project true
RUN poetry install --no-root
COPY ./ /
CMD ["poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port=8000"]