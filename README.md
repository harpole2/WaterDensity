# WaterDensity
This set of scripts reads a trajectory and calculates water density per frame and writes a DX file. The dx file is then made into a 1d profile along the z-axis and finally plotted as a tile graph in ggplot2

# pipeline
 write_waterdensity_perframe.py -> read_allframes.sh(calls dxfile_reader_withargs.py)->plot_water.r

# WaterDensity removing voxels with protein and lipid
This set of scripts reads a trajectory and calculates water density per frame and writes a DX file. It also calculates the same for lipid and protein in order to remove those from calculation. The dx file is then made into a 1d profile along the z-axis and finally plotted as a tile graph in ggplot2

# pipeline
 write_waterdensity_withPROLIP_perframe.py -> read_allframes_withProLip.sh(calls dxfile_reader_withargs_multiplefiles.py)->plot_water.r
