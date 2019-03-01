from  django.db  import  models
from  django.contrib.auth.models  import  User
from  django.core.validators  import  MinLengthValidator,MaxValueValidator, MinValueValidator

class Chef (models.Model):
    name = models.CharField(
        max_length= 200 ,
        validators=[MinLengthValidator( 2 ,  "Chef name must be greater than 1 character" )]
    )

    def __str__ (self):
        return  self.name

class Recipe (models.Model):
    name = models.CharField(
        max_length= 200 ,
        validators=[MinLengthValidator( 2 ,  "Recipe Name must begreater than 1 character" )]
    )
    rating = models.IntegerField( validators=[MinValueValidator( 0 ),MaxValueValidator( 5 )])

    ingredients = models.CharField(max_length= 300 )
    description = models.TextField(max_length= 3000 )
    chef = models.ForeignKey( 'Chef' , on_delete=models.CASCADE,null= False )


def __str__ (self):
    return  self.name
# Create your models here.
