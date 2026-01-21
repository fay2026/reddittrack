#!/bin/bash
# Script to run the scheduler in the background

# Get the directory where this script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$SCRIPT_DIR"

# Activate virtual environment if it exists
if [ -d "venv" ]; then
    source venv/bin/activate
fi

# Create logs directory
mkdir -p logs

# Run the scheduler and log output
echo "Starting Reddit Tracker Scheduler..."
echo "Logs will be written to: logs/scheduler.log"

nohup python3 scheduler.py >> logs/scheduler.log 2>&1 &

# Save the PID
echo $! > logs/scheduler.pid

echo "Scheduler started with PID: $(cat logs/scheduler.pid)"
echo "To stop: kill \$(cat logs/scheduler.pid)"
