FROM python:3.8-slim

# Setup env
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONFAULTHANDLER 1

# Compilation dependencies
RUN pip install poetry
RUN apt-get update && apt-get install -y --no-install-recommends gcc

# Install python dependencies in /.venv
COPY pyproject.toml .
COPY poetry.lock .
RUN poetry install

# Install application into container
COPY . .

# Run the executable
ENTRYPOINT ["poetry run python", "-m", "yaml2jsonnet"]
CMD ["--help"]
