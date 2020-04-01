# -*- coding: utf-8 -*-
"""
Created on January 10, 10:57:01 2020

@author: Clare McMullen
"""

import pandas as pd
from sklearn import utils, ensemble, metrics, tree
from sklearn.model_selection import train_test_split
import numpy
import pickle

def run_model(filename1, filename2, year):
    
    rookie = pd.read_csv(filename1)
    later = pd.read_csv(filename2)
    laterid = later['playerid']
   
    
    #Drop any that do not occur in both
    for i in range(0,len(rookie.index)):
        rookie_id = rookie.loc[i,'playerid']
        if laterid.isin([rookie_id]).any() == False:
            rookie.drop(rookie.loc[rookie['playerid']==rookie_id].index, inplace=True)
            
            
        
            
            
    #Sort so that rows line up
    later = later.sort_values('playerid', ignore_index = True)
    rookie = rookie.sort_values('playerid', ignore_index = True)  
    #print(later)
    
    #Make the BB% and K% numbers, not strings
    for i in range(0,len(rookie.index)):
        string = rookie.loc[i,'BB%']
        string2 = rookie.loc[i,'K%']
        string = string[0:-1]
        string2 = string2[0:-1]
        num = float(string)
        num2 = float(string2)
        rookie.loc[i,'BB%'] = num
        rookie.loc[i,'K%'] = num2
    
        
    print(rookie)
    
    #Add _later to the variable names
    rookie = rookie.reset_index(drop = True)
    later.drop(['Name', 'Team'], axis=1, inplace = True)
    later = later.add_suffix('_later')
    
    full = pd.concat([rookie,later], axis = 1)
    full.to_csv("Main"+year+".csv", index = False)
    
    #print(full)

    return full
    
    
    
    
def main():   
         
    df2000 = run_model('Rookies2000.csv', 'Later2000.csv', "2000")
    df2001 = run_model('Rookies2001.csv', 'Later2001.csv', "2001")
    df2002 = run_model('Rookies2002.csv', 'Later2002.csv', "2002")
    df2003 = run_model('Rookies2003.csv', 'Later2003.csv', "2003")
    df2004 = run_model('Rookies2004.csv', 'Later2004.csv', "2004")
    df2005 = run_model('Rookies2005.csv', 'Later2005.csv', "2005")
    df2006 = run_model('Rookies2006.csv', 'Later2006.csv', "2006")
    df2007 = run_model('Rookies2007.csv', 'Later2007.csv', "2007")
    df2008 = run_model('Rookies2008.csv', 'Later2008.csv', "2008")
    df2009 = run_model('Rookies2009.csv', 'Later2009.csv', "2009")
    df2010 = run_model('Rookies2010.csv', 'Later2010.csv', "2010")
    df2011 = run_model('Rookies2011.csv', 'Later2011.csv', "2011")
    df2012 = run_model('Rookies2012.csv', 'Later2012.csv', "2012")
    df2013 = run_model('Rookies2013.csv', 'Later2013.csv', "2013")
    df2014 = run_model('Rookies2014.csv', 'Later2014.csv', "2014")
    
    #Put together into one master file
    master = pd.concat([df2000,df2001,df2002,df2003,df2004,df2005,df2006,df2007,df2008,df2009,df2010,df2011,df2012,df2013,df2014])
    master.to_csv("Master.csv", index=False)
    
main()



