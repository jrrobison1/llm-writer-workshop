FROM python:3.10-slim

WORKDIR /app

# Install Poetry
RUN pip install poetry

# Copy the pyproject.toml and poetry.lock files
COPY service/pyproject.toml service/poetry.lock ./

# Install dependencies
RUN poetry config virtualenvs.create false \
  && poetry install --no-dev

# Copy the rest of the application code
COPY service/ .

# Expose the port the app runs on
EXPOSE 5000

# Set the entrypoint command
CMD ["poetry", "run", "python", "app.py"]