FROM fnndsc/python-poetry
COPY COPY pyproject.toml /
COPY poetry.lock /
WORKDIR .
RUN poetry config virtualenvs.in-project true
RUN poetry install --no-root
COPY ./ /
EXPOSE 8000
CMD ["poetry", "python3", "uvicorn", "main:app", "--host", "0.0.0.0"]