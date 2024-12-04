FROM python:3.12.1-slim as python-base

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1 \
    PYSETUP_PATH="/opt/pysetup" \
    VENV_PATH="/opt/pysetup/.venv"

ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"

# Install dependencies
RUN apt-get update && \
    apt-get install --no-install-recommends -y \
    curl \
    build-essential \
    libpq-dev \
    gcc && \
    rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN pip install poetry

RUN pip install python-decouple


# Create and set working directory
WORKDIR $PYSETUP_PATH

# Copy dependency files
COPY poetry.lock pyproject.toml ./

# Install dependencies
RUN poetry install --no-dev

# Set the working directory for app
WORKDIR /app

# Copy application code
COPY . /app/

# Expose the application port
EXPOSE 8000

RUN ls /app
RUN ls 

# Start the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
