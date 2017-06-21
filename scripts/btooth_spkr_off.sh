#!/bin/bash
#
DONGLE="00:80:5A:20:3A:06"
SPKR="A0:E9:DB:0B:01:8C"

expect <<- DONE
  spawn bluetoothctl
  match_max 1000
  expect  "]#"
  send    "disconnect A0:E9:DB:0B:01:8C\n\n"
  expect  "Successful disconnected"
  send    "discoverable off\n\n"
  expect  "Changing discoverable off succeeded"
  send    "quit\n"
DONE

