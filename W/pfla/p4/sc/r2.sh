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

# -- Commands ---

hea1() {
	echo -e ""
	echo -e ""
	echo -e "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
	echo -e "$1$"
	echo -e "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
}

# -- Endpoint Vars ---

EP1="https://mx-pfla-p4-api.vercel.app/"

# -- Sending one off commands with curl --
c1() {

	declare -a CMD=(

		# Curl command to endpoint
		"curl -I ${EP1}"

	)

	CMDEXEC="${CMD[0]}"
	echo -e "${BBLUE} · · ────── ꒰ঌ·✦·໒꒱ ────── · ·"
	echo -e "${BBLUE} · · ────── Sending Curl Requests ────── · ·"
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

# Loop Commands
c1_l() {

	# Deployed Endpoint
	EP="https://ftut1.vercel.app"

	declare -a CMD=(

		#Test the custom response headers for multiple routes
		"curl -I ${EP}"
		"curl -I ${EP}/pusy"
		"curl -I ${EP}/hello"
		"curl -I ${EP}/hellopg"
		"curl -I ${EP}/customz"
		"curl -I ${EP}/customz2"
		"curl -I ${EP}/customz3"
		"curl -I ${EP}/cu4"

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
	c1 2>&1 | tee -a sc/logz/r2.sh.txt
	# c1_l 2>&1 | tee -a sc/logz/r2.sh.txt

}
panty
