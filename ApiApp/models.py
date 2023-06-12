from django.db import models

# Create your models here.

class Food(models.Model):
    #類別屬性
    id = models.IntegerField(primary_key=True) #整數 主鍵(不可重複)
    p_id =models.IntegerField()
    p_name = models.CharField(max_length=60) #字串最多60字
    p_price = models.IntegerField()
    p_img_src = models.CharField(max_length=60) #字串最多60字

    def __str__(self):
        s = f'{self.id}{self.p_name}{self.p_price}{self.p_img_src}'
        return s