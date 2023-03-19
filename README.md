# Predicting the quality of wafer sensor for Photovoltaic applications

• Led a cross-functional team to implement a faulty wafer detection that reduced financial losses by 30% annually for a solar photovoltaic manufacturer due to inaccurate prediction.

• Developed an end-to-end pipeline that ingested and processed large volumes of IoT collected data, and used machine learning algorithms to detect faulty wafers in real-time with an accuracy of 95%.


Tech Stack: Python, Git, MongoDB, Dockers, CI/CD pipeline, Amazon S3, Elastic Container Registry, EC2, Object Oriented Programming, Machine Learning.

Success metrics: 30% annual reduction in financial losses due to incorrect prediction; model accuracy of 95%; model deployment time of 2 weeks.

More Details:
Wafer quality plays an important role in determining the effi ciency of a solar cell and the power output of a module. Therefore it is very crucial toidentify the bad quality wafer sensor. State of the art methods to identify faulty sensor is very cumbersome as it requires manual intervention in terms of measuring voltage and poweroutput across each cell which may takes months of time. Recent automation in photovoltaic industry can now generate streaming of live sensor data. The objective of this project was to use this data toreduce the faulty sensor detection time with high accuracy. 
Developed an end to end machine learning based project which involved IoT collected sensor data extraction from the database.
Data ingestion phase involved importing the data from the MongoDB, and exporting collection data as pandas dataframe.
Data validation included dropping the column which contains missing value more than specifi ed threshold and checking for data drift
The subsequent steps involved Data Transformation, Model Selection, Model Tuning, Prediction, and logging framework. Deployment phase wascompleted using AWS, and model retraining.
Such automation resulted in significant reduction of faulty sensor detection time (from months to few minutes) with 95% accurate prediction of faulty sensors.

