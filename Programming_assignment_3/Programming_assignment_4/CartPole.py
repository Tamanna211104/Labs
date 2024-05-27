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
    env = gym.make('CartPole-v0')

for i_episode in range(20):
    observation = env.reset()
    for t in range(100):
        env.render()
        if observation[2] < 0:
            action = 0
        else:
            action = 1
        observation, reward, done, info = env.step(action)
        if done:
            print("Episode finished after {} timesteps".format(t+1))
            break

env.close()



#Bot That Uses A Simple Network
class BasicNNBotCartPole():
    #Parameter Used In eleminating bad games
    cGOODGAMESCORETHRESHOLD=60
    #File Path for Saving the Trained Model For Avoiding Retraining It
    cLOADBOTPATH="BasicNNBotCartPoleModel.h5"
    def __init__(self,iObservationSpaceSize,iActionSpaceSize):
        #Observations are The Input For Our Network So Their Size Is Improtant 
        self.mObservationSpaceSize=iObservationSpaceSize
        self.mActionSpaceSize=iActionSpaceSize
        #Checks if we already have a Pre-Trained Modal Present
        if(os.path.isfile(self.cLOADBOTPATH)):
            #IF There is Use that Modal
            self.mModel = keras.models.load_model(self.cLOADBOTPATH)
            self.mDoesRequireTraining=False
        else:
            #If Not Generate Model And Set The Training Flag
            #Simple Model With Fully Connected Layers: Input Is The Observations Output is a Value between 0 To 1
            self.mModel = Sequential()
            self.mModel.add(Dense(8, activation='relu', input_dim=self.mObservationSpaceSize))
            self.mModel.add(Dense(4, activation='relu'))
            self.mModel.add(Dense(1, activation='linear')) 
            self.mModel.compile(loss='mse', optimizer=Adam())
            self.mDoesRequireTraining=True
            
import gym
import numpy as np

env = gym.make('CartPole-v0')

# Define the neural network
n_inputs = env.observation_space.shape[0]
n_hidden = 4
n_outputs = env.action_space.n
model = keras.Sequential([
    keras.layers.Dense(n_hidden, activation='relu', input_shape=(n_inputs,)),
    keras.layers.Dense(n_outputs, activation='softmax')
])

# Define the Q-learning algorithm
alpha = 0.1
gamma = 0.99
epsilon = 1.0
epsilon_min = 0.01
epsilon_decay = 0.995

for i_episode in range(500):
    state = env.reset()
    state = np.reshape(state, [1, n_inputs])
    for t in range(500):
        env.render()
        if np.random.rand() <= epsilon:
            action = env.action_space.sample()
        else:
            action = np.argmax(model.predict(state)[0])
        next_state, reward, done, _ = env.step(action)
        next_state = np.reshape(next_state, [1, n_inputs])
        target = reward + gamma * np.amax(model.predict(next_state)[0])
        target_f = model.predict(state)
        target_f[0][action] = alpha * target + (1 - alpha) * target_f[0][action]
        model.fit(state, target_f, epochs=1, verbose=0)
        state = next_state
        if done:
            print("Episode finished after {} timesteps".format(t+1))
            break
    if epsilon > epsilon_min:
        epsilon *= epsilon_decay

env.close()

def Train(self):
        #Run The Game 5000 Times With RandomBot
        vCaprtPoleEnv=CartPoleEnvWrapper()
        vRandomBot=RandomBot(self.mObservationSpaceSize,self.mActionSpaceSize)
        vAllActions=vCaprtPoleEnv.Run(5000,False,False,vRandomBot)
        #Get The Data From The Good Games
        vTrainingDataFeatures=[]
        vTrainingDataResults=[]
        for vActions in vAllActions:
            if(vActions["Score"]>self.cGOODGAMESCORETHRESHOLD):
                vTrainingDataFeatures=vTrainingDataFeatures+vActions["Observations"]
                vTrainingDataResults=vTrainingDataResults+vActions["Actions"]
        #Input Had To Be A NumPy Array
        vTrainingData=np.array(vTrainingDataFeatures)
        vTrainingLabels=np.array(vTrainingDataResults)
        #This Is Where Model IS Trained
        self.mModel.fit(vTrainingData,vTrainingLabels,epochs=10)
        #Saving The Trained Model
        self.mModel.save(self.cLOADBOTPATH)
        self.mDoesRequireTraining=False
def GetAction(self,iObservations):
        #Ask Network For An Output
        vPredictionResult=self.mModel.predict(np.array([iObservations]))[0][0]
        #If The Output is Closer to the 0 then Cart Moves Left Else Cart Moves Right
        if(vPredictionResult>=0.5):
            oSelectedAction=1
        else:
            oSelectedAction=0
        return oSelectedAction

class CartPoleEnvWrapper():
    cENVNAME="CartPole-v1"
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
        #Return OBservation, Action and Scores for Further Processing If Required
        return oAllActions

env = gym.make('CartPole-v1')

for i_episode in range(20):
    observation = env.reset()
    for t in range(100):
        env.render()
        if observation[2] > 0:
            action = 1
        else:
            action = 0
        observation, reward, done, info = env.step(action)
        if done:
            print("Episode finished after {} timesteps".format(t+1))
            break
env.close()


env = gym.make('CartPole-v1')

# Define the neural network
model = Sequential()
model.add(Dense(24, input_dim=4, activation='relu'))
model.add(Dense(24, activation='relu'))
model.add(Dense(2, activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer=Adam(lr=0.001))

# Train the neural network using Q-learning
for i_episode in range(20):
    state = env.reset()
    state = np.reshape(state, [1, 4])
    for t in range(100):
        env.render()
        action = np.argmax(model.predict(state)[0])
        next_state, reward, done, info = env.step(action)
        next_state = np.reshape(next_state, [1, 4])
        target = reward + 0.99 * np.amax(model.predict(next_state)[0])
        target_f = model.predict(state)
        target_f[0][action] = target
        model.fit(state, target_f, epochs=1, verbose=0)
        state = next_state
        if done:
            print("Episode finished after {} timesteps".format(t+1))
            break
env.close()

def main(iBotType):
    #Set Up the Environment
    vCaprtPoleEnv=CartPoleEnvWrapper()
    #Set Up the Bot
    vBot=iBotType(vCaprtPoleEnv.mObservationSpaceSize,vCaprtPoleEnv.mActionSpaceSize)
    #If the Bot Requires Training Call Train Function To Train  
    if(vBot.mDoesRequireTraining):
        print("Training The Bot")
        vBot.Train()
        print("Training Complete")
    #Test The Bot
    print("Testing The Bot")
    #Run Code 200 Times With Text And Image Display Using The Provided Bot
    vAllActions=vCaprtPoleEnv.Run(200,True,True,vBot)
    print("Testing Complete")
    #Calculate Average Score
    vTotalScore=0
    for vActions in vAllActions:
        vTotalScore=vTotalScore+vActions["Score"]
    print("Average Score: "+str(vTotalScore/len(vAllActions)))

if __name__ == "__main__":
    #main(RandomBot)
    main(BasicNNBotCartPole)