import nltk
import sklearn_crfsuite
from sklearn_crfsuite import metrics
import string 

class CRFNotTrainedError(Exception):
	"""
	New Exception that signified that the Conditional Random Field
	model is not trained.
	"""
	def __init__(self, m):
		self.message = m
	def __str__(self):
		return self.message

class Bookkeeping:
	"""
	This class is a Named-Entity Recognition (NER) program that builds on
	Conditional Random Field (CRF) machine learning model. 

	It is trained with a training file using self.learn() method, and the trained
	model is tested on a testing file using self.test() method. 

	To labeled a memo, the method self.predict_single_memo() is called on a memo string.
	"""

	def __init__(self):
		self.crf = None # stores the trained crf class model.

	def learn(self, trainFile):
		"""
		Function: train the CRF model using the trainFile calling methods from
		the imported module sklearn_crfsuite.
		"""
		train_list = self.get_train_file(trainFile) # receive the list of word tokens and their respective lables from the training file
		X_train = [self.sent2features(s) for s in train_list]	# a list of memo tokens from the training file
		y_train = [self.sent2labels(s) for s in train_list]		# a list of labels for the memo tokens from the training file


		# uses the CRF model from the module sklearn_crfsuite and train

		crf = sklearn_crfsuite.CRF(
			 algorithm='lbfgs', # L-BFGS algorithm is a gradient descent algorithm
		)
		crf.fit(X_train, y_train); # train the CRF model

		self.crf = crf

	def test(self, testFile):
		"""
		Function: test the trained CRF model using the testFile and calling methods from
		the imported module sklearn_crfsuite.
		"""
		if not self.crf: 
			# if the CRF model is not trained, raise error. 
			raise CRFNotTrainedError("CRF not trained yet.")

		test_list = self.get_test_file(testFile)	# receive the list of word tokens and their respective lables from the testing file
		X_test = [self.sent2features(s) for s in test_list] # a list of memo word tokens from the testing file
		y_test = [self.sent2labels(s) for s in test_list]	# a list of labels for the memo tokens from the testing file


		labels = list(self.crf.classes_) # the labels: "NAME", "LOC" (LOCATION), "O" (UNCATOGORIZED)

		y_pred = self.crf.predict(X_test)							# test the CRF module
		metrics.flat_f1_score(y_test, y_pred, 						# receive the F1-score from the testing
							   average='weighted', labels=labels)

		# sort the labels for higher readability when the F1-score is printed
		sorted_labels = sorted(
			 labels,
			 key=lambda name: (name[1:], name[0])
		)

		print(sklearn_crfsuite.metrics.flat_classification_report(
			 y_test, y_pred, labels=sorted_labels, digits=3
		))

	def predict_single_memo(self, sent):
		"""
		Function: Use the CRF model to label the new memo string sent. 
		"""
		if not self.crf:
			# if the CRF model is not trained, raise error. 
			raise CRFNotTrainedError("CRF not trained yet.")

		# tokenized the sentence and associate each token with feature functions
		# call the labels-predicting method from the imported module sklearn_crfsuite.
		sent_tokenized = [(s, None) for s in sent.split()] 
		X_test = self.sent2features(sent_tokenized)
		print(sent)
		print(list(zip(sent.split(), self.crf.predict_single(X_test))))


	def get_test_file(self, file_name):
		"""
		Function: Receive a testing file, which follows the format of "WORD 	LABEL" and ,
		and splits each word-label line into a tuple of word and its label. 

		Return: a list of tuples of words and its label (NAME, LOCATION, O)
		"""
		test_list = list()
		with open(file_name, encoding='utf-8') as testFile:
			labeled_memo = list()
			for line in testFile:
				if line != "\n":
					token_label = tuple(line.split())
					labeled_memo.append(token_label)
				else:
					test_list.append(labeled_memo)
					labeled_memo = list()

			if labeled_memo:
				test_list.append(labeled_memo) 

		print("Get Test File:", file_name)
		return test_list


	def get_train_file(self, file_name):
		"""
		Function: Receive a training file, which follows the format of "WORD 	LABEL" and ,
		and splits each word-label line into a tuple of word and its label. 

		Return: a list of tuples of words and its label (NAME, LOCATION, O)
		"""
		train_list = list()
		with open(file_name, encoding='utf-8') as trainFile:
			labeled_memo = list()
			for line in trainFile:
				if line != "\n":
					token_label = tuple(line.split())
					labeled_memo.append(token_label)
				else:
					train_list.append(labeled_memo)
					labeled_memo = list()

			if labeled_memo:
				train_list.append(labeled_memo) 

		print("Get Train File:", file_name)
		return train_list


	def word2features(self, sent, i):
		"""
		Feature functions that follows the format of CRF model in the sklearn-crfsuit module.

		The feature functions for a specific word w:
		1. Its entire word in lower case
		2. The first 4 characters
		3. The last 4 characters
		4. Whether it is a number
		5. Whether it has any digit number
		6. Whether it has any punctuation symbols such as '*', '-', etc.
		7. The features of the word (from feature 1 to 6) before w
		8. The features of the word (from feature 1 to 6) two-word before w
		9. The features of the word (from feature 1 to 6) after w
		10. The features of the word (from feature 1 to 6) two-word after w
		"""

		word = sent[i][0]	# the current word

		features = {	# the feature functions on the current word
			'bias': 1.0,
			'word.lower()': word.lower(),
			'word[-4:]': word[-4:],
			'word[:4]': word[:4],
			'word.isdigit()': word.isdigit(),
			'word.hasdigit()': any(char.isdigit() for char in word),
			'word.haspunct()': any(char in string.punctuation for char in word),
		}

		if i > 0:	# the feature functions on the word one-word before the current word
			word1 = sent[i-1][0]
			features.update({
				'-1:word.lower()': word1.lower(),
				'-1:word[-4:]': word1[-4:],
				'-1:word[:4]': word1[:4],
				'-1:word.hasdigit()': any(char.isdigit() for char in word1),
				'-1:word.haspunct()': any(char in string.punctuation for char in word1),
			})
		else:
			features['BOS'] = True

		if i > 1:	# the feature functions on the word two-word before the current word
			word2 = sent[i-2][0]
			features.update({
				'-2:word.lower()': word2.lower(),
				'-2:word[-4:]': word2[-4:],
				'-2:word[:4]': word2[:4],
				'-2:word.hasdigit()': any(char.isdigit() for char in word2),
				'-2:word.haspunct()': any(char in string.punctuation for char in word2),
			})


		if i < len(sent)-1:		# the feature functions on the word one-word after the current word
			word1 = sent[i+1][0]
			features.update({
				'+1:word.lower()': word1.lower(),
				'+1:word[-4:]': word1[-4:],
				'+1:word[:4]': word1[:4],
				'+1:word.hasdigit()': any(char.isdigit() for char in word1),
				'+1:word.haspunct()': any(char in string.punctuation for char in word1),
			})
		else:
			features['EOS'] = True

		if i < len(sent)-2:		# the feature functions on the word two-word after the current word
			word2 = sent[i+2][0]
			features.update({
				'+2:word.lower()': word2.lower(),
				'+2:word[-4:]': word2[-4:],
				'+2:word[:4]': word2[:4],
				'+2:word.hasdigit()': any(char.isdigit() for char in word2),
				'+2:word.ispunct()': word2[0] in string.punctuation,
				'+2:word.haspunct()': any(char in string.punctuation for char in word2),
			})

		return features

	def sent2features(self, sent):
		# apply the feature functions to each word token in a memo string sent
		return [self.word2features(sent, i) for i in range(len(sent))]

	def sent2labels(self, sent):
		# extract a list of labels from a list of tuples made up of the word token and its labels for a memo string
		try:
			return [label for token, label in sent]
		except ValueError:
			print(sent)
			raise ValueError

	def sent2tokens(self, sent):
		# extract a list of tokens from a list of tuples made up of the word token and its labels for a memo string
		try:
			return [token for token, label in sent]
		except ValueError:
			print(sent)
			raise ValueError



B = Bookkeeping()
B.learn("train1.txt")
B.test("test1.txt")
B.learn("train2.txt")
B.test("test2.txt")
B.learn("train3.txt")
B.test("test3.txt")
B.learn("train4.txt")
B.test("test4.txt")
B.learn("train5.txt")
B.test("test5.txt")
B.learn("train6.txt")
B.test("test6.txt")
B.learn("train7.txt")
B.test("test7.txt")
B.learn("train8.txt")
B.test("test8.txt")
B.learn("train9.txt")
B.test("test9.txt")
