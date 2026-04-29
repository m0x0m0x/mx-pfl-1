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

# Oneoff Coommands

oneOFF() {

	declare -a CMD=(

		#0 -  View all routes
		"uv run flask routes"

	)

	CMDEXEC="${CMD[0]}"
	echo -e "${BBLUE} · · ────── ꒰ঌ·✦·໒꒱ ────── · ·"
	echo -e "${BBLUE} · · ────── One OFf Commands ────── · ·"
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

# Sending Curl requests to the Flask Endpoint for testing
sendCurl() {

	# Endpoint
	EP="https://ftut1.vercel.app"
	DP="https://fluffy-telegram-97679qp95pvf4xg-5000.app.github.dev"

	declare -a CMD=(

		#0 -  Install Render Cli -Docs - https://render.com/docs/cli
		"curl ${EP}"

		#1 -  Testing endpoint
		"curl ${EP}/greet/panty"

		#2 - Testing URL Handle Params
		"curl ${EP}/handle_url_params?name=panty&age=18"

		#3 - Testing post method
		"curl -X POST ${DP}/hello"

		#4 - Testing post with post to see error
		"curl ${DP}/hello"

		#5 - hellopg endpoint
		"curl -X POST ${DP}/hellopg"

		#6 - hellopg put request
		"curl -X PUT ${DP}/hellopg"

		#7 - hellopg put request in deployed EP
		"curl -X PUT ${EP}/hellopg"

		#8 - Custom End Point - Redirects to image
		"curl ${EP}/customz"

		#9 - Custom End Point - Displays Image in Page
		"curl ${EP}/customz2"

		#10 - Testing endpoint /hellopg unknown request
		"curl -X DELETE ${DP}/hellopg"

		#11 - Get the Response header
		"curl -I ${DP}/cu4"

		#12 - Get the Response header for custom route
		"curl -I ${DP}/customz3"

		#13 - Get the response header from deployed route
		"curl -I ${EP}/customz3"

		#14 - Get the response header from deployed route
		"curl -I ${EP}/cu4"

		#15 - Get the response header from localroute
		"curl -I ${DP}/cu5"

		#16 - Get the response header from deployed route
		"curl -I ${EP}/cu5"

		#17 - Custom Response on local deployed route
		"curl -I ${DP}/cu6"

	)

	CMDEXEC="${CMD[17]}"
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
}

# Sending multiple curl commands
se_cu_lo() {

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
	done
}

# --- Execution ---
panty() {
	oneOFF 2>&1 | tee -a scr/logz/r2.sh.txt
	# sendCurl 2>&1 | tee -a scr/logz/r2.sh.txt
	# se_cu_lo 2>&1 | tee -a scr/logz/r2.sh.txt
}
panty
