from django.db import models
 

def area_image_directory_path(instance, filename): 
    return 'area_{0}/{1}'.format(instance.name, filename)

class AreaImage(models.Model):
    image_name = models.CharField(max_length=255,blank=True,null=True)
    image = models.ImageField(upload_to=area_image_directory_path)
    pinned_point_loc_x = models.DecimalField(blank=True,null=True,max_digits=10,decimal_places=6)
    pinned_point_loc_y = models.DecimalField(blank=True,null=True,max_digits=10,decimal_places=6)

    image_min_x = models.DecimalField(blank=True,null=True,max_digits=10,decimal_places=6)
    image_max_x = models.DecimalField(blank=True,null=True,max_digits=10,decimal_places=6)
    image_min_y = models.DecimalField(blank=True,null=True,max_digits=10,decimal_places=6)
    image_max_y = models.DecimalField(blank=True,null=True,max_digits=10,decimal_places=6)

    created_at = models.DateTimeField(auto_created=True,auto_now_add=True)
    updated_at = models.DateTimeField(auto_created=True,auto_now=True)


class Area(models.Model):
    name = models.CharField(max_length=255,blank=True,null=True)
    title = models.CharField(max_length=255,blank=True,null=True)
    notes = models.CharField(max_length=255,blank=True,null=True)
    link = models.CharField(max_length=255,blank=True,null=True)

    related_image =models.OneToOneField(AreaImage,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_created=True,auto_now_add=True)
    updated_at = models.DateTimeField(auto_created=True,auto_now=True)


class AskedQuestions(models.Model):
    question = models.CharField(max_length=255,blank=True,null=True)
    answer = models.CharField(max_length=255,blank=True,null=True)
    related_area = models.ForeignKey(to=Area,related_name='related_area',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_created=True,auto_now_add=True)
    updated_at = models.DateTimeField(auto_created=True,auto_now=True)
