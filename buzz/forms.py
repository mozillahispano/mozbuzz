from django.forms import ModelForm
from mozbuzz.buzz.models import Mention, FollowUp

class MentionForm(ModelForm):
    class Meta:
        model = Mention
        fields = ('type','origin', 'feedback', 'link', 'text', 
                  'author_expertise', 'previous_product_comments', 
                  'estimated_audience', 'relevant_audience', 'update_rate', 
                  'remarks')

class FollowUpForm(ModelForm):
    class Meta:
        model = FollowUp
        fields = ('status','remarks')
