#!/bin/sh
uvicorn api:app --reload --log-level debug --host 0.0.0.0 --port 8080
