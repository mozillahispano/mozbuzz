from django.forms import ModelForm
from mozbuzz.buzz.models import Mention

class MentionForm(ModelForm):
    class Meta:
        model = Mention
        fields = ('type','origin', 'feedback', 'link', 'text', 
                  'author_expertise', 'previous_product_comments', 
                  'estimated_audience', 'relevant_audience', 'update_rate', 
                  'remarks')

