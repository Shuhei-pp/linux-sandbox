#!/bin/bash
false &
wait $!
echo "Exit status of the false command: $?"