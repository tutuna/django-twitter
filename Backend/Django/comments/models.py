from django.contrib.auth.models import User
from django.db import models
from tweets.models import Tweet



class Comment(models.Model):
	"""
	At this version, I will utilize an easy comment
	"""
	user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
	tweet = models.ForeignKey(Tweet, null=True, on_delete=models.SET_NULL)
	content = models.TextField(max_length=140)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		# sort all comments in a tweet
		index_together = (('tweet', 'created_at'),)

	def __str__(self):
		return '{} - {} says {} at tweet {}'.format(
			self.created_at,
			self.user,
			self.content,
			self.tweet_id,
		)