#!/bin/bash
#
DONGLE="00:80:5A:20:3A:06"
SPKR="A0:E9:DB:0B:01:8C"

# Check that the dongle is ON
declare -a devicelist
declare -a addrlist

readarray -n 10 -O 0 -t devicelist < <(hcitool dev|grep -v "^Devices:" | awk '{print $2}') 2>/dev/null


if [[ "${devicelist[@]}" =~ "${DONGLE}" ]]; then
  # Check that the speaker is Available
  readarray -n 10 -O 0 -t addrlist < <(hcitool scan|grep -v "^Scanning"|sed -e "s/^[ \t]//g" -e "s/\t/ /g" | head -n 9) 2>/dev/null

  if [[ "${addrlist[@]}" =~ "${SPKR}" ]]; then
    echo "FOUND"
  #set timeout 5
expect <<- DONE
  spawn bluetoothctl
  match_max 1000
  expect  "]#"
  send    "disconnect A0:E9:DB:0B:01:8C\n\n"
  expect  "Successful disconnected"
  send    "power on\n\n"
  expect  "Changing power on succeeded"
  send    "discoverable on\n\n"
  expect  "Changing discoverable on succeeded"
  send    "pairable on\n\n"
  expect  "Changing pairable on succeeded"
  send    "agent NoInputNoOutput\n"
  expect  "Agent registered"
  send    "default-agent\n\n"
  expect  "Default agent request successful"
  send    "scan on\n"
  expect  "Device A0:E9:DB:0B:01:8C"
  send    "trust A0:E9:DB:0B:01:8C\n"
  expect  "Changing A0:E9:DB:0B:01:8C trust succeeded"
  send    "connect A0:E9:DB:0B:01:8C\n"
  expect  "Connected: yes"
  send    "quit\n"
DONE

  else
    echo "SPEAKER NOT FOUND"
    exit 2
  fi
else
  echo "DONGLE NOT FOUND"
  exit 2
fi

