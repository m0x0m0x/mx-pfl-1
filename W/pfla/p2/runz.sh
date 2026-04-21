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

# Sending Curl requests to the Flask Endpoint for testing
sendCurl() {

	# Endpoint
	EP="https://fluffy-telegram-97679qp95pvf4xg-5000.app.github.dev/"

	declare -a CMD=(

		#0 -  Install Render Cli -Docs - https://render.com/docs/cli
		"curl https://fluffy-telegram-97679qp95pvf4xg-5000.app.github.dev/"

		#1 -  Testing endpoint
		"curl https://fluffy-telegram-97679qp95pvf4xg-5000.app.github.dev/greet/panty"

		#2 - Testing the route which got deployed on vercel shows index
		"curl https://fluffy-telegram-97679qp95pvf4xg-5000.app.github.dev/index"

	)

	CMDEXEC="${CMD[2]}"
	echo -e "${BBLUE} · · ────── ꒰ঌ·✦·໒꒱ ────── · ·"
	echo -e "${BBLUE} · · ────── Sending Curl Requests ────── · ·"
	echo -e "${BBLUE} · · ────── ꒰ঌ·✦·໒꒱ ────── · ·"
	date
	echo -e "Executing:${BMAGENTA}${CMDEXEC}${RESET}"
	eval "${CMDEXEC}"
	echo -e "${BGREEN}Done!"
	echo -e "───── ⋆⋅☆⋅⋆ ─────${RESET}"
	echo -e "───── ⋆⋅☆⋅⋆ ─────${RESET}"
	echo -e "───── ⋆⋅☆⋅⋆ ─────${RESET}"
}

# --- Execution ---
panty() {
	# uv_s1 2>&1 | tee -a logz/runz.sh.txt
	sendCurl 2>&1 | tee -a logz/runz.sh.txt
}
panty
