library(ggplot2)
library(tools)
library(plyr)
library(reshape2)


setwd("WHATEVER_DIRECTORY")
filelist = list.files(pattern = ".*.txt") #assumes folder is clean ouside of the txt created from dx files
all_data<-data.frame(frame=integer(),z_axis=integer(), variable=factor(),value=numeric())
for (i in 0:(length(filelist)-1)){
  tmp_name<-paste("water_density_convert_alongz_",i,".txt",sep="")
  tmp_z<-read.table(tmp_name)
  z_axis<-1:nrow(tmp_z)
  frame <-rep(i,times=nrow(tmp_z))
  water_den_data<-data.frame(frame,z_axis,tmp_z)
  colnames(water_den_data)[3]<-"density"
  water_den_data<-melt(water_den_data,id=c("frame","z_axis"))
  all_data<-rbind(all_data,water_den_data)
  assign(file_path_sans_ext(tmp_name),water_den_data)
}

#all_data$density<-cut(all_data$value,
#                  breaks=c(0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0,1.1),
#                  labels=as.character(c(0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9,1.0)),
#                  include.lowest=TRUE)

#water_plot<- ggplot(data=all_data,aes(x=frame,y=z_axis)) +
#  theme_bw() +
#  scale_x_continuous(expand = c(0, 0)) + 
#  scale_y_continuous(expand = c(0, 0)) +
#  theme(panel.grid.major = element_blank(), panel.grid.minor = element_blank()) +
#  geom_tile(aes(fill=density)) +
#  scale_fill_manual(values=(colorRampPalette(c("red","white", "blue"))( 12 )))

all_data$density<-cut(all_data$value,
                      breaks=c(0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1.0,1.05, 1.1),
                      labels=as.character(c(0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1.0,1.05)),
                      include.lowest=TRUE)
water_plot<- ggplot(data=all_data,aes(x=frame,y=z_axis)) +
  theme_bw() +
  scale_x_continuous(expand = c(0, 0)) + 
  scale_y_continuous(expand = c(0, 0)) +
  theme(panel.grid.major = element_blank(), panel.grid.minor = element_blank()) +
  geom_tile(aes(fill=density)) +
  scale_fill_manual(values=(colorRampPalette(c("red","white", "blue"))( 22 )))


