#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 16:04:51 2020

@author: claremcmullen
"""

import pandas as pd
from sklearn import utils, ensemble, metrics, tree
from sklearn.model_selection import train_test_split
import numpy
import pickle

def run_model(filename1, filename2):
    
    #MasterCopy
    rookie = pd.read_csv(filename1)
    
    #Minors
    later = pd.read_csv(filename2)
    laterid = later['PlayerId']
   
    
    #Delete any players who do not have minor league stats
    for i in range(0,len(rookie.index)):
        rookie_id = rookie.loc[i,'playerid']
        
        if laterid.isin([rookie_id]).any() == False:
            rookie.drop(rookie.loc[rookie['playerid']==rookie_id].index, inplace=True)
            
            
        
            
            
    #Sort so rows line up
    later = later.sort_values('PlayerId', ignore_index = True)
    rookie = rookie.sort_values('playerid', ignore_index = True)  
    print(rookie)
    print(later)
   
    
    #Remove already known stats
    rookie = rookie.reset_index(drop = True)
    later.drop(['Name', 'Team', 'Age'], axis=1, inplace = True)
    later = later.add_suffix('_minors')
    
    full = pd.concat([rookie,later], axis = 1)
    #full.to_csv("NewMasterMinors.csv", index = False)
    #full.to_csv("Bo_master.csv", index = False)
    full.to_csv("Pre_master.csv", index = False)
    
    print(full)

    
    
    
    
    
def main():   
         
    run_model('MasterCopy.csv', 'Minors.csv')
    #run_model('Prefile.csv', 'Prefile_minors.csv')
    
    
main()



