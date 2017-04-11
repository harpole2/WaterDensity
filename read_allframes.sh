#!/bin/bash
source activate py27


#prints things
set -x
for ((ii = 0; ii <= 1877; ii++)); do
	python dxfile_reader_withargs.py -i water_density_convert_${ii}.dx -o water_density_convert_alongz_${ii}

   
done
