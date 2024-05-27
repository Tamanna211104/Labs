import random
import gym
import numpy as np
import keras
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam
import os


#Bot That Return a Random Action For Pong Game
class PongRandomBot():
    def __init__(self,iObservationSpaceSize,iActionSpaceSize):
        #Action Space Size is Required So Bot Can Randomize Action
        self.mActionSpaceSize=iActionSpaceSize
        #Random Bot Does not Require Training
        self.mDoesRequireTraining=False
    #Random Bot Does not Require Training But Train Function Need To Be Present
    def Train(self):
        pass
    #This Is Where Bot Selects Random Action
    #There Are 2 Actions For The Pong 3 and 4
    def GetAction(self,iObservations):
        oSelectedAction=random.randint(0,self.mActionSpaceSize-1)+2
        return oSelectedAction

def main(iBotType):
    #Set Up the Environment
    vGameEnv=PongEnvWrapper()
    #Set Up the Bot
    vBot=iBotType(vGameEnv.mObservationSpaceSize,2)
    #If the Bot Requires Training Call Train Function To Train  
    if(vBot.mDoesRequireTraining):
        print("Training The Bot")
        vBot.Train()
        print("Training Complete")
    #Test The Bot
    print("Testing The Bot")
    #Run Game With Text And Image Display Using The Provided Bot
    vAllActions=vGameEnv.Run(True,True,vBot)
    print("Testing Complete")

class PongEnvWrapper():
    cENVNAME="Pong-v0"
    def __init__(self):
        self.mProblemEnvironment=gym.make(self.cENVNAME)
        self.mObservationSpaceSize=self.mProblemEnvironment.observation_space.shape[0]
        self.mActionSpaceSize=self.mProblemEnvironment.action_space.n

    def Run(self,iIsDisplayingGame,iIsDisplayingText,iBot):
        oAllActions=[]
        #We Start From The Beginning
        vCurrentObservation=self.mProblemEnvironment.reset()
        vScore=0
        vSetActions={"Observations":[],"Actions":[],"Score":0}
        while True:
            #This Is The display
            if(iIsDisplayingGame):
                self.mProblemEnvironment.render()
            #Get Bots Action
            vSelectedAction=iBot.GetAction(vCurrentObservation)
            #Apply action to Get To Next State
            vNewObservation,vReward,vIsDone,_=self.mProblemEnvironment.step(vSelectedAction)
            #Save State And Action Taken 
            vSetActions["Observations"].append(vCurrentObservation)
            vSetActions["Actions"].append([vSelectedAction])
            vCurrentObservation=vNewObservation
            #End Of Set There Are 20 Sets in The Game
            if(vReward!=0):
                vScore=vScore+vReward
                if(iIsDisplayingText):
                    if(vReward==-1):
                        print("Set Ended, Set Lost")
                    else:
                        print("Set Ended, Set Won")
                    #Save State And Action Taken 
                    vSetActions["Score"]=vReward
                    oAllActions.append(vSetActions)
            #If Game Ended
            if(vIsDone):
                break
        #This Will Display Text At The End Of Game
        if(iIsDisplayingText):
           print("Game Ended, Achieved Score: "+str(vScore))
        #Return Observation, Action and Scores for Further Processing If Required
        return oAllActions



if __name__ == "__main__":
    main(PongRandomBot)