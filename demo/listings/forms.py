from django import Form


class carform(forms.Form):

    title = forms.CharField(label='title of the car', max_length=100)
    