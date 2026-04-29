#!/usr/bin/env bash

# -------------------------
#  Upload to vercel production and run run git push commands
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

# Upload Operations
up_1() {

	declare -a CMD=(

		# First Perform git push
		"../../../g"

		# docs vercel prod
		"pwd && cd doc && vercel --prod"

		# Then Main app upload which is on root
		"pwd && vercel --prod"

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
	up_1 2>&1 | tee -a scr/logz/upz.sh.txt
}
panty
