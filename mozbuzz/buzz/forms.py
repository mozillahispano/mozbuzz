from django.forms import ModelForm, TextInput
from mozbuzz.buzz.models import Mention, FollowUp


class MentionForm(ModelForm):
    class Meta:
        model = Mention
        fields = ('link', 'origin', 'source_name', 'text', 'type', 'feedback',
                  'country', 'author_expertise', 'previous_product_comments',
                  'product', 'estimated_audience', 'relevant_audience',
                  'update_rate', 'remarks')
        widgets = {
            "source_name": TextInput
        }


class FollowUpForm(ModelForm):
    class Meta:
        model = FollowUp
        fields = ('status', 'remarks')
        
