#!/bin/bash
@set inputFolder = "./Dataset/feature_extraction"
for /r %inputFolder% %F in (*.txt) do ("C:\Program Files\CloudCompare\CloudCompare.exe" -C_EXPORT_FMT txt -LOG_FILE log.txt -O %F -FEATURE VERTICALITY 0.1 Verticality 0.4 Omnivariance 0.2 Surface_variation 0.2 Planarity 0.8)
