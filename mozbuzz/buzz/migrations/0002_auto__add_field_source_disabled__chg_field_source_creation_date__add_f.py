# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Source.disabled'
        db.add_column('buzz_source', 'disabled', self.gf('django.db.models.fields.BooleanField')(default=False), keep_default=False)

        # Changing field 'Source.creation_date'
        db.alter_column('buzz_source', 'creation_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True))

        # Adding field 'AuthorExpertise.disabled'
        db.add_column('buzz_authorexpertise', 'disabled', self.gf('django.db.models.fields.BooleanField')(default=False), keep_default=False)

        # Changing field 'AuthorExpertise.creation_date'
        db.alter_column('buzz_authorexpertise', 'creation_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True))

        # Adding field 'File.disabled'
        db.add_column('buzz_file', 'disabled', self.gf('django.db.models.fields.BooleanField')(default=False), keep_default=False)

        # Changing field 'File.creation_date'
        db.alter_column('buzz_file', 'creation_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True))

        # Changing field 'Report.creation_date'
        db.alter_column('buzz_report', 'creation_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True))

        # Adding field 'Product.disabled'
        db.add_column('buzz_product', 'disabled', self.gf('django.db.models.fields.BooleanField')(default=False), keep_default=False)

        # Changing field 'Product.creation_date'
        db.alter_column('buzz_product', 'creation_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True))

        # Adding field 'Mention.disabled'
        db.add_column('buzz_mention', 'disabled', self.gf('django.db.models.fields.BooleanField')(default=False), keep_default=False)

        # Changing field 'Mention.creation_date'
        db.alter_column('buzz_mention', 'creation_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True))

        # Changing field 'Mention.last_update_date'
        db.alter_column('buzz_mention', 'last_update_date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True))

        # Adding field 'MentionType.disabled'
        db.add_column('buzz_mentiontype', 'disabled', self.gf('django.db.models.fields.BooleanField')(default=False), keep_default=False)

        # Changing field 'MentionType.creation_date'
        db.alter_column('buzz_mentiontype', 'creation_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True))


    def backwards(self, orm):
        
        # Deleting field 'Source.disabled'
        db.delete_column('buzz_source', 'disabled')

        # Changing field 'Source.creation_date'
        db.alter_column('buzz_source', 'creation_date', self.gf('django.db.models.fields.DateTimeField')())

        # Deleting field 'AuthorExpertise.disabled'
        db.delete_column('buzz_authorexpertise', 'disabled')

        # Changing field 'AuthorExpertise.creation_date'
        db.alter_column('buzz_authorexpertise', 'creation_date', self.gf('django.db.models.fields.DateTimeField')())

        # Deleting field 'File.disabled'
        db.delete_column('buzz_file', 'disabled')

        # Changing field 'File.creation_date'
        db.alter_column('buzz_file', 'creation_date', self.gf('django.db.models.fields.DateTimeField')())

        # Changing field 'Report.creation_date'
        db.alter_column('buzz_report', 'creation_date', self.gf('django.db.models.fields.DateTimeField')())

        # Deleting field 'Product.disabled'
        db.delete_column('buzz_product', 'disabled')

        # Changing field 'Product.creation_date'
        db.alter_column('buzz_product', 'creation_date', self.gf('django.db.models.fields.DateTimeField')())

        # Deleting field 'Mention.disabled'
        db.delete_column('buzz_mention', 'disabled')

        # Changing field 'Mention.creation_date'
        db.alter_column('buzz_mention', 'creation_date', self.gf('django.db.models.fields.DateTimeField')())

        # Changing field 'Mention.last_update_date'
        db.alter_column('buzz_mention', 'last_update_date', self.gf('django.db.models.fields.DateTimeField')())

        # Deleting field 'MentionType.disabled'
        db.delete_column('buzz_mentiontype', 'disabled')

        # Changing field 'MentionType.creation_date'
        db.alter_column('buzz_mentiontype', 'creation_date', self.gf('django.db.models.fields.DateTimeField')())


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'buzz.authorexpertise': {
            'Meta': {'object_name': 'AuthorExpertise'},
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'creation_user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'disabled': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'buzz.country': {
            'Meta': {'object_name': 'Country'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'})
        },
        'buzz.file': {
            'Meta': {'object_name': 'File'},
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'creation_user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'disabled': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'})
        },
        'buzz.mention': {
            'Meta': {'object_name': 'Mention'},
            'author_expertise': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['buzz.AuthorExpertise']"}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'creation_user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'creator'", 'to': "orm['auth.User']"}),
            'disabled': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'estimated_audience': ('django.db.models.fields.IntegerField', [], {}),
            'feedback': ('django.db.models.fields.IntegerField', [], {'max_length': '1'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_update_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'last_update_user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'updater'", 'to': "orm['auth.User']"}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'origin': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['buzz.Source']"}),
            'previous_product_comments': ('django.db.models.fields.IntegerField', [], {'max_length': '1'}),
            'relevant_audience': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'remarks': ('django.db.models.fields.TextField', [], {}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['buzz.MentionType']"}),
            'update_rate': ('django.db.models.fields.IntegerField', [], {'max_length': '1'})
        },
        'buzz.mentiontype': {
            'Meta': {'object_name': 'MentionType'},
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'creation_user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'disabled': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'})
        },
        'buzz.product': {
            'Meta': {'object_name': 'Product'},
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'creation_user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'disabled': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'})
        },
        'buzz.report': {
            'Meta': {'object_name': 'Report'},
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'creation_user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'report_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['buzz.ReportType']"})
        },
        'buzz.reporttype': {
            'Meta': {'object_name': 'ReportType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'})
        },
        'buzz.source': {
            'Meta': {'object_name': 'Source'},
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'creation_user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'disabled': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'})
        },
        'buzz.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['buzz']
