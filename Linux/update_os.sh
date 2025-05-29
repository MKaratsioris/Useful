#!/bin/bash

# Color codes
GREEN='\033[0;32m'    # Success
RED='\033[0;31m'      # Error
YELLOW='\033[1;33m'   # Step/Info
NC='\033[0m'          # No Color

# Functions
step() {
    echo -e "${GREEN}  $1${NC}"
}

success() {
    echo -e "${GREEN}  $1${NC}"
}

error() {
    echo -e "${RED}  $1${NC}"
}

# Begin
step "[1/5] sudo apt update -y"
if sudo apt update -y 2>&1 | sed 's/^/          /'; then
    success "      apt update completed successfully"
else
    error "    apt update failed"
fi

step "[2/5] sudo apt upgrade -y"
if sudo apt upgrade -y 2>&1 | sed 's/^/          /'; then
    success "      apt upgrade completed successfully."
else
    error "    apt upgrade failed"
fi

step "[3/5] sudo apt-get update -y"
if sudo apt-get update -y 2>&1 | sed 's/^/          /'; then
    success "      apt-get update completed successfully"
else
    error "    apt-get update failed"
fi

step "[4/5] sudo apt-get upgrade -y"
if sudo apt-get upgrade -y 2>&1 | sed 's/^/          /'; then
    success "      apt-get upgrade completed successfully"
else
    error "    apt-get upgrade failed"
fi

# ESET Antivirus check
step "[5/5] mokutil --sb-state"

SB_STATE=$(mokutil --sb-state 2>/dev/null)
if echo "$SB_STATE" | grep -qi "SecureBoot enabled"; then
    success "      $SB_STATE"
elif echo "$SB_STATE" | grep -qi "SecureBoot disabled"; then
    error "      $SB_STATE"
else
    error "Failed to determine Secure Boot status."
    echo -e "${RED}$SB_STATE${NC}"
fi
