hjs -D mapreduce.job.reduces=1 -files /home/wl1599/crime_analysis/column_investigation -mapper column_investigation/map_BORO_NM.py -reducer column_investigation/reduce_BORO_NM.py -input /user/wl1599/NYPD_Complaint_Data_Historic.csv -output /user/wl1599/BORO_NM.out

hjs -D mapreduce.job.reduces=1 -files /home/wl1599/crime_analysis/column_investigation -mapper column_investigation/map_CMPLNT_FR_DT.py -reducer column_investigation/reduce_CMPLNT_FR_DT.py -input /user/wl1599/NYPD_Complaint_Data_Historic.csv -output /user/wl1599/CMPLNT_FR_DT.out

hjs -D mapreduce.job.reduces=1 -files /home/wl1599/crime_analysis/column_investigation -mapper column_investigation/map_CMPLNT_FR_TM.py -reducer column_investigation/reduce_CMPLNT_FR_TM.py -input /user/wl1599/NYPD_Complaint_Data_Historic.csv -output /user/wl1599/CMPLNT_FR_TM.out

hjs -D mapreduce.job.reduces=1 -files /home/wl1599/crime_analysis/column_investigation -mapper column_investigation/map_CMPLNT_TO_DT.py -reducer column_investigation/reduce_CMPLNT_TO_DT.py -input /user/wl1599/NYPD_Complaint_Data_Historic.csv -output /user/wl1599/CMPLNT_TO_DT.out

hjs -D mapreduce.job.reduces=1 -files /home/wl1599/crime_analysis/column_investigation -mapper column_investigation/map_CMPLNT_TO_TM.py -reducer column_investigation/reduce_CMPLNT_TO_TM.py -input /user/wl1599/NYPD_Complaint_Data_Historic.csv -output /user/wl1599/CMPLNT_TO_TM.out

hjs -D mapreduce.job.reduces=1 -files /home/wl1599/crime_analysis/column_investigation -mapper column_investigation/map_RPT_DT.py -reducer column_investigation/reduce_RPT_DT.py -input /user/wl1599/NYPD_Complaint_Data_Historic.csv -output /user/wl1599/RPT_DT.out

hjs -D mapreduce.job.reduces=1 -files /home/wl1599/crime_analysis/column_investigation -mapper column_investigation/map_OFNS_DESC.py -reducer column_investigation/reduce_OFNS_DESC.py -input /user/wl1599/NYPD_Complaint_Data_Historic.csv -output /user/wl1599/OFNS_DESC.out

hjs -D mapreduce.job.reduces=1 -files /home/wl1599/crime_analysis/column_investigation -mapper column_investigation/map_KY_CD.py -reducer column_investigation/reduce_KY_CD.py -input /user/wl1599/NYPD_Complaint_Data_Historic.csv -output /user/wl1599/KY_CD.out

hjs -D mapreduce.job.reduces=1 -files /home/wl1599/crime_analysis/column_investigation -mapper column_investigation/map_PD_CD.py -reducer column_investigation/reduce_PD_CD.py -input /user/wl1599/NYPD_Complaint_Data_Historic.csv -output /user/wl1599/PD_CD.out

hjs -D mapreduce.job.reduces=1 -files /home/wl1599/crime_analysis/column_investigation -mapper column_investigation/map_PD_DESC.py -reducer column_investigation/reduce_PD_DESC.py -input /user/wl1599/NYPD_Complaint_Data_Historic.csv -output /user/wl1599/PD_DESC.out

hjs -D mapreduce.job.reduces=1 -files /home/wl1599/crime_analysis/column_investigation -mapper column_investigation/map_CRM_ATPT_CPTD_CD.py -reducer column_investigation/reduce_CRM_ATPT_CPTD_CD.py -input /user/wl1599/NYPD_Complaint_Data_Historic.csv -output /user/wl1599/CRM_ATPT_CPTD_CD.out

