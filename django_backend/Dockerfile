FROM python:3.10-slim-buster

ARG APP_UID
ENV APP_UID=${APP_UID:-1000}
ARG APP_GID
ENV APP_GID=${APP_GID:-1000}

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .
RUN pip install --upgrade pip
RUN apt-get update && \
    apt-get install -y build-essential libcairo2-dev pkg-config python3-distutils-extra python3-distutils python3-apt libsystemd-dev libdbus-1-3 libdbus-1-dev libcups2-dev libgirepository1.0-dev python3-dev
RUN apt-get update -y && apt upgrade -y

RUN whoami
RUN groupadd -g ${APP_GID} django_user
RUN useradd -u ${APP_UID} -g ${APP_GID} -m django_user
USER django_user
RUN whoami
# RUN update-alternatives --install /usr/bin/python python /usr/bin/python3.10 4
RUN pip install --upgrade pip setuptools
# Install project dependencies

RUN pip install --no-cache-dir -r requirements.txt

# Copy the Django project code into the container
COPY . .

# Expose the default Django development server port
EXPOSE 4100

# Run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:4100"]