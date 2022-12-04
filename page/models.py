from django.db import models

class cars(models.Model):
    name = models.CharField(max_length = 50)
    
    BRAND_CHOICES=(
        ('mercedez','MERCEDEZ'),
        ('honda','HONDA'),
        ('toyota','TOYOTA'),
        ('bmw','BMW'),
        ('ferari','FERARI'),
        ('ford','FORD'),
        ('range rover','RANGE ROVER'),
        ('bentley','BENTLEY'),
        ('maclauren','MACLAUREN')
        
    )
    brand = models.CharField(max_length = 50, choices = BRAND_CHOICES)
    MODEL_CHOICES= (
        ('1998','1998'),
        ('1999','1999'),
        ('2000','2000'),
        ('2001','2001'),
        ('2002','2002'),
        ('2003','2003'),
        ('2004','2004'),
        ('2005','2005'),
        ('2006','2006'),
        ('2007','2007'),
        ('2008','2008'),
        ('2009','2009'),
        ('2010','2010'),
        ('2011','2011'),
        ('2012','2012'),
        ('2013','2013'),
        ('2014','2014'),
        ('2015','2015'),
        ('2016','2016'),
        ('2017','2017'),
        ('2018','2018'),
        ('2019','2019'),
        ('2020','2020'),
        ('2021','2021'),
        ('2022','2022'),
        
    )
    
    year = models.CharField(max_length = 4, choices= MODEL_CHOICES)
    STATUS_CHOICES = (
        ('new','New'),
        ('nused','Nigerian Used'),
        ('fused','Foreign Used'),
    )
    status = models.CharField(max_length = 20, choices= STATUS_CHOICES)
    COLOR_CHOICES=(
        ('white','WHITE'),
        ('black','BLACK'),
        ('yellow','YELLOW'),
        ('pink','PINK'),
        ('brown','BROWN'),
        ('red','RED'),
        ('green','GREEN'),
        ('blue','BLUE'),
        ('peach','PEACH'),
    )
    colour = models.CharField(max_length = 8, choices = COLOR_CHOICES)
    price = models.CharField(max_length = 50)
    number_available = models.PositiveIntegerField()
    comments = models.TextField(max_length=300)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.name
    