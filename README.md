# Accident_Analysis_Report

From  https://data.cityofnewyork.us/Public-Safety/NYPD-Motor-Vehicle-Collisions/h9gi-nx95 we can find the raw data for our analysis.

Used Hadoop streaming API to analyze counts for each vehicle that describe the total count, per vehicle type, that the vehicle type was involved in an incident.

Mapper.py breaks the .cvs file into keys for vehicle type code
Reducer.py sums-up the value associated with the similar keys

The part-00000 file is the final output from the MapReduce

Command to run after clonning the directory: hadoop jar /usr/hdp/2.6.3.0-235/hadoop-mapreduce/hadoop-streaming-2.7.3.2.6.3.0-235.jar -file mapper.py -mapper mapper.py -file reducer.py -reducer reducer.py -input /data/nyc/nyc-traffic.csv -output output/finalOutput

the output will get generated in output/finalOutput part-00000 file
