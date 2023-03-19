# Machine Learning based Air-pressure sensor fault prediction

• Conducted an analysis of Air-Pressure system fault detection in automobile that resulted in a 10% increase in revenue for the manufacturer.

• Built a production grade XGBoost based model to reduce false negatives, since cost incurred due to false negative was observed as 50 times higher than the false positives, and identified opportunities to increase revenue by reducing the cost due to unnecessary repairs.


Tech Stack: Python, Git, Cassandra, MLOps, Dockers, Amazon S3, Elastic Container Registry, EC2, Object Oriented Programming, XGBoost

Success metrics: 10% increase in revenue; model accuracy of 96%; reduction of false negative cases by 25%.

More Details:
The system in focus is the Air Pressure system (APS) which generates pressurized air that are utilized in various functions in a truck, such as brakingand gear changes. The datasets positive class corresponds to component failures for a specifi c component of the APS system. The negative classcorresponds to trucks with failures for components not related to the APS system.

The objective was to reduce the cost due to unnecessary repairs. Therefore, it was required to minimize the false predictions.

Data validation phase involved dropping columns with more than 70% of missing values.

Data visualization revealed that the target classes was highly imbalanced.

Synthetic Minority Oversampling Technique (SMOTE) method was used to deal with the imbalanced dataset.

Data transformation step involved used of Robust Scaler method.

Used various imputation of null values such as: KNN, simple (mean and median), MICE, and PCA.

Evaluated Machine Learning model on diff erent imputation techniques using parameters such as: Accuracy, F1 score, Precision, Recall, ROC-AUCScore, and Cost.
The best Model was identifi ed as XGBoost Classifi er with 99.6% accuracy and cost of 2950.

Used MLOps, CI/CD pipeline, Dockers, Containers during production and implementation, and AWS for deployment.

