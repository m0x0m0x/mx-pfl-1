#!/usr/bin/env bash

#---------------------------------
#  Bash script to run some installs
#---------------------------------

# /// Housekeeping ///

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

# /// Variables ///

# /// Functions ///

# Function Single
pussy1() {
	declare -a CMD=(

		#0 -  Install Render Cli -Docs - https://render.com/docs/cli
		"curl -fsSL https://raw.githubusercontent.com/render-oss/cli/refs/heads/main/bin/install.sh | sh"

		#1 -  Install Vercel Cli -Docs - https://vercel.com/docs/cli?package-manager=bun
		"bun add -g vercel"

		#2 - Witr Installation - Tool fo understanding process -https://github.com/pranshuparmar/witr
		"curl -fsSL https://raw.githubusercontent.com/pranshuparmar/witr/main/install.sh | bash"

	)

	CMDEXEC="${CMD[2]}"
	echo -e "${BBLUE} · · ────── ꒰ঌ·✦·໒꒱ ────── · ·"
	echo -e "${BBLUE} · · ────── PantySmellling ────── · ·"
	echo -e "${BBLUE} · · ────── ꒰ঌ·✦·໒꒱ ────── · ·"
	date
	echo -e "Executing:${BMAGENTA}${CMDEXEC}${RESET}"
	eval "${CMDEXEC}"
	echo -e "${BGREEN}Done!"
	echo -e "───── ⋆⋅☆⋅⋆ ─────${RESET}"
	echo -e "───── ⋆⋅☆⋅⋆ ─────${RESET}"
	echo -e "───── ⋆⋅☆⋅⋆ ─────${RESET}"
}

# Looping Booties
booty1() {
	declare -a CMD=(

		#0 - Get Compartment List
		echo -e "Drink Her Piss"
	)

	for CMDEXEC in "${CMD[@]}"; do
		echo -e "${BBLUE}────── ꒰ঌ·✦·໒꒱ ──────${RESET}"
		echo -e "${BBLUE}────── Woman Ass Poop Eating ──────${RESET}"
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

# /// Execiton ///

panty() {
	pussy1 2>&1 | tee -a logz/ins.sh.txt
	# booty1 2>&1 | tee -a logz/ins.sh.txt

}
panty
