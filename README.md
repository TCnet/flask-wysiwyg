flask-wysiwyg provides custom form fields to render wysiwyg editor instead of regular textareas. It takes care of cleaning html for you too. With its super secure defaults you do not want to modified it's whitelisting rules.

how to use? from flask-wysiwyg import WysiwygField

class InfoForm(Form):
title=StringField('Title',validators=[Required(), Length(1, 64)]) body=WysiwygField("txteditor",validators=[Required()])
use "WysiwygField" field.

Don't forget the download the bootstrap-wysiwyg.add the css and javascrpts.

The demo in the static\flask_wysiwyg\bootstrap-wysiwyg\index.html
