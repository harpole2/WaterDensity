# WaterDensity
This set of scripts reads a trajectory and calculates water density per frame and writes a DX file. The dx file is then made into a 1d profile along the z-axis and finally plotted as a tile graph in ggplot2

#pipeline write_waterdensity_perframe.py -> read_allframes.sh(calls dxfile_reader_withargs.py)->plot_water.r
