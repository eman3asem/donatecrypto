# !/bin/sh
source .venv/bin/activate
python -m flask --app main run -p $PORT --debug

#!/bin/bash

export FLASK_APP=main.py
export FLASK_ENV=development
export FLASK_DEBUG=1

# Start Flask server
flask run