# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'UserProfile'
        db.create_table('buzz_userprofile', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
        ))
        db.send_create_signal('buzz', ['UserProfile'])

        # Adding model 'Product'
        db.create_table('buzz_product', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50, db_index=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('creation_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('creation_user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
        ))
        db.send_create_signal('buzz', ['Product'])

        # Adding model 'ReportType'
        db.create_table('buzz_reporttype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50, db_index=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('buzz', ['ReportType'])

        # Adding model 'Country'
        db.create_table('buzz_country', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50, db_index=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('buzz', ['Country'])

        # Adding model 'File'
        db.create_table('buzz_file', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50, db_index=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('creation_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('creation_user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
        ))
        db.send_create_signal('buzz', ['File'])

        # Adding model 'Source'
        db.create_table('buzz_source', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50, db_index=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('creation_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('creation_user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
        ))
        db.send_create_signal('buzz', ['Source'])

        # Adding model 'MentionType'
        db.create_table('buzz_mentiontype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50, db_index=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('creation_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('creation_user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
        ))
        db.send_create_signal('buzz', ['MentionType'])

        # Adding model 'AuthorExpertise'
        db.create_table('buzz_authorexpertise', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('creation_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('creation_user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
        ))
        db.send_create_signal('buzz', ['AuthorExpertise'])

        # Adding model 'Mention'
        db.create_table('buzz_mention', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('creation_user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='creator', to=orm['auth.User'])),
            ('creation_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('last_update_user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='updater', to=orm['auth.User'])),
            ('last_update_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('link', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('text', self.gf('django.db.models.fields.TextField')()),
            ('origin', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['buzz.Source'])),
            ('type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['buzz.MentionType'])),
            ('author_expertise', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['buzz.AuthorExpertise'])),
            ('feedback', self.gf('django.db.models.fields.IntegerField')(max_length=1)),
            ('previous_product_comments', self.gf('django.db.models.fields.IntegerField')(max_length=1)),
            ('estimated_audience', self.gf('django.db.models.fields.IntegerField')()),
            ('relevant_audience', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('update_rate', self.gf('django.db.models.fields.IntegerField')(max_length=1)),
            ('remarks', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('buzz', ['Mention'])

        # Adding model 'Report'
        db.create_table('buzz_report', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('creation_user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('creation_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('report_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['buzz.ReportType'])),
        ))
        db.send_create_signal('buzz', ['Report'])


    def backwards(self, orm):
        
        # Deleting model 'UserProfile'
        db.delete_table('buzz_userprofile')

        # Deleting model 'Product'
        db.delete_table('buzz_product')

        # Deleting model 'ReportType'
        db.delete_table('buzz_reporttype')

        # Deleting model 'Country'
        db.delete_table('buzz_country')

        # Deleting model 'File'
        db.delete_table('buzz_file')

        # Deleting model 'Source'
        db.delete_table('buzz_source')

        # Deleting model 'MentionType'
        db.delete_table('buzz_mentiontype')

        # Deleting model 'AuthorExpertise'
        db.delete_table('buzz_authorexpertise')

        # Deleting model 'Mention'
        db.delete_table('buzz_mention')

        # Deleting model 'Report'
        db.delete_table('buzz_report')


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
            'creation_date': ('django.db.models.fields.DateTimeField', [], {}),
            'creation_user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
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
            'creation_date': ('django.db.models.fields.DateTimeField', [], {}),
            'creation_user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'})
        },
        'buzz.mention': {
            'Meta': {'object_name': 'Mention'},
            'author_expertise': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['buzz.AuthorExpertise']"}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {}),
            'creation_user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'creator'", 'to': "orm['auth.User']"}),
            'estimated_audience': ('django.db.models.fields.IntegerField', [], {}),
            'feedback': ('django.db.models.fields.IntegerField', [], {'max_length': '1'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_update_date': ('django.db.models.fields.DateTimeField', [], {}),
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
            'creation_date': ('django.db.models.fields.DateTimeField', [], {}),
            'creation_user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'})
        },
        'buzz.product': {
            'Meta': {'object_name': 'Product'},
            'creation_date': ('django.db.models.fields.DateTimeField', [], {}),
            'creation_user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'})
        },
        'buzz.report': {
            'Meta': {'object_name': 'Report'},
            'creation_date': ('django.db.models.fields.DateTimeField', [], {}),
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
            'creation_date': ('django.db.models.fields.DateTimeField', [], {}),
            'creation_user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
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
