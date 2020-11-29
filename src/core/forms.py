from django.forms import ModelForm

from .models import Post
from common.models import Photo


class PostCreationForm(ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body', 'image')

    def save(self, user, *args, **kwargs):
        post = Post.objects.create(title=self.data.get('title'), body=self.data.get('body'), poster=user)

        print(self.data)

        if self.data.get('image'):
            post.image = Photo.objects.get(pk=self.data.get('image'))

        post.save()
