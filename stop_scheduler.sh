#!/bin/bash
# Script to stop the scheduler

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
PID_FILE="$SCRIPT_DIR/logs/scheduler.pid"

if [ -f "$PID_FILE" ]; then
    PID=$(cat "$PID_FILE")
    echo "Stopping scheduler (PID: $PID)..."
    kill $PID 2>/dev/null
    rm "$PID_FILE"
    echo "Scheduler stopped."
else
    echo "No scheduler PID file found. Is it running?"
fi
