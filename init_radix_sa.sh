#!/bin/bash
curl -O http://www.engr.uconn.edu/~man09004/radixSA.zip		# -O for output to file
unzip -o radixSA.zip						# -o for overwrite automatically
cd radixSA && make clean && make 				# Enter subdirectory and make
cp radixSA ../radixSAbin					# Copy the compiled binary into the main directory
cd ..								# Return to main directory
rm -r -f radixSA						# Remove the subdirectory
rm radixSA.zip							# Remove the zip file
mv radixSAbin radixSA						# Rename the compiled binary
