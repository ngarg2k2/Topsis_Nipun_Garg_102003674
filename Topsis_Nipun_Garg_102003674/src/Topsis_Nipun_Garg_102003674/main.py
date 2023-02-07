import pandas as pd
import numpy as np
import sys

def get_score(dataframe,weights,impacts,output):

    weights = [float(x) for x in weights.split(',')]
    impacts = impacts.split(',')

    ## check for column count>3
    if dataframe.shape[1]<3:
        print("Dataset must have atleast 3 columns(first column being name)!")
        quit()
    ## check for non numeric columns
    for i in range(1,dataframe.shape[1]):
        if (dataframe.dtypes[i]=='object'):
            print("Dataset has non numeric columns. Please make them numeric and enter the weights and impacts accordingly!")
            quit()

    df = dataframe.iloc[:,1:].values
    df = df.astype('float64')

    ## check for correct weights and impacts entered
    if df.shape[1]!=len(weights):
        print("Enter the correct number of weights!")
        quit()
    if df.shape[1]!=len(impacts):
        print("Enter the correct number of impacts!")
        quit()



    # calculating the root of sum of squares for each column
    sum_sq = []
    for i in range(df.shape[1]):
        sum_sq.append(np.sqrt(np.sum(df[:,i]**2)))



    # normalisation and weight multiplication
    for i in range(df.shape[0]):
        for j in range(df.shape[1]):
            df[i,j]=df[i,j]/sum_sq[j] * weights[j]



    # calculating the ideal best and ideal worst lists
    ideal_best = []
    ideal_worst = []

    for i in range(df.shape[1]):
        if impacts[i]=='+':
            ideal_best.append(np.max(df[:,i]))
            ideal_worst.append(np.min(df[:,i]))
        elif impacts[i]=='-':
            ideal_best.append(np.min(df[:,i]))
            ideal_worst.append(np.max(df[:,i]))
        else: # error handling
            print("Impacts must be either + or -!")
            quit()





    # calculating the distance from best and worst
    dist_from_best = []
    dist_from_worst = []

    for i in range(df.shape[0]):
        d_b = np.sqrt(np.sum((ideal_best-df[i,:])**2))
        dist_from_best.append(d_b)
        d_w = np.sqrt(np.sum((ideal_worst-df[i,:])**2))
        dist_from_worst.append(d_w)




    # calculating the score values
    score = [dist_from_worst[i]/(dist_from_worst[i]+dist_from_best[i]) for i in range(len(dist_from_best))]




    # calculating the ranks
    sorted_score = sorted(score,reverse=True)
    rank = [sorted_score.index(x)+1 for x in score]

    dataframe['Topsis Score']=score
    dataframe['Rank'] = rank
    # return dataframe
    print(dataframe)
    dataframe.to_csv(output)

    

# get_score(pd.read_csv(sys.argv[1]),sys.argv[2],sys.argv[3],sys.argv[4])
# print(data)
# data.to_csv(sys.argv[4])