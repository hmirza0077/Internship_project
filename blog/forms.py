from django import forms
from .models import Post
from .models import Comments
from django.utils.translation import gettext_lazy as _

class CommentsForm(forms.ModelForm):
    first_name = forms.CharField(max_length=50, label=False, widget=forms.TextInput(attrs={'placeholder': _('نام شما')}))
    # email = forms.EmailField(max_length=50, label=False, widget=forms.TextInput(attrs={'placeholder': _('ایمیل شما')}))
    body = forms.CharField(max_length=50, label=False, widget=forms.Textarea(attrs={'placeholder': _('دیدگاه شما')}))
    #content_type = forms.CharField(max_length=50, label=False, widget=forms.TextInput(attrs={'placeholder': 'موضوع'}))

    
    def get_comment_create_data(self, site_id=None):
        data = super(CommentsForm, self).get_comment_create_data()
        data.update({'title': self.cleaned_data['title']})
        return data

    class Meta:
        model = Comments
        fields = ('first_name', 'body',)
