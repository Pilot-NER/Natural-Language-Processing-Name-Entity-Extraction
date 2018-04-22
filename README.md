# NLP-Approach: Conditional Random Field (CRF) for Named-Entity Recognition

### How CRF works:
In very broad terms, CRF rates each word in the text based on predetermined features (ex: Capitalisation, word length, etc) and labels each word based on its features as well as the features of the words surrounding it. CRF uses feature functions to quantify different features of each word in a sentence. Examples of features include whether the word is capitalized. The feature function takes four basic parameters as input – a sentence *s* , the position *i* of a word in the sentence, the label L<sub>i</sub> of the current word, and the label L<sub>i-1</sub> of the previous word – and then outputs a real number. For example, a feature function  f(s, i, L<sub>i</sub>,  L<sub>i-1</sub>) can be designed to output 1 if the position *i*  = 1, L<sub>i</sub> = NAME and the first character of the word is capitalized. Each output of a feature function f<sub>*j*</sub>  is associated with a weight λ<sub>*j*</sub>. Overall, there is an n-dimensional vector V<sub>f</sub> = { f<sub>1</sub>(x), f<sub>2</sub>(x), ..., f<sub>n</sub>(x)} for a word input x and a n-dimensional vector of weights V<sub>λ</sub> = { λ<sub>1</sub>, λ<sub>2</sub>, ... , λ<sub>n</sub>}. The sum of the scalar product between V<sub>f</sub> and V<sub>λ</sub> for each word in the entire sentence outputs a score S which quantifies how accurate the sequence of labels are for the sentence. To generate the highest possible S, which signifies the best labeling of the sentence, V<sub>λ</sub> is optimized through gradient descent, which is as follows:
1. For each feature function f<sub>*j*</sub>, randomly assign a value between 0 to 1 to the associated weight λ<sub>*j*</sub>. 
2. Carry out the following iterations until a certain number of iterations is performed (the stopping condition):
  1. Calculate the gradient of the log of probability for the score s (obtained through exponentiation and normalization) with respect to  λ<sub>*j*</sub>.
  2. Move  λ<sub>*j*</sub> in the direction of the gradient with a constant learning rate α.
3. The vector of weights V<sub>λ</sub> is optimized.

### Results:
For 10/90 split of memos data:
The F1-score for Stanford Named Entity Recognizer (NER) is 40.12%
The F1-score for our CRF with custom features is 80.00%.

For 90/10 split of memos data:
The F1-score for Stanford Named Entity Recognizer (NER) is 69.87%
The F1-score for our CRF with custom features is 89.00%.

Example:
![Example](https://github.com/Final-Project-Freshman/NLP-Approach/blob/master/result.png)
