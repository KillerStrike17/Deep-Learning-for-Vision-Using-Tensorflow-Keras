# Coding Drill - 99.4%-Accuracy-under-15k-Parameters
This repository consists of 4 codes,each has 3 changes in it from the previous one resulting in better accuracy, hence we are drilling down the program to achieve better accuracy over better networks.
## First Iteration
It is a basic Neural Network with 32 btach size and 10 epochs
### Result
Parameters:- 12458

Accuracy:- 98.99

Epochs:- 8
## Second Iteration
### Change
3 Batch Normaliation Layer added
### Result
Parameters:- 12618 

Accuracy:- 99.04%

Epochs:- 6
## Third Iteration
### Change
3 Dropout Layer added
### Result
Parameters:- 12618

Accuracy:- 99.18%

Epochs:- 8
## Fourth Iteration
### Change
Epoch = 40

Batch Size = 64

Learning rate = 0.03
### Result
Parameters:- 12618

Accuracy:- 99.40%

Epochs:- 20

### Note:- Architectural Basics file contains the concept used and the reason behind it.
