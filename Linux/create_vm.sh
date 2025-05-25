#!/bin/bash

# Example usage with auto-start
# ./create_vm.sh -n UbuntuVM -i ~/Downloads/ubuntu.iso -m 4096 -c 4 -d 30000 -s ~/VMShare -a gui
# This creates a VM called UbuntuVM with 4 GB RAM, 4 CPUs, 30 GB disk, ISO mounted from ~/Downloads/ubuntu.iso, shared folder from ~/VMShare and launch it in GUI mode right away.

# Default values
VM_NAME=""
VM_OS_TYPE="Ubuntu_64"
VM_MEMORY=2048
VM_VRAM=16
VM_CPUS=2
VM_DISK_SIZE=20000
ISO_PATH=""
SHARED_FOLDER_PATH="$HOME/VMShared"
SHARED_FOLDER_NAME="shared"
AUTO_START="none"  # Values: none | gui | headless

# Usage function
usage() {
  echo "Usage: $0 -n VM_NAME -i ISO_PATH [options]"
  echo ""
  echo "Required:"
  echo "  -n VM_NAME              Name of the virtual machine"
  echo "  -i ISO_PATH             Path to the OS installer ISO"
  echo ""
  echo "Optional:"
  echo "  -t VM_OS_TYPE           VirtualBox OS type (default: Ubuntu_64)"
  echo "  -m VM_MEMORY            Memory in MB (default: 2048)"
  echo "  -v VM_VRAM              Video RAM in MB (default: 16)"
  echo "  -c VM_CPUS              Number of CPUs (default: 2)"
  echo "  -d VM_DISK_SIZE         Disk size in MB (default: 20000)"
  echo "  -s SHARED_FOLDER_PATH   Path to shared folder on host (default: ~/VMShared)"
  echo "  -a AUTO_START           Auto-start VM mode: 'gui' or 'headless' (default: none)"
  echo "  -h                      Show this help message"
  exit 1
}

# Parse flags
while getopts "n:i:t:m:v:c:d:s:a:h" opt; do
  case ${opt} in
    n) VM_NAME="$OPTARG" ;;
    i) ISO_PATH="$OPTARG" ;;
    t) VM_OS_TYPE="$OPTARG" ;;
    m) VM_MEMORY="$OPTARG" ;;
    v) VM_VRAM="$OPTARG" ;;
    c) VM_CPUS="$OPTARG" ;;
    d) VM_DISK_SIZE="$OPTARG" ;;
    s) SHARED_FOLDER_PATH="$OPTARG" ;;
    a) AUTO_START="$OPTARG" ;;
    h|*) usage ;;
  esac
done

# Check required fields
if [[ -z "$VM_NAME" || -z "$ISO_PATH" ]]; then
  echo "Error: -n VM_NAME and -i ISO_PATH are required."
  usage
fi

# Validate AUTO_START
if [[ "$AUTO_START" != "none" && "$AUTO_START" != "gui" && "$AUTO_START" != "headless" ]]; then
  echo "Error: Invalid value for -a AUTO_START. Use 'gui', 'headless', or omit."
  exit 1
fi

# Derived paths
VM_DIR="$HOME/VirtualBox VMs/$VM_NAME"
VMDK_FILE="$VM_DIR/$VM_NAME.vdi"

# Create VM
VBoxManage createvm --name "$VM_NAME" --ostype "$VM_OS_TYPE" --register

# Modify VM
VBoxManage modifyvm "$VM_NAME" \
  --memory "$VM_MEMORY" \
  --vram "$VM_VRAM" \
  --cpus "$VM_CPUS" \
  --audio none \
  --boot1 dvd --boot2 disk --boot3 none --boot4 none \
  --nic1 nat \
  --clipboard bidirectional \
  --draganddrop bidirectional

# Create disk
VBoxManage createmedium disk --filename "$VMDK_FILE" --size "$VM_DISK_SIZE" --format VDI

# Attach controllers and media
VBoxManage storagectl "$VM_NAME" --name "SATA Controller" --add sata --controller IntelAhci
VBoxManage storageattach "$VM_NAME" --storagectl "SATA Controller" --port 0 --device 0 \
  --type hdd --medium "$VMDK_FILE"

VBoxManage storagectl "$VM_NAME" --name "IDE Controller" --add ide
VBoxManage storageattach "$VM_NAME" --storagectl "IDE Controller" --port 0 --device 0 \
  --type dvddrive --medium "$ISO_PATH"

# Create shared folder if it doesn't exist
mkdir -p "$SHARED_FOLDER_PATH"

VBoxManage sharedfolder add "$VM_NAME" \
  --name "$SHARED_FOLDER_NAME" \
  --hostpath "$SHARED_FOLDER_PATH" \
  --automount

# Start VM if requested
if [[ "$AUTO_START" == "gui" ]]; then
  VBoxManage startvm "$VM_NAME" --type gui
elif [[ "$AUTO_START" == "headless" ]]; then
  VBoxManage startvm "$VM_NAME" --type headless
fi

# Output summary
echo ""
echo "✅ Virtual machine '$VM_NAME' created successfully!"
echo ""
echo "📋 VM Configuration Summary:"
echo "  Name:               $VM_NAME"
echo "  OS Type:            $VM_OS_TYPE"
echo "  Memory:             ${VM_MEMORY}MB"
echo "  Video Memory:       ${VM_VRAM}MB"
echo "  CPUs:               $VM_CPUS"
echo "  Disk Size:          ${VM_DISK_SIZE}MB"
echo "  Disk File:          $VMDK_FILE"
echo "  ISO Image:          $ISO_PATH"
echo "  Clipboard:          bidirectional"
echo "  Drag and Drop:      bidirectional"
echo "  Shared Folder:      $SHARED_FOLDER_PATH (mounted as '$SHARED_FOLDER_NAME')"
echo "  Auto Start Mode:    $AUTO_START"
echo ""

VBoxManage showvminfo "$VM_NAME" | grep -E "Name:|Guest OS:|Memory size:|Number of CPUs:|VRAM size:|State:|DVD|HDD|NIC|Clipboard Mode|Drag and drop Mode|Shared folders:"

