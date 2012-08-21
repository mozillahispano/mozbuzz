from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.db.utils import DatabaseError

from buzz.helpers import slugifyUniquely


#Choices
PREVIOUS_PRODUCT_COMMENTS = (
        (0,'No'),
        (1,'Yes'),
        (2,'Unknown'),
    )

UPDATE_RATE = (
        (00, 'Never'),
        (10, 'Yearly'),
        (20, 'Monthly'),
        (25, 'Weekly'),
        (30, 'Daily'),
        (40, 'Hourly'),
        (50, 'Unknown'),
    )

FEEDBACK_TYPES = (
        (00, 'Very bad'),
        (10, 'Bad'),
        (20, 'Neutral'),
        (30, 'Good'),
        (40, 'Very good'),
    )

#user profile related
class UserProfile(models.Model):
    user = models.OneToOneField(User)

    def __str__(self):
        return "%s's profile" % self.user

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        try:
            UserProfile.objects.get_or_create(user=instance)
        except DatabaseError:
            #skipping pre-south error
            pass

post_save.connect(create_user_profile, sender=User)


#manager for soft deletion
class EnabledManager(models.Manager):
    def get_query_set(self):
        query_set = super(self.__class__, self).get_query_set()
        return query_set.filter(disabled=False)


class SoftDeletableModel(models.Model):
    objects = models.Manager()
    enabled = EnabledManager()

    class Meta:
        abstract = True


#sluggifier
class SluggedModel(SoftDeletableModel):
    def save(self):
        if not self.id:
            self.slug = slugifyUniquely(self.name, self.__class__)

        models.Model.save(self)

    class Meta:
        abstract = True


#models
class Product(SluggedModel):
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=100)
    creation_date = models.DateTimeField(auto_now_add=True)
    creation_user = models.ForeignKey(User, null=True, blank=True)
    disabled = models.BooleanField(default=False)

    def save_model(self, request, obj, form, change):
        obj.creation_user = request.user
        obj.save()

    def __unicode__(self):
        return self.name


class ReportType(SluggedModel):
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name


class Country(SluggedModel):
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

    class Meta():
        verbose_name_plural = "Countries"


class File(SluggedModel):
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    creation_date = models.DateTimeField(auto_now_add=True)
    creation_user = models.ForeignKey(User, null=True, blank=True)
    disabled = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name


class Source(SluggedModel):
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=100)
    creation_date = models.DateTimeField(auto_now_add=True)
    creation_user = models.ForeignKey(User, null=True, blank=True)
    disabled = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name


class MentionType(SluggedModel):
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=100)
    creation_date = models.DateTimeField(auto_now_add=True)
    creation_user = models.ForeignKey(User, null=True, blank=True)
    disabled = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name


class AuthorExpertise(SoftDeletableModel):
    name = models.CharField(max_length=100)
    creation_date = models.DateTimeField(auto_now_add=True)
    creation_user = models.ForeignKey(User, null=True, blank=True)
    disabled = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name


class Mention(SoftDeletableModel):
    creation_user = models.ForeignKey(User, related_name="creator", null=True,
                                      blank=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    last_update_user = models.ForeignKey(User, related_name="updater")
    last_update_date = models.DateTimeField(auto_now=True)
    disabled = models.BooleanField(default=False)

    link = models.URLField(null=True, blank=True)
    text = models.TextField()
    source_name = models.TextField()
    origin = models.ForeignKey(Source)
    type = models.ForeignKey(MentionType)
    author_expertise = models.ForeignKey(AuthorExpertise)
    country = models.ForeignKey(Country, on_delete=models.PROTECT, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.PROTECT, null=True, blank=True)
    feedback = models.IntegerField(max_length=1, choices=FEEDBACK_TYPES)
    previous_product_comments = models.IntegerField(max_length=1,
        choices=PREVIOUS_PRODUCT_COMMENTS)
    estimated_audience = models.IntegerField()
    relevant_audience = models.BooleanField()
    update_rate = models.IntegerField(max_length=1, choices=UPDATE_RATE)
    remarks = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return "%s @ %s" %(self.type, self.source_name)

    def __obj__(self):
        def getval(att):
            val = getattr(self,att)
            if isinstance(val,models.Model):
                return val.pk
            return val

        return dict([(k,getval(k)) for k in ("origin","type",
            "author_expertise","country","product","feedback",
            "previous_product_comments","estimated_audience",
            "relevant_audience","update_rate")])

    def followups(self):
        return FollowUp.enabled.filter(mention=self)


class FollowUpStatus(SluggedModel):
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

    class Meta():
        verbose_name_plural = "Follow ups statuses"


class FollowUp(SoftDeletableModel):
    creation_date = models.DateTimeField(auto_now_add=True)
    creation_user = models.ForeignKey(User, null=True, blank=True)
    status = models.ForeignKey(FollowUpStatus)
    disabled = models.BooleanField(default=False)
    mention = models.ForeignKey(Mention)
    remarks = models.TextField()

    def __unicode__(self):
        return self.status.name


class Report(SoftDeletableModel):
    name = models.CharField(max_length=100)
    creation_user = models.ForeignKey(User, null=True, blank=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    report_type = models.ForeignKey(ReportType)

    def __unicode__(self):
        return self.name

class RSSFeed(models.Model):
    name = models.TextField()
    url = models.URLField()
    product = models.ForeignKey(Product,related_name="feeds")
    last_updated = models.DateTimeField()

    def __unicode__(self):
        return "%s (%s)" % (self.name, self.product.name)

class RSSPost(models.Model):
    feed = models.ForeignKey(RSSFeed,related_name="posts")
    hidden = models.BooleanField(default=False)
    title = models.TextField()
    link = models.URLField(max_length=3000)
    guid = models.TextField()
    pub_date = models.DateTimeField()
    description = models.TextField()

