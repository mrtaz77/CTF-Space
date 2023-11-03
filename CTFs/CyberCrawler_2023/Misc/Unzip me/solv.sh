#!/bin/bash

# Create the 'solv' folder if it doesn't exist
mkdir -p solv

# Copy the original file to the 'solv' folder
cp flag.zip solv/

# Change directory to 'solv'
cd solv

# Counter for iterations
iteration=1
while true; do
    # Check if the file exists
    if [ -f "flag.zip" ]; then
        if [ $((iteration%2)) -eq 0 ]; then
            # Even iteration: unzip the file
            unzip flag.zip > /dev/null 2>&1
        else
            # Odd iteration: extract .tar.gz file
            tar -xzf flag.tar.gz > /dev/null 2>&1
            # Remove the .tar.gz file
            rm flag.tar.gz > /dev/null 2>&1
        fi

        # Increment the iteration counter
        ((iteration++))
    else
        # No more files to unzip, break the loop
        break
    fi
done


# C3{uNzip_iS_NoT_eaSy}