from django.forms import ModelForm

from .models import Message


class ContactForm(ModelForm):
    class Meta:
        model = Message
        fields = ['sender_name', 'sender_email', 'company', 'message']

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['sender_name'].widget.attrs.update({
            'id': 'contact-form-name',
            'placeholder': 'Mike Wazowski'
        })
        self.fields['sender_email'].widget.attrs.update({
            'id': 'contact-form-email',
            'placeholder': 'wazowski@monsters.com'
        })
        self.fields['company'].widget.attrs.update({
            'id': 'contact-form-company',
            'placeholder': "Monsters, Inc."
        })
        self.fields['message'].widget.attrs.update({
            'id': 'contact-form-message',
            'rows': 8,
            'placeholder': "Your message..."
        })
