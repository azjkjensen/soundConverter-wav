# soundConverter.py

'''
Sound converter for changing .wav files to C-readable data.
This file will take the given wav files
in the SampleSounds/ directory next to
it and converts them into a C-readable
format as data arrays and sample rate
variables.
'''

import scipy.io.wavfile
import sys

# Get the file name (fn) to read from
fn = sys.argv[1]

# Grab the wav file sample rate and data array
fs1,y1 = scipy.io.wavfile.read(fn, 'r')

# Open the new file to save to.
outFile = open(sys.argv[2], 'w')

# Put the #include in for primitive fixed-width types 
outFile.write('#include "stdint.h"\n')

# Strip off the .wav from the filename
fn_stripped = fn.split('.')[0]

# Write all information as a C file.
outFile.write('\n\nuint32_t ' + fn_stripped + '_rate = ' + str(fs1) +\
';\nuint32_t ' + fn_stripped + '_frames = ' + str(len(y1)) +\
';\nuint32_t ' + fn_stripped + '_data[] = {')

# Add all items in the array, comma separated
outFile.write(','.join(str(y) for y in y1))	

# End the array
outFile.write('};\n')

# Print out the information being saved as user feedback.
print 'reading from: ', fn
print 'saving to: ', sys.argv[2]
print 'Sample rate: ',
print fs1
print 'Data: '
print y1
print
