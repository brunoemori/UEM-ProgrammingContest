from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    title = forms.CharField(max_length=64, widget=forms.TextInput(attrs={"placeholder": "Problem title"}))

    problemNumber = forms.IntegerField(widget=forms.TextInput(attrs={"placeholder": "Problem number"}))

    inputs = forms.CharField(required=False, max_length=64, 
        widget=forms.Textarea(attrs={"placeholder": "Inputs", 'onkeydown': 'insertTab(this, event);', 'class': 'my-0'}))

    outputs = forms.CharField(required=False, max_length=64, 
            widget=forms.Textarea(attrs={"placeholder": "Outputs", 'onkeydown': 'insertTab(this, event);', 'class': 'my-0'}))

    body = forms.CharField(widget=forms.Textarea(attrs={"placeholder": "Description", 'onkeydown': 'insertTab(this, event);'}))

    bodyCode = forms.CharField(required=False, 
            widget=forms.Textarea(attrs={"placeholder": "Your code", 'onkeydown': 'insertTab(this, event);', 
            'class': 'codemirror-inputarea'}))

    class Meta:
        model = Article
        fields=('title', 'problemNumber', 'inputs', 'outputs', 'body', 'bodyCode')

    def clean(self, *args, **kwargs):
        articleNumber = self.cleaned_data.get('problemNumber')

        try:
            exists = Article.objects.all().filter(problemNumber=articleNumber)

        except Article.DoesNotExists:
            exists = None

        if (exists):
            raise forms.ValidationError('This problem already exists on this wiki.')
    
        return super(ArticleForm, self).clean(*args, **kwargs)
