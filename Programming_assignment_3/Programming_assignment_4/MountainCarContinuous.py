import random
import gym
import numpy as np
import keras
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam
import os

class MountainCarContinousWrapper():
    cENVNAME="MountainCarContinuous-v0"
    def __init__(self):
        self.mProblemEnvironment=gym.make(self.cENVNAME)
        self.mObservationSpaceSize=self.mProblemEnvironment.observation_space.shape[0]
        self.mActionSpaceSize=self.mProblemEnvironment.action_space.shape[0]

    def Run(self,iIterationCount,iIsDisplayingGame,iIsDisplayingText,iBot):
        oAllActions=[]
        for vIterationIndex in range(iIterationCount):
            #Every Iteration We Start From The Beginning
            vCurrentObservation=self.mProblemEnvironment.reset()
            vIterationScore=0
            vIterationActions={"Observations":[],"Values":[],"Score":0}
            while True:
                #This Is The display
                if(iIsDisplayingGame):
                    self.mProblemEnvironment.render()
                #Get Bots Action
                vSelectedValue=iBot.GetValue(vCurrentObservation)
                #Apply action to Get To Next State
                vNewObservation,vReward,vIsDone,_=self.mProblemEnvironment.step([vSelectedValue])
                #If Failed 
                if(vIsDone):
                    break
                vIterationScore=vIterationScore+vReward
                #Save State And Action Taken 
                vIterationActions["Observations"].append(vCurrentObservation)
                vIterationActions["Value"].append([vSelectedValue])
                vCurrentObservation=vNewObservation
            #Save Score
            vIterationActions["Score"]=vIterationScore
            oAllActions.append(vIterationActions)
            #This Will Display Text For Each Trial
            if(iIsDisplayingText):
                print("Iteration Number: "+str(vIterationIndex)+" Achieved Score: "+str(vIterationScore))
        #Return OBservation, Action and Scores for Further Processing If Required
        return oAllActions

def main(iBotType):
    if(iBotType==None):
        return
    #Set Up the Environment
    vEnv=MountainCarContinousWrapper()
    #Set Up the Bot
    vBot=iBotType(vEnv.mObservationSpaceSize,vEnv.mActionSpaceSize)
    #If the Bot Requires Training Call Train Function To Train  
    if(vBot.mDoesRequireTraining):
        print("Training The Bot")
        vBot.Train()
        print("Training Complete")
    #Test The Bot
    print("Testing The Bot")
    #Run Code 200 Times With Text And Image Display Using The Provided Bot
    vAllActions=vEnv.Run(200,True,True,vBot)
    print("Testing Complete")
    #Calculate Average Score
    vTotalScore=0
    for vActions in vAllActions:
        vTotalScore=vTotalScore+vActions["Score"]
    print("Average Score: "+str(vTotalScore/len(vAllActions)))

if __name__ == "__main__":
    vBotType=None
    main(vBotType)