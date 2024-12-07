#!/bin/bash

if [ -e lock ]; then
    echo "lock file exists."
else
    touch lock
    echo "lock file created."
fi