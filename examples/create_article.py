import pureodm
import pureodm.codecs
import pymongo

class Article(pureodm.Model):
	fields = {
		'title': {
			'type': unicode,
			'required': True
		},
		'body': {
			'type': unicode
		},
		'attachments': {
			'type': [str],
			'codec': pureodm.codecs.Base64Codec
		}
	}

if __name__ == '__main__':
	connection = pymongo.Connection(host='localhost', port=27017)
	database = connection['pureodmTest']
	articles = database['articles']

	article = Article(title=u'This one time, I wrote an object-document mapper.')
	attachments = ['some-picture.png']
	article['attachments'] = attachments

	print(article.save_to(None))

	for attachment in article['attachments']:
		print(attachment)
		
	connection.close()
