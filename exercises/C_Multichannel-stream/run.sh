#!/bin/bash

process_id=$1

# Program commands
program2_commands=(
    "python sample_gen.py"
)

program3_commands=(
    "python logger.py"
)

# Execute commands in a new terminal window
execute_in_terminal() {
    title="$1"
    shift
    commands=("$@")

    # Construct the command string
    command_string=$(printf "%s\n" "${commands[@]}")

    # Open a new terminal window and execute the command string
    gnome-terminal --title="$title" -- bash -c "$command_string"
}

# Execute commands in separate terminal windows
execute_in_terminal "Sample Generator" "${program2_commands[@]}"
sleep 2
execute_in_terminal "Logger" "${program2_commands[@]}"