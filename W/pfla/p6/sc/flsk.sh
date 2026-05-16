#!/usr/bin/env bash

# -------------------------
#  flask.sh - Flask running commands
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

# -- Commands ---

hea1() {
	echo -e ""
	echo -e ""
	echo -e "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
	echo -e "$1$"
	echo -e "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
}

# -- Sending one off commands with flask --
fl1() {

	declare -a CMD=(

		# 0 - Flask cli help
		"uv run flask --help"

		# 1 - Flask see routes
		"uv run flask routes"

		# 2 - Flask limiter help
		"uv run flask limiter --help"

	)

	CMDEXEC="${CMD[2]}"
	echo -e "${BBLUE} · · ────── ꒰ঌ·✦·໒꒱ ────── · ·"
	echo -e "${BBLUE} · · ────── flask cli Requests ────── · ·"
	echo -e "${BBLUE} · · ────── ꒰ঌ·✦·໒꒱ ────── · ·"
	date
	echo -e "Executing:${BMAGENTA}\n${CMDEXEC}\n${RESET}"
	echo -e "///////////"
	eval "${CMDEXEC}"
	echo -e "\n///////////"
	echo -e "${BGREEN}\nDone!"
	echo -e "───── ⋆⋅☆⋅⋆ ─────${RESET}"
	echo -e "───── ⋆⋅☆⋅⋆ ─────${RESET}"
	echo -e "───── ⋆⋅☆⋅⋆ ─────${RESET}"
	echo
	echo
	echo
}

# Loop Commands with flask
fl2() {

	declare -a CMD=(

		# Get the limiter Config
		"uv run flask limiter config"

		# Get the limiter Config
		"uv run flask limiter limits"

	)

	for CMDEXEC in "${CMD[@]}"; do
		echo -e "${BBLUE}────── ꒰ঌ·✦·໒꒱ ──────${RESET}"
		echo -e "${BBLUE}────── Curl -I on Deployed endpoints ──────${RESET}"
		echo -e "${BBLUE}────── ꒰ঌ·✦·໒꒱ ──────${RESET}"
		echo -e "Executing: ${CMDEXEC}"
		eval "${CMDEXEC}"
		echo -e "${BGREEN}Done!${RESET}"
		echo -e "${BBLUE}───── ⋆⋅☆⋅⋆ ─────${RESET}"
		echo -e "${BBLUE}───── ⋆⋅☆⋅⋆ ─────${RESET}"
		echo -e "${BBLUE}───── ⋆⋅☆⋅⋆ ─────${RESET}"
		echo # Add blank line between commands
		echo # Add blank line between commands
		echo # Add blank line between commands
	done
}

# --- Execution ---
panty() {
	# fl1 2>&1 | tee -a sc/logz/flsk.sh.txt
	fl2 2>&1 | tee -a sc/logz/flsk.sh.txt

}
panty
