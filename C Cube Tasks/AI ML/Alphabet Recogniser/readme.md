Alphabet Recogniser

* I applied two under sampling techniques to prepare the data and have presented the results
* The first model uses Near Miss 1 algorithm where majority class examples that have the smallest average distance to the three closest minority class examples
* With this under-sampling we balanced the samples for all the classes
* In the second model, I used neighbourhood cleaning rule which removes redundant and ambiguous noisy examples
* Here there is less focus on improving the balance of class distribution and this model focuses more on the quality of examples retained in the majority class
* Finally the output predictions of both the models have been presented
* While using the near miss algorithm there was a variation of about 14% between consecutive runs
* The NCR model has marginally less variation ~ (2-3%)

Details for first model
* After under-sampling, dataset shape 22958(883 images per alphabet)
* Training dataset is reshaped for training model
* Target variable is encoded using one hot encoding
* 18366 images as training dataset after train test split
* 4592 images as validation/test dataset
* Created a trial model with convolution layer of 32 filters of size 5x5 and max pooling of size 2x2
* The trial model consists of :
    * A single convolution layer. It takes an input image with dimension of 28x28x1. Then it is convolved with 32 filters of size 5x5 resulting in dimension of 24x24x32 
    * And a single pooling layer which applies a filter of size 2x2 and a stride of 2. The resulting dimension will be 12x12x32.
    * A flattened layer is used as a connection layer between convolution and the fully connected dense layers.
    * There are 2 dense layers, first one with 128 neurons and the output layer with 26 neurons for predicting the 26 alphabets
    * This trial model after training resulted in a validation accuracy of 96.25% and training accuracy 99.30%
    * I used rectify linear function as the activation function for the convolution layer
    * The activation for the final output layer is softmax
* The solution requires multi-class classification(26 alphabet). Starting with a simple CNN to start with and we created the final CNN model after parameter tuning.
* As part of parameter tuning, a grid search for the fully connected dense layer neurons was done 
* A grid search was done for the batch size and finally for dropout ratio for training.
* Using the best parameters based on grid search, the final CNN model was created
* Final CNN model resulted in a validation accuracy of 98.26% and training accuracy of 99.71%
* Then I loaded the dataset and removed the unnamed column because it was an index to the dataset
*  then used the final model to predict the test dataset
* The prediction dataset from the model will contain the probability of each alphabet being recognised in the image.
* Then the letter with highest probability is mapped to the image
* 0 to 25 in the dataset is replaced with the alphabet characters and is saved to a csv file.


Details for second model
* Since I ran into memory issues in kaggle I had to split it into two notebooks 
* The first notebook outputs x train data and y train data after NCR Undersampling 
* These two sets of data are used in the second notebook to create the CNN model
* After selecting the best parameters I have commented out all the code for the parameter tuning and this notebook has the final model and prediction with the best resulting parameters
* Training accuracy is 99.67%
* Validation accuracy 99.68%
