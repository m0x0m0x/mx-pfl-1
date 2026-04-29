#!/usr/bin/env bash

# -------------------------
#  UV Run
# -------------------------

# Error Handling
set -euo pipefail

# Colors
BBLACK='\033[1;90m'
BRED='\033[1;91m'
BGREEN='\033[1;92m'
BYELLOW='\033[1;93m'
BBLUE='\033[1;94m'
BMAGENTA='\033[1;95m'
BCYAN='\033[1;96m'
BWHITE='\033[1;97m'
RESET='\033[0m'

# Commands

hea1() {
	echo -e ""
	echo -e ""
	echo -e "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
	echo -e "$1$"
	echo -e "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
}

# UV Setup

uv_s1() {
	hea1 "UV Setup 1 with Flash"
	uv init .
	uv run main.py
	uv add flask flask-cors routes
	uv tree
}

# --- Execution ---
panty() {
	uv_s1 2>&1 | tee -a sc/logz/r1.sh.txt
}
panty
