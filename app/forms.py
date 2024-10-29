from django import forms

g=[['Male','male'], ['Female', 'female']]
c=[['Python', 'python'], ['django', 'django'],['Java', 'java']]

class StudentForm(forms.Form):
    sname=forms.CharField()
    sid=forms.IntegerField()
    semail=forms.EmailField()
    surl=forms.URLField()
    spassword=forms.CharField(widget=forms.PasswordInput)
    #sgender=forms.ChoiceField(choices=g)
    sgender=forms.ChoiceField(choices=g,widget=forms.RadioSelect)
    #scourse=forms.ChoiceField(choices=c)
    scourse=forms.MultipleChoiceField(choices=c,widget=forms.CheckboxSelectMultiple)
    saddress=forms.CharField(widget=forms.Textarea(attrs= {'cols':10,'rows':10}) )
