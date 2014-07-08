from flask import render_template
from wtforms.widgets.core import HTMLString, html_params, escape
from wtforms import StringField,TextField,Field
from wtforms.compat import text_type, string_types, iteritems

class WysiwygWidget(object):

    def __call__(self, field, **kwargs):
        kwargs.setdefault('id', field.id)
        html=''
        html+='<div class=\"btn-toolbar m-b-sm btn-editor\" data-role=\"editor-toolbar\"data-target=\"#editor\"><div class=\"btn-group\"><a class=\"btn btn-default btn-sm dropdown-toggle\" data-toggle=\"dropdown\"        title=\"Font\"><i class=\"fa fa-font\"></i><b class=\"caret\"></b></a><ul class=\"dropdown-menu\"></ul></div><div class=\"btn-group\"><a class=\"btn btn-default btn-sm dropdown-toggle\" data-toggle=\"dropdown\"        title=\"Font Size\"><i class=\"fa fa-text-height\"></i>            &nbsp;<b class=\"caret\"></b></a><ul class=\"dropdown-menu\"><li><a data-edit=\"fontSize 5\"><font size=\"5\">                        Huge</font></a></li><li><a data-edit=\"fontSize 3\"><font size=\"3\">                        Normal</font></a></li><li><a data-edit=\"fontSize 1\"><font size=\"1\">                        Small</font></a></li></ul></div><div class=\"btn-group\"><a class=\"btn btn-default btn-sm\" data-edit=\"bold\" title=\"Bold (Ctrl/Cmd+B)\"><i class=\"fa fa-bold\"></i></a><a class=\"btn btn-default btn-sm\" data-edit=\"italic\" title=\"Italic (Ctrl/Cmd+I)\"><i class=\"fa fa-italic\"></i></a><a class=\"btn btn-default btn-sm\" data-edit=\"strikethrough\" title=\"Strikethrough\"><i class=\"fa fa-strikethrough\"></i></a><a class=\"btn btn-default btn-sm\" data-edit=\"underline\" title=\"Underline (Ctrl/Cmd+U)\"><i class=\"fa fa-underline\"></i></a></div><div class=\"btn-group\"><a class=\"btn btn-default btn-sm\" data-edit=\"insertunorderedlist\" title=\"Bullet list\"><i class=\"fa fa-list-ul\"></i></a><a class=\"btn btn-default btn-sm\" data-edit=\"insertorderedlist\" title=\"Number list\"><i class=\"fa fa-list-ol\"></i></a><a class=\"btn btn-default btn-sm\" data-edit=\"outdent\" title=\"Reduce indent (Shift+Tab)\"><i class=\"fa fa-dedent\"></i></a><a class=\"btn btn-default btn-sm\" data-edit=\"indent\" title=\"Indent (Tab)\"><i class=\"fa fa-indent\"></i></a></div><div class=\"btn-group\"><a class=\"btn btn-default btn-sm\" data-edit=\"justifyleft\" title=\"Align Left (Ctrl/Cmd+L)\"><i class=\"fa fa-align-left\"></i></a><a class=\"btn btn-default btn-sm\" data-edit=\"justifycenter\" title=\"Center (Ctrl/Cmd+E)\"><i class=\"fa fa-align-center\"></i></a><a class=\"btn btn-default btn-sm\" data-edit=\"justifyright\" title=\"Align Right (Ctrl/Cmd+R)\"><i class=\"fa fa-align-right\"></i></a><a class=\"btn btn-default btn-sm\" data-edit=\"justifyfull\" title=\"Justify (Ctrl/Cmd+J)\"><i class=\"fa fa-align-justify\"></i></a></div><div class=\"btn-group\"><a class=\"btn btn-default btn-sm dropdown-toggle\" data-toggle=\"dropdown\"        title=\"Hyperlink\"><i class=\"fa fa-link\"></i></a><div class=\"dropdown-menu\"><div class=\"input-group m-l-xs m-r-xs\"><input class=\"form-control input-sm\" placeholder=\"URL\" type=\"text\" data-edit=\"createLink\"                /><div class=\"input-group-btn\"><button class=\"btn btn-default btn-sm\" type=\"button\">                        Add</button></div></div></div><a class=\"btn btn-default btn-sm\" data-edit=\"unlink\" title=\"Remove Hyperlink\"><i class=\"fa fa-cut\"></i></a></div><div class=\"btn-group hide\"><a class=\"btn btn-default btn-sm\" title=\"Insert picture (or just drag & drop)\"        id=\"pictureBtn\"><i class=\"fa fa-picture-o\"></i></a><input type=\"file\" data-role=\"magic-overlay\" data-target=\"#pictureBtn\"        data-edit=\"insertImage\" /></div><div class=\"btn-group\"><a class=\"btn btn-default btn-sm\" data-edit=\"undo\" title=\"Undo (Ctrl/Cmd+Z)\"><i class=\"fa fa-undo\"></i></a><a class=\"btn btn-default btn-sm\" data-edit=\"redo\" title=\"Redo (Ctrl/Cmd+Y)\"><i class=\"fa fa-repeat\"></i></a></div></div>'
        html+='<textarea class=\"hide flask-wysiwyg\"   data-editor=\"editor\" %s>%s</textarea>'
        html+='<div id=\"editor\"   style=\"overflow:scroll;height:150px;max-height:150px\"  class="bootstrap-wysiwyg form-control" >%s</div>'
        
        
        return HTMLString(html % (html_params(name=field.name, **kwargs), escape(text_type(field._value())),escape(text_type(field._value()))))

    
 


class WysiwygField(TextField):
    widget = WysiwygWidget()
  

   
    
    