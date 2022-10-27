# Datahub

Datahub is an example application for receiving state events from internet of things connected devices and then publishing their history to other consumers.


## Initial setup

Create a python virtual environment, activate it and install the required packages from the requirements file.

    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt

Install the datahub code itself in development mode so that changes are available as they are iterated on.

    pip install -e .


## Running tests

This project uses pytest. After initial setup is complete, you can run tests with the pytest command.

    pytest