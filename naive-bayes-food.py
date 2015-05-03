from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

categories=['healthy', 'unhealthy']

training=[
	('data/healthy.csv', 0),
	('data/unhealthy.csv', 1)
]

if __name__ == '__main__':
	data=[]
	target=[]
	for doc in training:
		file=open(doc[0])
		for line in file:
			line=line.rstrip();
			ls=line.split(',')
			target.append(doc[1])
			data.append(' '.join(ls[1:]))
	print target

	cv = CountVectorizer()
	x_count = cv.fit_transform(data)

	tf = TfidfTransformer(use_idf=False).fit(x_count)
	x_freq = tf.transform(x_count)

	classifier = MultinomialNB().fit(x_freq, target)
	test=['']
	test_count=cv.transform(test)
	test_freq=tf.transform(test_count)

	print classifier.predict(test_freq)[0]
