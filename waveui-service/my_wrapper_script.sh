#!/bin/bash

# Start the first process
./waved_process.sh &
  
# Start the second process
./waveui_app_process.sh &
  
# Wait for any process to exit
wait -n
  
# Exit with status of process that exited first
exit $?