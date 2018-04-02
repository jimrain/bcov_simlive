from rest_framework import serializers
from simlive.models import BCAccount, Video


class BCAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = BCAccount
        fields = ('id', 'name', 'accountId', 'clientId', 'clientSecret', 'liveAccountId', 'liveApiToken', 'liveClippingCreds')

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ('id', 'title', 'bcAccount', 'video_id', 'duration', 'description', 'path')

