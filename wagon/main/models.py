from django.db import models

class Table(models.Model):
    
    def __str__(self):
        return self
    
class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    first_name = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class CbResults(models.Model):
    total = models.TextField(blank=True, null=True)  # This field type is a guess.
    pred_month = models.TextField(blank=True, null=True)  # This field type is a guess.
    pred_day = models.TextField(blank=True, null=True)  # This field type is a guess.
    
    def __str__(self):
        return self.total

    class Meta:
        db_table = 'cb_results'


class DjangoAdminLog(models.Model):
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class GbResults(models.Model):
    total = models.TextField(blank=True, null=True)  # This field type is a guess.
    pred_month = models.TextField(blank=True, null=True)  # This field type is a guess.
    pred_day = models.TextField(blank=True, null=True)  # This field type is a guess.
    
    def __str__(self):
        return self.total

    class Meta:
        managed = False
        db_table = 'gb_results'


class KnnResults(models.Model):
    total = models.TextField(blank=True, null=True)  # This field type is a guess.
    pred_month = models.TextField(blank=True, null=True)  # This field type is a guess.
    pred_day = models.TextField(blank=True, null=True)  # This field type is a guess.
    
    def __str__(self):
        return self.total

    class Meta:
        managed = False
        db_table = 'knn_results'


class LrResults(models.Model):
    total = models.TextField(blank=True, null=True)  # This field type is a guess.
    pred_month = models.TextField(blank=True, null=True)  # This field type is a guess.
    pred_day = models.TextField(blank=True, null=True)  # This field type is a guess.
    
    def __str__(self):
        return self.total

    class Meta:
        managed = False
        db_table = 'lr_results'


class MainTable(models.Model):

    class Meta:
        managed = False
        db_table = 'main_table'


class PredTable(models.Model):
    wagnum = models.IntegerField(blank=True, null=True)
    month = models.TextField(blank=True, null=True)
    target_month = models.IntegerField(blank=True, null=True)
    target_day = models.IntegerField(blank=True, null=True)
    
    

    class Meta:
        managed = False
        db_table = 'pred_table'


class TtlResults(models.Model):
    total = models.TextField(blank=True, null=True)  # This field type is a guess.
    pred_month = models.TextField(blank=True, null=True)  # This field type is a guess.
    pred_day = models.TextField(blank=True, null=True)  # This field type is a guess.
    
    def __str__(self):
        return self.total

    class Meta:
        managed = False
        db_table = 'ttl_results'