hjs -D mapreduce.job.reduces=1 -files /home/wl1599/crime_analysis/column_investigation -mapper column_investigation/map_LAW_CAT_CD.py -reducer column_investigation/reduce_LAW_CAT_CD.py -input /user/wl1599/NYPD_Complaint_Data_Historic.csv -output /user/wl1599/LAW_CAT_CD.out

hjs -D mapreduce.job.reduces=1 -files /home/wl1599/crime_analysis/column_investigation -mapper column_investigation/map_JURIS_DESC.py -reducer column_investigation/reduce_JURIS_DESC.py -input /user/wl1599/NYPD_Complaint_Data_Historic.csv -output /user/wl1599/JURIS_DESC.out

hjs -D mapreduce.job.reduces=1 -files /home/wl1599/crime_analysis/column_investigation -mapper column_investigation/map_ADDR_PCT_CD.py -reducer column_investigation/reduce_ADDR_PCT_CD.py -input /user/wl1599/NYPD_Complaint_Data_Historic.csv -output /user/wl1599/ADDR_PCT_CD.out

hjs -D mapreduce.job.reduces=1 -files /home/wl1599/crime_analysis/column_investigation -mapper column_investigation/map_LOC_OF_OCCUR_DESC.py -reducer column_investigation/reduce_LOC_OF_OCCUR_DESC.py -input /user/wl1599/NYPD_Complaint_Data_Historic.csv -output /user/wl1599/LOC_OF_OCCUR_DESC.out

hjs -D mapreduce.job.reduces=1 -files /home/wl1599/crime_analysis/column_investigation -mapper column_investigation/map_PREM_TYP_DESC.py -reducer column_investigation/reduce_PREM_TYP_DESC.py -input /user/wl1599/NYPD_Complaint_Data_Historic.csv -output /user/wl1599/PREM_TYP_DESC.out

hjs -D mapreduce.job.reduces=1 -files /home/wl1599/crime_analysis/column_investigation -mapper column_investigation/map_PARKS_NM.py -reducer column_investigation/reduce_PARKS_NM.py -input /user/wl1599/NYPD_Complaint_Data_Historic.csv -output /user/wl1599/PARKS_NM.out

hjs -D mapreduce.job.reduces=1 -files /home/wl1599/crime_analysis/column_investigation -mapper column_investigation/map_HADEVELOPT.py -reducer column_investigation/reduce_HADEVELOPT.py -input /user/wl1599/NYPD_Complaint_Data_Historic.csv -output /user/wl1599/HADEVELOPT.out

hjs -D mapreduce.job.reduces=1 -files /home/wl1599/crime_analysis/column_investigation -mapper column_investigation/map_X_COORD_CD.py -reducer column_investigation/reduce_X_COORD_CD.py -input /user/wl1599/NYPD_Complaint_Data_Historic.csv -output /user/wl1599/X_COORD_CD.out

hjs -D mapreduce.job.reduces=1 -files /home/wl1599/crime_analysis/column_investigation -mapper column_investigation/map_Y_COORD_CD.py -reducer column_investigation/reduce_Y_COORD_CD.py -input /user/wl1599/NYPD_Complaint_Data_Historic.csv -output /user/wl1599/Y_COORD_CD.out

hjs -D mapreduce.job.reduces=1 -files /home/wl1599/crime_analysis/column_investigation -mapper column_investigation/map_Latitude.py -reducer column_investigation/reduce_Latitude.py -input /user/wl1599/NYPD_Complaint_Data_Historic.csv -output /user/wl1599/Latitude.out

hjs -D mapreduce.job.reduces=1 -files /home/wl1599/crime_analysis/column_investigation -mapper column_investigation/map_Longitude.py -reducer column_investigation/reduce_Longitude.py -input /user/wl1599/NYPD_Complaint_Data_Historic.csv -output /user/wl1599/Longitude.out

hjs -D mapreduce.job.reduces=1 -files /home/wl1599/crime_analysis/column_investigation -mapper column_investigation/map_Lat_Lon.py -reducer column_investigation/reduce_Lat_Lon.py -input /user/wl1599/NYPD_Complaint_Data_Historic.csv -output /user/wl1599/Lat_Lon.out

