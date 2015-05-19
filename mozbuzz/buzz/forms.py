from django.forms import ModelForm, TextInput, ClearableFileInput
from mozbuzz.buzz.models import Mention, FollowUp

'''
  Changes order fields
'''
class CustomClearableFileInput(ClearableFileInput):
    template_with_clear = '<br>  <label for="%(clear_checkbox_id)s">%(clear_checkbox_label)s</label> %(clear)s'

class MentionForm(ModelForm):
    class Meta:
        model = Mention
        fields = ('link', 'origin', 'source_name', 'text', 'type', 'feedback',
                  'country', 'author_expertise', 'previous_product_comments',
                  'product', 'estimated_audience', 'relevant_audience',
                  'update_rate', 'remarks', 'upload_file')
        widgets = {
            "source_name": TextInput,
            'upload_file': CustomClearableFileInput
        }


class FollowUpForm(ModelForm):
    class Meta:
        model = FollowUp
        fields = ('status', 'remarks')
        
