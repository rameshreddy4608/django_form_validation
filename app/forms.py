from django import forms
g=[['MALE','male'],('FEMALE','female')]
c=[['python','PYTHON'],('django','django'),['sql','sql']]
class studentform(forms.Form):
    name=forms.CharField(max_length=100)
    age=forms.IntegerField()
    email=forms.EmailField()
    date=forms.DateField()
    password=forms.CharField(max_length=100,widget=forms.PasswordInput)
    address=forms.CharField(max_length=100,widget=forms.Textarea(attrs={'cols':10,'rows':5}))
    gender=forms.ChoiceField(choices=g,widget=forms.RadioSelect )
    course=forms.MultipleChoiceField(choices=c,widget=forms.CheckboxSelectMultiple)
