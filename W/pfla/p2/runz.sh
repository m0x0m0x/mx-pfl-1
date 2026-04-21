#!/usr/bin/env bash

# -------------------------
#  UV Run
# -------------------------

# Error Handling
set -euo pipefail

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
	hea1 "UV Setup 1 with FastAPI"

	# UC Commands
	CO1="uv run app.py"

	## RUN Above Commands
	echo -e "--- Executing ${CO1} ---"
	eval "$CO1"
	echo -e ""
	echo -e ""
	echo -e ""

}

# --- Execution ---
panty() {
	uv_s1 2>&1 | tee -a logz/rushlogs.txt
}
panty
