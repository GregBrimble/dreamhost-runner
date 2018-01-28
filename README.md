# DreamHost Runner
Tiny parent application responsible for calling a web application when hosted in DreamHost (specifically, the Shared Hosting plan).     

## Usage
1. In the domain root, e.g. `/home/gregbrimble/boilerplate.gregbrimble.com`, copy this repository `$ git clone git@github.com:GregBrimble/dreamhost-runner.git .`.
2. In a child folder, create/clone the application files (e.g. in `/home/gregbrimble/boilerplate.gregbrimble.com/`, run `$ git clone git@github.com:GregBrimble/boilerplate-web-service.git boilerplate_web_service`).
3. Copy `config.example.py` to `config.py`, and edit as appropriate for the application files.
4. Create a virtual environment for the application e.g. `$ virtualenv -p python3.6 venv`.
5. Install any requirements for the application e.g. `$ . venv/bin/activate && pip install -r boilerplate.gregbrimble.com/requirements.txt && deactivate`.
6. Make sure everything is setup correctly by running `$ python passenger_wsgi.py`.

### `Config.py`
| Variable | Value                                                 |
| -------- | ----------------------------------------------------- |
| PACKAGE  | Applicaton folder name e.g. `boilerplate_web_service` |
| MODULE   | Main application file e.g. `app` from `app.py`        |
| INSTANCE | Flask instance name e.g. `app`                        |
