from django.db import models
# from users.models import Users
# Create your models here.


class Products(models.Model):
    image = models.ImageField(upload_to='all/')
    video = models.FileField(upload_to='all/')
    name = models.CharField(max_length=200)
    title = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'products'

    def __str__(self):
        return f"ID: {self.pk} | Name: {self.name}"


# class Comments(models.Model):
#     user = models.ForeignKey(Users, on_delete=models.CASCADE)
#     product = models.ForeignKey(Products, on_delete=models.CASCADE)
#     like = models.IntegerField(max_length=1)
#
#     class Meta:
#         db_table = 'comments'
#
#     def __str__(self):
#         return f"ID: {self.pk} | User: {self.user.username}"


# class Saved(models.Model):
#     user = models.ForeignKey(Users, on_delete=models.CASCADE)
#     product = models.ForeignKey(Products, on_delete=models.CASCADE)
#
#     class Meta:
#         db_table = 'saved'
#
#     def __str__(self):
#         return f"ID: {self.pk} | User: {self.user.username}"