import nltk
import sklearn_crfsuite
from sklearn_crfsuite import metrics
import string 

class CRFNotTrained(Exception):
	def __init__(self, m):
		self.message = m
	def __str__(self):
		return self.message

class Bookkeeping:

	def __init__(self):
		self.crf = None

	def learn(self, trainFile):
		train_list = self.get_train_file(trainFile)
		X_train = [self.sent2features(s) for s in train_list]
		y_train = [self.sent2labels(s) for s in train_list]

		crf = sklearn_crfsuite.CRF(
			 algorithm='lbfgs',
		)
		crf.fit(X_train, y_train);

		self.crf = crf

	def test(self, testFile):
		if not self.crf:
			raise CRFNotTrained("CRF not trained yet.")

		test_list = self.get_test_file(testFile)
		X_test = [self.sent2features(s) for s in test_list]
		y_test = [self.sent2labels(s) for s in test_list]


		labels = list(self.crf.classes_)
		# labels.remove('O')

		y_pred = self.crf.predict(X_test)
		metrics.flat_f1_score(y_test, y_pred,
							   average='weighted', labels=labels)


		# group B and I results
		sorted_labels = sorted(
			 labels,
			 key=lambda name: (name[1:], name[0])
		)
		print(sklearn_crfsuite.metrics.flat_classification_report(
			 y_test, y_pred, labels=sorted_labels, digits=3
		))

	def predict_single_memo(self, sent):
		if not self.crf:
			raise CRFNotTrained("CRF not trained yet.")

		sent_tokenized = [(s, None) for s in sent.split()]
		X_test = self.sent2features(sent_tokenized)
		print(sent)
		print(list(zip(sent.split(), self.crf.predict_single(X_test))))


	def get_test_file(self, file_name):
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
		word = sent[i][0]

		features = {
			'bias': 1.0,
			'word.lower()': word.lower(),
			'word[-3:]': word[-4:],
			'word[:3]': word[:4],
			'word.isupper()': word.isupper(),
			'word.istitle()': word.istitle(),
			'word.isdigit()': word.isdigit(),
			'word.hasdigit()': any(char.isdigit() for char in word),
			'word.haspunct()': any(char in string.punctuation for char in word),
		}

		if i > 0:
			word1 = sent[i-1][0]
			features.update({
				'-1:word.lower()': word1.lower(),
				'-1:word.istitle()': word1.istitle(),
				'-1:word.isupper()': word1.isupper(),
				'-1:word[-3:]': word1[-4:],
				'-1:word[:3]': word1[:4],
				'-1:word.hasdigit()': any(char.isdigit() for char in word1),
				'-1:word.haspunct()': any(char in string.punctuation for char in word1),
			})
		else:
			features['BOS'] = True

		if i > 1:
			word2 = sent[i-2][0]
			features.update({
				'-2:word.lower()': word2.lower(),
				'-2:word.istitle()': word2.istitle(),
				'-2:word.isupper()': word2.isupper(),
				'-2:word[-3:]': word2[-4:],
				'-2:word[:3]': word2[:4],
				'-2:word.hasdigit()': any(char.isdigit() for char in word2),
				'-2:word.haspunct()': any(char in string.punctuation for char in word2),
			})


		if i < len(sent)-1:
			word1 = sent[i+1][0]
			features.update({
				'+1:word.lower()': word1.lower(),
				'+1:word.istitle()': word1.istitle(),
				'+1:word.isupper()': word1.isupper(),
				'+1:word[-3:]': word1[-4:],
				'+1:word[:3]': word1[:4],
				'+1:word.hasdigit()': any(char.isdigit() for char in word1),
				'+1:word.haspunct()': any(char in string.punctuation for char in word1),
			})
		else:
			features['EOS'] = True

		if i < len(sent)-2:
			word2 = sent[i+2][0]
			features.update({
				'+2:word.lower()': word2.lower(),
				'+2:word.istitle()': word2.istitle(),
				'+2:word.isupper()': word2.isupper(),
				'+2:word[-3:]': word2[-4:],
				'+2:word[:3]': word2[:4],
				'+2:word.hasdigit()': any(char.isdigit() for char in word2),
				'+2:word.ispunct()': word2[0] in string.punctuation,
				'+2:word.haspunct()': any(char in string.punctuation for char in word2),
			})

		return features

	def sent2features(self, sent):
		return [self.word2features(sent, i) for i in range(len(sent))]

	def sent2labels(self, sent):
		try:
			return [label for token, label in sent]
		except ValueError:
			print(sent)
			raise ValueError

	def sent2tokens(self, sent):
		try:
			return [token for token, label in sent]
		except ValueError:
			print(sent)
			raise ValueError



B = Bookkeeping()
B.learn("train9.txt")
B.test("test9.txt")
B.predict_single_memo("LOS ANGELES AIRPORT LOS ANGELES AIRPORT LOS ANGELES CA Ref5531020AALA Crd3846 Dt11/25")