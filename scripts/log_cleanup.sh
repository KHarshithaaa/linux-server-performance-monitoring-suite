#!/bin/bash
# Log Cleanup and Retention Automation Script

LOG_DIR="/var/log"
RETENTION_DAYS=7

echo "[$(date)] Running automated log cleanup in $LOG_DIR..."

# Purge logs older than 7 days
find "$LOG_DIR" -type f -name "*.log" -mtime +$RETENTION_DAYS -exec rm -f {} \;

# Truncate active log files larger than 100MB
find "$LOG_DIR" -type f -name "*.log" -size +100M -exec truncate -s 50M {} \;

echo "[$(date)] Log hygiene routine completed."

