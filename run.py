#!/usr/bin/env python3

import subprocess
import sys

# run Smooth Contours
p1 = subprocess.run(['smooth_contours','input_0.png', '-p','output.pdf','-t','output.txt'])


# convert the PDF result into a PNG image
p2 = subprocess.run(['gs', '-dNOPAUSE', '-dBATCH', '-sDEVICE=pnggray', '-dGraphicsAlphaBits=4',
                        '-r72','-dEPSCrop', '-sOutputFile=output.png', 'output.pdf'])

if p2.returncode != 0:
    with open('demo_failure.txt', 'w') as file:
        file.write("pdf->png conversion failed," + " GS may be missing on this system")
        sys.exit(0)

