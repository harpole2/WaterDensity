#!/bin/bash
source activate py27


#prints things
set -x
for ((ii = 0; ii <= 3475; ii++)); do
	python dxfile_reader_withargs_multiplefiles.py -il lipid_density_notconvert_${ii}.dx -ip protein_density_notconvert_${ii}.dx -iw water_density_convert_${ii}.dx -o water_density_convert_alongz_factLipPro_${ii}  
done
