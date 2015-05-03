from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

categories=['healthy', 'unhealthy']

training=[
	('data/healthy.csv', 0),
	('data/unhealthy.csv', 1)
]

testing=[
	('data/healthy_test.csv',0),
	('data/unhealthy.csv', 1)
]

def read_file(doc):
	data=[]
	target=[]
	file=open(doc[0])
	for line in file:
		line=line.rstrip();
		ls=line.split(',')
		target.append(doc[1])
		data.append(' '.join(ls[2:]))
	file.close()
	return (data, target)

if __name__ == '__main__':

	train_data=[]
	train_target=[]
	for doc in training:
		res=read_file(doc)
		train_data+=res[0]
		train_target+=res[1]
	print train_target

	test_data=[]
	test_target=[]
	for doc in testing:
		res=read_file(doc)
		test_data+=res[0]
		test_target+=res[1]

	cv = CountVectorizer()
	train_count = cv.fit_transform(train_data)

	tf = TfidfTransformer(use_idf=False).fit(train_count)
	train_freq = tf.transform(train_count)

	classifier = MultinomialNB().fit(train_freq, train_target)

	test_count=cv.transform(test_data)
	test_freq=tf.transform(test_count)

	predictions = classifier.predict(test_freq)
	correct=0.0;
	for i in range(0,len(predictions)):
		if predictions[i]==test_target[i]:
			correct+=1
	rate=float(correct/len(predictions))*100
	print len(predictions),"predictions made and",correct,"of them are correct. This yields a",rate,"% success rate."
