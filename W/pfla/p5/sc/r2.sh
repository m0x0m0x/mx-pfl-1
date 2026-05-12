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

EP1="https://mx-pfla-p5-api.vercel.app/"
LP1="https://fluffy-telegram-97679qp95pvf4xg-5000.app.github.dev/"

# -- Sending one off commands with curl --
c1() {

	declare -a CMD=(

		# 0 - Curl command to endpoint
		"curl -I ${EP1}"

		# 1 - Curl to check headers - Local Endpoint"
		"curl -I ${LP1}/file_upload"

		# 2 - Curl to check headers - Local Endpoint"
		"curl -I ${EP1}/file_upload"

		# 3 - Curl Loop to check rate limiter EP
		"curl_loop "

	)

	CMDEXEC="${CMD[3]}"
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

# -- Miscellaneous Commands ---

# This Curl loop is being written to test rate limiter functionality
curl_loop() {
	# Make 10 requests to generate rate limit counters
	for i in {1..10}; do
		curl https://mx-pfla-p5-api.vercel.app/
		echo "Request $i done"
	done
}

# Enhanced , this one will also , extract the reponse code and headers
curl_loop2() {
	# Make 10 requests to generate rate limit counters
	for i in {1..10}; do
		# Fetch headers silently, then extract status + rate-limit headers
		response=$(curl -s -I -w "\n%{http_code}" https://mx-pfla-p5-api.vercel.app/)

		# Extract HTTP status code (last line)
		status_code=$(echo "$response" | tail -n1)

		# Extract common rate-limit headers (case-insensitive)
		rate_limit_headers=$(echo "$response" | grep -iE '^x-ratelimit-|^ratelimit-|^x-rate-limit-' | tr -d '\r')

		# Print clean summary
		echo "[$i] Status: $status_code"
		if [ -n "$rate_limit_headers" ]; then
			echo "$rate_limit_headers" | while read -r header; do
				echo "    $(echo "$header" | cut -d: -f1 | tr '[:lower:]' '[:upper:]'): $(echo "$header" | cut -d: -f2- | xargs)"
			done
		else
			echo "    Rate-limit headers: none found"
		fi
		echo ""
	done
}

# --- Execution ---
panty() {
	# c1 2>&1 | tee -a sc/logz/r2.sh.txt
	# c1_l 2>&1 | tee -a sc/logz/r2.sh.txt
	# curl_loop 2>&1 | tee -a sc/logz/r2.sh.txt
	curl_loop2 2>&1 | tee -a sc/logz/r2.sh.txt

}
panty
