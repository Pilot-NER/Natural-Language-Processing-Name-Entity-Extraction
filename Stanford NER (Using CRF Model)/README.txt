This README file is about how to run the Stanford NER on our transaction memos list.

1. Decide which training file (files with .tok) in the folder stanford-ner to use for training Stanford NER program.

2. Change the line "trainFile = train1.tok" into "trainFile = (file that you decide)" in the train.prop file in the folder
stanford-ner

3. Inside the folder stanford-ner, run the command "java -cp stanford-ner.jar edu.stanford.nlp.ie.crf.CRFClassifier -prop train.prop"
in the command prompt to train the CRF model.

4. Inside the folder stanford-ner, run the command "java -cp stanford-ner.jar edu.stanford.nlp.ie.crf.CRFClassifier -loadClassifier ner-model.ser.gz -testFile test1.tsv" in the command prompt to test the trained CRF model. (Remember to change the corresponding testing file name for the phrase "-testFile test1.tsv" if you pick a training file
except "train1.tok")

