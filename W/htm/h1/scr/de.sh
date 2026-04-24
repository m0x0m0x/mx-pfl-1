#!/usr/bin/env bash

# -------------------------
#  Deployment Script
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

# Sending Curl requests to the Flask Endpoint for testing
dep1() {

	declare -a CMD=(

		#0 -  Serve with bun
		"bun index.html"

	)

	CMDEXEC="${CMD[0]}"
	echo -e "${BBLUE} · · ────── ꒰ঌ·✦·໒꒱ ────── · ·"
	echo -e "${BBLUE} · · ────── Bun Server Page ────── · ·"
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
}

# --- Execution ---
panty() {
	dep1 2>&1 | tee -a scr/logz/dep.sh.txt
}
panty
