#!/bin/sh
source .venv/bin/activate
uvicorn main:app --host 0.0.0.0 --port $PORT --reload