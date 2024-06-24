#!/bin/bash

# Execute commands in separate terminal windows
osascript -e 'tell app "Terminal"
    activate
    do script "cd ~/Projects/lsl-workshop/exercises/C_Multichannel-stream &&
    conda activate lsl-ws &&
    python logger.py" 
end tell'

sleep 2

osascript -e 'tell app "Terminal"
    activate
    do script "cd ~/Projects/lsl-workshop/exercises/C_Multichannel-stream &&
    conda activate lsl-ws &&
    python sample_gen.py" 
end tell'