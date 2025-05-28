python3 update.py && python3 -m bot

export PORT=${PORT:-8080}
uvicorn main:app --host 0.0.0.0 --port $PORT
