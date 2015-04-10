from django.core.exceptions import ValidationError

'''
	Function that valid extension
	when upload file in form
'''
def valid_extension(value):

	if (not value.name.endswith('.pdf') and 
		not value.name.endswith('.jpg')):

		raise ValidationError('Files allowed: .jpg and .pdf')
