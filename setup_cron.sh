#!/bin/bash
# Setup cron job for daily execution (alternative to scheduler.py)

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Create the cron command
CRON_CMD="0 8 * * * cd $SCRIPT_DIR && python3 main.py >> logs/cron.log 2>&1"

# Check if cron job already exists
if crontab -l 2>/dev/null | grep -q "reddit track"; then
    echo "⚠️  Cron job already exists!"
    echo "Current crontab:"
    crontab -l | grep "reddit track"
    echo ""
    read -p "Do you want to replace it? (y/n) " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        exit 0
    fi
    # Remove old entry
    crontab -l | grep -v "reddit track" | crontab -
fi

# Add new cron job
(crontab -l 2>/dev/null; echo "# Reddit Tracker - Daily at 8 AM") | crontab -
(crontab -l 2>/dev/null; echo "$CRON_CMD") | crontab -

echo "✅ Cron job added successfully!"
echo "📅 Will run daily at 8:00 AM"
echo ""
echo "To view: crontab -l"
echo "To remove: crontab -e (then delete the reddit track lines)"
