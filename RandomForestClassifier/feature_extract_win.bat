set local EnableDelayedExpansion
set Compared=D:\3DGeoInfo\RandomForestClassifier\Dataset\feats
set Reference=D:\3DGeoInfo\RandomForestClassifier\Dataset
for %%f in ( "%Compared%"\* ) do ("C:\Program Files\CloudCompare\cloudcompare.exe" -SILENT -AUTO_SAVE OFF -C_EXPORT_FMT ASC -EXT TXT -LOG_FILE "%Reference%"\log.txt -O "%Compared%"\%%~nxf -FEATURE VERTICALITY 0.1 -FEATURE VERTICALITY 0.4 -FEATURE OMNIVARIANCE 0.2 -FEATURE SURFACE_VARIATION 0.2 -FEATURE PLANARITY 0.8 -SAVE_CLOUDS "%Reference%\\%%~nf+_feats.txt" -CLEAR_ALL)