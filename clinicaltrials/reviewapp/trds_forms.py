# coding: utf-8

from clinicaltrials.reviewapp.models import Attachment
from django import forms
from django.utils.translation import ugettext as _

ACCESS = [
    ('public', 'Public'),
    ('private', 'Private'),
]


class ExistingAttachmentForm(forms.ModelForm):
    class Meta:
        model = Attachment
        exclude = ['submission']

    title = _('Existing Attachment')
    file = forms.CharField(required=False,label=_('File'),max_length=255)

class NewAttachmentForm(forms.ModelForm):
    class Meta:
        model = Attachment
        fields = ['file','description','submission','public']

    title = _('New Attachment')
    submission = forms.CharField(widget=forms.HiddenInput,required=False)

