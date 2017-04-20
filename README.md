To generate the first table regarding details of each column. You need to run the script in ./code/column_investigation/

For example, in order to get BORO_NM.out, on dumbo you run
hjs -D mapreduce.job.reduces=1 -files <dumbo_directory> -mapper <dumbo_directory>/map_BORO_NM.py -reducer <dumbo_directory>/reduce_BORO_NM.py -input <hdfs_directory>/NYPD_Complaint_Data_Historic.csv -output <hdfs_directory>/BORO_NM.out
Then you use getmerge  and scp command to transfer output file from hdfs and dumbo to your local directory.

To generate most of graphs in the summary, you run weitao.ipynb which takes the output files from previous steps to generate graphs.

There are also some graphs generated from different sources:

In folder named 'boros', you can find MapReduce scripts that generate total number of offenses in 5 boroughs from 2006 to 2015. You should find 5 mappers for 5 boroughs and one reducer that is compatible with these five mappers. You should also find all 5 outputs inside the folder as well as related graphs

In forlder named 'offense_lv', you can find MapReduce scripts that generate total number of 3 types of offense(violation, misdemeanor and felony) for each month from 2006 to 2015. You should find 12 mappers for 12 months and one reducer that is compatible with these 12 mappers. You should also find all 12 outputs inside the folder as well as related graphs.

In folder named 'top20', you can find a spark program, top20spark.py, that generates total number of top 20 offenses from 2006 to 2015. You should also a output file inside the folder.

In folder named 'wordcloud', you can find a MapReduce program that generate a .out file that contains the first word of PD_DESC for each offense from 2006 to 2015. You should find the output as well as a wordcloud graph inside the folder.

In folder 'year', you can find MapReduce scripts that generate total number of offenses every year from 2006 to 2015. You should find 10 mappers for 10 years and one reducer that is compatible with these 10 mappers. You shold also find 10 outputs inside the folder as well as related graphs.

For MapReduce tasks in these folders, you need to run:
hjs \
       -files <dumbo_directory>/<mapper>.py,<dumbo_directory>/<reducer>.py \
       -input <hdfs_directory>/NYPD_Complaint_Data_Historic.csv \
       -output <hdfs_directory>/<task_name>.out \
       -mapper <mapper>.py \
       -reducer <reducer>.py

To get MapReduce output files from HDFS, you need to run:
hfs -getmerge <hdfs_directory>/<task_name>.out <task_name>.out

For spark task in folder 'top20', you need to run:
spark-submit top20spark.py <hdfs_directory>/NYPD_Complaint_Data_Historic.csv
To get spark output file, you need to run:
hfs -getmerge top20.out top20.out


At last, you need to pscp or scp command to ransfer output file from dumbo to your local directory.

All the graphs in 5 folders above are can be generated using shangying.ipynb and output files in these folders.
To generate wordcloud, you need to first

pip install wordcloud

Then you can find the mask graph inside 'wordcloud' folder, named 'nyc_capture.PNG'.


