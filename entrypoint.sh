#!/bin/bash

# Start the socket listener in the background
curl -N https://stream.wikimedia.org/v2/stream/recentchange | nc -l -p 9999 &

# Start your PySpark job
python3 main.py
