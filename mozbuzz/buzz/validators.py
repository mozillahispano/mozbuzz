from django.core.exceptions import ValidationError

'''
	Function that valid extension
	when upload file in form
'''
def valid_extension(value):

	if (not value.name.endswith('.pdf') and 
		not value.name.endswith('.jpg') and
		not value.name.endswith('.png') and 
		not value.name.endswith('.gif') and 
		not value.name.endswith('.jpeg') and 
		not value.name.endswith('.bmp') and
		not value.name.endswith('.ico') and 
		not value.name.endswith('.txt') and
		not value.name.endswith('.doc') and 
		not value.name.endswith('.docx') and 
		not value.name.endswith('.odt')):

		files_allowed = ""
		files_allowed = files_allowed + ".pdf, .jpg, .png, .gif,"
		files_allowed = files_allowed + " .jpeg, .bmp, .ico, .doc,"
		files_allowed = files_allowed + " .docx, .odt, .txt"
		raise ValidationError('Files allowed: ' + files_allowed)
