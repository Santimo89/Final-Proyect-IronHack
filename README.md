![Ironhack logo](https://i.imgur.com/1QgrNNw.png)

# Final-Proyect-IronHack

## Overview

The goal of this proyect is to give to the surfer the best conditions for him to decide where to go in the north of Spain and dont miss the spot.

I followed the following steps to achieve the goal:

1.Extract information:
    
    - Extract waves info and create dataset fom Puertos del Estado web
    - Extract weather info trough api from AEMET web
    - Web scrapping and api info from other webs(windguru, meteomatics, meteogalicia), wich at the end result to be not accurate and had to be dismissed

2. Clean the dataset:
    - Label encode some features
    - Drop highly correlated features
    - Standardize values

3. Train test split to divide my data in X_ train, X_test, y_train, y_test

4. Grid search for Random Forest hyperparameters

5. Train model 

