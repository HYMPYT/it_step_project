from django import forms

from .models import Post


class PostCreationForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body', 'image')

    def save(self, user, *args, **kwargs):
        post = Post.objects.create(title=self.data.get('title'), body=self.data.get('body'), poster=user)

        print(self.data)

        if self.data.get('image'):
            post.image = self.data.get('image')

        post.save()
