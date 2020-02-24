# Architectural Basics
Here we will be discussing the concepts used,order in which they should be placed and the thought behind it.
## Points in the order of usage
1. Kernels and how do we decide the number of kernels?

**Reason:** Based on the type of data and problem we need to decide the number of kernels and they are the feature extracter, they will identify the desired features from the dataset.

2. 3x3 Convolutions

**Reason:** After deceding the kernelas and number to be used, convolution layers are added, so as the dataset (here images) go through the kernels, convolution takes place thus this comes after kernels is decided.

3. Receptive Field,

**Reason:** Every convolution layer of a network has a receptive field, hence after every layer this has to be calucalted as it is the deciding factor when a transition block comes in as here the image size is 28x28 so after 5x5 or 7x7 there are chances that egdes and gradients are formed, thus this needs to be calculated.

4. Position of MaxPooling

**Reason:** Enough parameters has to be there for edges and graidients to be formed, if placed early will lose a lot of data.

5. MaxPooling

**Reason:** To reduce the number of parameters and layers, it is used, hence after the program has some decent amount of parameters, it can be used to pool the values and obtain the maximum value out of it.

6. Concept of Transition Layers

**Reason:** here we are using this concept to reduce the number of channels in very less parameters, therefore very useful a dn is used.

7. Position of Transition Layer

**Reason:**  There is no paper which says whether to use it before max pooling or after, here i will be placing it after max pooling and my reason is that after max pooling i.e. the maximum values are being picked this can be used to reduce channel size with very less parameters over the maximum picked values. 

8. 1x1 Convolutions 

**Reason:** When we add transition layer, 1x1 convolution will happen, thus this will come after that.

9. How many layer

**Reason:** Based on the receptive field and type of data, the layers of the network has to be decided. Here as mnist is a very simple dataset so a receptive field of 24x24 is good enough, so based on that i will be adding layers to the network.

10. When do we stop convolutions and go ahead with a larger kernel or some other alternative (which we have not yet covered)

**Reason:** When we are close to the output, we generally go with larger kernels because we done want to lose data any further, as the more we convolve the less the parameters will go, the more the data is lost and specific entries will be read many times leading to biasness in the data. So here currently we will be using a high kernel layer, later GAP will be used

11. SoftMax

**Reason:** This layer is added to exaggerate the output obtained, hence will be the last layer of the neural network.

12. The distance of MaxPooling from Prediction,

**Reason:** After the network is designed, it is amust to check that max pooling doesnt fall close to prediction layer, the reason is that we dont want to lose data when we are close to the output as it plays a major role in deciding the output.

13. Learning Rate

**Reason:** This is used inthe final iteration to checck the changes in accuarcy varing the learning rate. Initially the rate is by default fixed. Based on the problem it can be changes or kept the same.

14. Adam vs SGD

**Reason:** Decing the optimzer is important as it allows the netowrk to not stpo at local maximas or minimas. Most og the times Adam does the job, but sometimes when it fails it has to be replaced.

15. Number of Epochs and when to increase them,

**Reason:** Now it is the time to train the netowek, so we deicde the hyper parameters. Epoch is number of time the whole dataset will be read. Therefore Initially while testing the networks it has to be kep constant for all, when a decent network is created we can vary and observe changes.

16. Batch Size, and effects of batch size

**Reason:** After epochs, this is the parameter we need to fix, the batch size means how many data entries will go together for training at a time. Initially while desiging the network it is kep constant and later when a decent network is build it is varies in order to obtain the maximum output. The more the batc size the less is the time to run each epoch and less are the forward and backward propogations.

17. When to add validation checks

**Reason:** While trainging the network it is important to know how the network is performing, it is not necessary that in every epoch the network in learning at a same rate. Thus knowing the best epoch and understanding the training and validation accuracy at the same time helps in identifying the flaws in the network.

18. How do we know our network is not going well, comparatively, very early

**Reason:** When the training process is began, first three validation accuracies are recorded on the initial network. Then these accuracies are tested over the next networks, if they perform well in first three epochs, they are likely to be better network than the initial ones. Hence in this way the user doesnot have to wait for whole training to end.

19. Batch Normalization

**Reason:** The above steps will create a basic vanilla network, Now this process will normalize the batches, here the data is in black and white format, so when we look at the filters, they are of gray in color, extraction of data is difficult, hence it makes them more vivid easing the network to understand the difference.

20.Image Normalization

**Reason:** We use this to normalize the input data. Based on the accuracies of the network and the output of the filters, we may find the need to normalize the data, so at that time this is used. 

21 The distance of Batch Normalization from Prediction,

**Reason:** Batch normalization should not be used before prediction as the value of those data points is high, hence normalizaing them will result in loss of data, Thus the network may not perform as desired as a lot of data will be lost just befre predicting. Hence when the layers are added this needs to be taken care. This will complete are iteration 2 code.

22. When do we introduce DropOut, or when do we know we have some overfitting


**Reason:** When there is a difference between training and validation accuracy i.e. when the model is overfitted to the dataset. Therefore at that time there is a need to add this layer. 

23. DropOut

**Reason:** This layers are added when there is a need for them, they are added in iteration3 model as in iteration 2 the model was overfitting.


24. LR schedule and concept behind it

**Reason:** When the network is build, Learning rate can be made adaptive based on the epochs or validation accuracy, this is the final step to make the model fit over the data. This is the final change made in 4th iteration.
