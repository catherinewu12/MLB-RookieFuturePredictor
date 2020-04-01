#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 16:26:00 2020

@author: claremcmullen
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import utils, ensemble, metrics, tree, linear_model
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.multioutput import MultiOutputRegressor
import numpy
import pickle
from sklearn.utils import shuffle

def run_model(filename):
    file_path = filename + ".csv"
    
    contents = pd.read_csv(file_path)
    #contents = contents.drop([['random']])
    
    target = contents['WAR_later']
    
    #Original Features, not currently used for model
    #features = contents.drop(['Name','Team','playerid', 'playerid_later', 'G_later','PlayerId_minors',	'PA_later',	'HR_later',	'R_later',	'RBI_later',	'SB_later',	'BB%_later',	'K%_later',	'ISO_later',	'BABIP_later',	'AVG_later',	'OBP_later',	'SLG_later',	'wOBA_later',	'wRC+_later',	'BsR_later',	'Off_later',	'Def_later','WAR_later', 'playerid_later'], axis = 1)
    
    #Most Important Features (used for this version of model)
    features = contents[['WAR', 'wRC+_minors', 'Def', 'wSB_minors','BABIP_minors', 'wOBA_minors', 'Spd_minors']]
    
    #Another set of test features
    #features = contents.drop(['Name','Team','WAR' ,'playerid', 'playerid_later', 'G_later','PlayerId_minors',	'PA_later',	'HR_later',	'R_later',	'RBI_later',	'SB_later',	'BB%_later',	'K%_later',	'ISO_later',	'BABIP_later',	'AVG_later',	'OBP_later',	'SLG_later',	'wOBA_later',	'wRC+_later',	'BsR_later',	'Off_later',	'Def_later','WAR_later', 'playerid_later', 'R', 'SB', 'K%', 'ISO', 'wOBA', 'wRC+', 'E', 'FP', 'Def', 'wOBA_minors'], axis = 1)
    
    print(features)
    print(target)
    
    training_data, testing_data, training_target, testing_target = train_test_split(features, target, test_size=0.20, random_state=34)
    
    
    #Regression 
    ########################################################
    model = ensemble.RandomForestRegressor()
    model.fit(training_data, training_target)
    
    
    
    #Scores##################################################
    print("Accuracy score (training): {0:.3f}".format(model.score(training_data, training_target)))
    print("Accuracy score (validation): {0:.3f}".format(model.score(testing_data, testing_target)))
    
    
    importance = list (model.feature_importances_)
    
    columns = list(features.columns.values)
    for i in range(0,len(importance)):
        print(columns[i]," ",importance[i] * 100)
    
    
    

    # Plot feature importance
    feature_importance = model.feature_importances_
    # make importances relative to max importance
    feature_importance = 100.0 * (feature_importance / feature_importance.max())
    sorted_idx = np.argsort(feature_importance)
    pos = np.arange(sorted_idx.shape[0]) + .5
    plt.subplot(1, 2, 2)
    plt.barh(pos, feature_importance[sorted_idx], align='center')
    plt.yticks(pos, np.array(list(features))[sorted_idx])
    plt.xlabel('Relative Importance')
    plt.title('Variable Importance')
    plt.show()
    
    #Predictions#####################
    info = pd.read_csv("Pre_master.csv")
    #info = info.drop(['Name','Team' ,'playerid', 'PlayerId_minors'], axis = 1)
    info = info[['WAR', 'wRC+_minors', 'Def', 'wSB_minors','BABIP_minors','wOBA_minors', 'Spd_minors']]
    
    pre = model.predict(info);
    print("Bo:",pre[0])
    print("Biggio" , pre[1])
    print("Juan", pre[2])
    print("Alonso" , pre[3])
    print("Reese", pre[4])
    print("Rowdy", pre[5])
    print("Vlad" , pre[6])
    print("Alvarez is", pre[9])
    print("Tatis is", pre[10])
    print("Robles is", pre[11])
    
    

    
    

run_model('NewMasterMinors')
