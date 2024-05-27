import random
import gym
import numpy as np
import keras
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam
import os


#Bot That Return a Random Action
class RandomBot():
    def __init__(self,iObservationSpaceSize,iActionSpaceSize):
        #Action Space Size is Required So Bot Can Randomize Action
        self.mActionSpaceSize=iActionSpaceSize
        #Random Bot Does not Require Training
        self.mDoesRequireTraining=False
    #Random Bot Does not Require Training But Train Function Need To Be Present
    def Train(self):
        pass
    #This Is Where Bot Selects Random Action
    def GetAction(self,iObservations):
        oSelectedAction=random.randint(0,self.mActionSpaceSize-1)
        return oSelectedAction

class MountainCarWrapper():
    cENVNAME="MountainCar-v0"
    def __init__(self):
        self.mProblemEnvironment=gym.make(self.cENVNAME)
        self.mObservationSpaceSize=self.mProblemEnvironment.observation_space.shape[0]
        self.mActionSpaceSize=self.mProblemEnvironment.action_space.n

    def Run(self,iIterationCount,iIsDisplayingGame,iIsDisplayingText,iBot):
        oAllActions=[]
        for vIterationIndex in range(iIterationCount):
            #Every Iteration We Start From The Beginning
            vCurrentObservation=self.mProblemEnvironment.reset()
            vIterationScore=0
            vIterationActions={"Observations":[],"Actions":[],"Score":0}
            while True:
                #This Is The display
                if(iIsDisplayingGame):
                    self.mProblemEnvironment.render()
                #Get Bots Action
                vSelectedAction=iBot.GetAction(vCurrentObservation)
                #Apply action to Get To Next State
                vNewObservation,vReward,vIsDone,_=self.mProblemEnvironment.step(vSelectedAction)
                #If Failed 
                if(vIsDone):
                    break
                vIterationScore=vIterationScore+vReward
                #Save State And Action Taken 
                vIterationActions["Observations"].append(vCurrentObservation)
                vIterationActions["Actions"].append([vSelectedAction])
                vCurrentObservation=vNewObservation
            #Save Score
            vIterationActions["Score"]=vIterationScore
            oAllActions.append(vIterationActions)
            #This Will Display Text For Each Trial
            if(iIsDisplayingText):
                print("Iteration Number: "+str(vIterationIndex)+" Achieved Score: "+str(vIterationScore))
        #Return Observation, Action and Scores for Further Processing If Required
        return oAllActions

# Create the mountain car environment
env = gym.make('MountainCar-v0')

# Define the maximum number of episodes
MAX_EPISODES = 1000

# Define the maximum number of steps per episode
MAX_STEPS = 200

# Define the main function
def main():
    for episode in range(MAX_EPISODES):
        # Reset the environment for a new episode
        observation = env.reset()

        for step in range(MAX_STEPS):
            # Render the environment
            env.render()

            # Determine the agent's action based on the observation
            action = get_action(observation)

            # Take the action and observe the new state and reward
            new_observation, reward, done, info = env.step(action)

            # Update the observation
            observation = new_observation

            # Check if the episode is over
            if done or step == MAX_STEPS - 1:
                break

# Define a function to get the agent's action based on the observation
def get_action(observation):
    position, velocity = observation

    # If the car is moving to the right and has positive velocity, accelerate to the right
    if velocity > 0:
        return 2

    # If the car is moving to the left and has negative velocity, accelerate to the left
    if velocity < 0:
        return 0

    # If the car is not moving, accelerate to the right
    return 2

# Call the main function
if __name__ == '__main__':
    main()
    def main(iBotType):
    #Set Up the Environment
            vEnv=MountainCarWrapper()
    #Set Up the Bot
    import gym

env = gym.make('MountainCar-v0')

for i_episode in range(20):
    observation = env.reset()
    for t in range(100):
        env.render()
        if observation[1] < 0:
            action = 0
        else:
            action = 2
        observation, reward, done, info = env.step(action)
        if done:
            print("Episode finished after {} timesteps".format(t+1))
            break
env.close()

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
    main(RandomBot)