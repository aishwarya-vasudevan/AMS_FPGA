#!/bin/bash -
#===============================================================================
#
#          FILE: bib2html.sh
#
#         USAGE: ./bib2html.sh
#
#   DESCRIPTION: 
#
#       OPTIONS: ---
#  REQUIREMENTS: ---
#          BUGS: ---
#         NOTES: ---
#        AUTHOR: Mirco Meiners (MM), Mirco.Meiners@hs-bremen.de
#  ORGANIZATION: 
#       CREATED: 25.03.2020 15:26:22
#      REVISION:  ---
#===============================================================================

set -o nounset                                  # Treat unset variables as an error

bibtex2html -a -nobibsource \
    -header "<h2> Bibliography EEP AMS-FPGA </h2>" \
    -css "https://netdna.bootstrapcdn.com/bootswatch/3.1.1/spacelab/bootstrap.min.css" \
    ams-fpga.bib
