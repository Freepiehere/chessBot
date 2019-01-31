import numpy as np 
import keras

#import processed .npz dataset file
class Dataset():
    def __init__(self,filename):
        print('Loading Data...')
        npy_dataset = self.loadData(filename)
        args = npy_dataset.files
        self.X = npy_dataset[args[0]]
        self.Y = npy_dataset[args[1]]

    def loadData(self,filename):
        return np.load(filename)


# keras-implemented convolutional neural networks
class Net():
    def  __init__(self,ds=None,learning_rate=0.01,model=None):
            
        if not ds:
            self.X,self.Y=None,None
            self.num_input = None
            self.num_output = None
        else:
            print('Initiatlizing Network...')
            self.X,self.Y = ds.X,ds.Y
            self.num_input = self.X.shape[-1]
            self.num_output = self.Y.shape[-1]

        # optimizer trining parameters
        self.learning_rate = learning_rate
        self.num_epochs = 20
        if not model:
            self.model = self.architecture()
        else:
            self.model = model

#1 1024 layer: 47.45% accuracy
#2 1024 layer: % accuracy
    def architecture(self):
        print('Building AI...')

        model = keras.models.Sequential()
        model.add(keras.layers.Dense(1024,activation='relu'))
        model.add(keras.layers.Dense(1024,activation=None))
        model.add(keras.layers.Dropout(0.2))
        model.add(keras.layers.Dense(self.num_output,activation='softmax'))
        return model
        
    def train(self):
        print('Training AI...')
        training_samples = self.X
        training_labels = self.Y
        
        #optimizer = keras.optimizers.RMSprop(lr=self.learning_rate,decay=1/self.num_epochs)
        optimizer = keras.optimizers.SGD()
        loss = keras.losses.mean_squared_error

        self.model.compile(optimizer=optimizer,loss=loss,metrics=['accuracy'])
        self.model.fit(training_samples,training_labels,epochs=self.num_epochs)
        
        scores = self.model.evaluate(training_samples,training_labels,verbose=0)
        print("%s: %.2f%%" % (self.model.metrics_names[1], scores[1]*100))

    def evaluateSample(self,sample):
        prediction = self.model.predict(np.expand_dims(sample,axis=0))
        return prediction[0] 

    def saveModel(self):
        #keras.utils.plot_model(self.model,to_file='model.png')
        model_JSON = self.model.to_json()
        with open("model.json","w") as json_file:
            json_file.write(model_JSON)
        self.model.save_weights("model.h5")



if __name__ == "__main__":
    ds = Dataset("dataset.npz")
    net = Net(ds)
    net.train()
    net.saveModel()
    num_epoch = 1000
