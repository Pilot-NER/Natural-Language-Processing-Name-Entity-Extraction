# NLP-Approach: Conditional Random Field (CRF) for Named-Entity Recognition

### How CRF works:
In very broad terms, CRF rates each word in the text based on predetermined features (ex: Capitalisation, word length, etc) and labels each word based on its features as well as the features of the words surrounding it. CRF uses feature functions to quantify different features of each word in a sentence. Examples of features include whether the word is capitalized. The feature function takes four basic parameters as input – a sentence *s* , the position *i* of a word in the sentence, the label L<sub>i</sub> of the current word, and the label L<sub>i-1</sub> of the previous word – and then outputs a real number. For example, a feature function  f(s, i, L<sub>i</sub>,  L<sub>i-1</sub>) can be designed to output 1 if the position *i*  = 1, L<sub>i</sub> = NAME and the first character of the word is capitalized. Each output of a feature function f<sub>*j*</sub>  is associated with a weight λ<sub>*j*</sub>. Overall, there is an n-dimensional vector V<sub>f</sub> = { f<sub>1</sub>(x), f<sub>2</sub>(x), ..., f<sub>n</sub>(x)} for a word input x and a n-dimensional vector of weights V<sub>λ</sub> = { λ<sub>1</sub>, λ<sub>2</sub>, ... , λ<sub>n</sub>}. The sum of the scalar product between V<sub>f</sub> and V<sub>λ</sub> for each word in the entire sentence outputs a score S which quantifies how accurate the sequence of labels are for the sentence. To generate the highest possible S, which signifies the best labeling of the sentence, V<sub>λ</sub> is optimized through gradient descent, which is as follows:
1. For each feature function f<sub>*j*</sub>, randomly assign a value between 0 to 1 to the associated weight λ<sub>*j*</sub>. 
2. Carry out the following iterations until a certain number of iterations is performed (the stopping condition):
  1. Calculate the gradient of the log of probability for the score s (obtained through exponentiation and normalization) with respect to  λ<sub>*j*</sub>.
  2. Move  λ<sub>*j*</sub> in the direction of the gradient with a constant learning rate α.
3. The vector of weights V<sub>λ</sub> is optimized.

### Stanford NER
Stanford NER is one of the most widely used open-source NER programs which provides a general Java implementation of the CRF model. To train the program, we labeled each word token in the list of transaction memos with “NAME”, “LOCATION”, or “O” (uncategorized). After training Stanford NER with different partitioning ratios of data, we found that as the sample size of training data increases, the F1-score of the Stanford NER model increases, as shown in the following figure. F1-score is a measure of accuracy in statistical analysis of binary classification. It is the average of both the precision and the recall score.The precision score is the ratio of all accurate classifications divided by all our classifications while the recall score is the number of accurate classifications divided by the number of the all possible accurate classifications.

The F1-score increases with the size of training data because the variance of the testing data decreases as the partitioning ratio of training data and testing data increases. However, for the recommended 70:30 split (Ng, n.d.), the F1-score is merely 0.63. The accuracy is lower than the accuracy of our rule-based NER model. The primary reason is that Stanford NER considers features based on English grammar which is not applicable to bank memos. For instance, Stanford NER checks whether the first letter of a word is a capital letter to determine if the word is a vendor’s name, but many memos are fully capitalized. Moreover, Stanford NER uses a feature function that detects parts-of-the-speech (POS) such as adjectives, nouns, verbs, and prepositions, but memos are syntactically incorrect.

### CRF with Custom Feature Functions

We built our own CRF model specifically for bank memos. We used the Python package “sklearn-crfsuite” package to customize the feature functions of the CRF model based on our observations of patterns in the sample dataset. The feature functions measure the following features:

![Table of features]()

The feature functions for a word measures the features of itself, the two words before it, and the two words after it. This is because we found that this increased the F1-score of our program.
After training our custom CRF NER model using the sample dataset, we found that for all partitioning ratios, the F1-scores of our NER model are higher than that for Stanford NER model. Surprisingly, even with a 20:80 partition, the F1-score for our NER model in labeling the remaining memos exceeds 80%. This suggests that there are notably salient patterns that are generalizable to all sample memos. Additionally, in the result figure, the gradient of the regression in partitioning ratio against F1-scores for our model is smaller than the Stanford model. This means that our custom NER model can learn the patterns of features with a smaller size of training data.

![Result Figure]()

![Result of Custom CRF](https://github.com/Final-Project-Freshman/NLP-Approach/blob/master/result.png)
