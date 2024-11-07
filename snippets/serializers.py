from rest_framework import serializers
from snippets.models import Snippet

class SnippetSerializers(serializers.ModelSerializer):

    class Meta:
        model = Snippet
        fields = ['id', 'title', 'lineos']