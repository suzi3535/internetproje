from django.db import models

class Albumler(models.Model):
	sanatci = models.CharField(max_length=250)
	album_adi = models.CharField(max_length=250)
	album_turu = models.CharField(max_length=100)
	album_kapagi = models.CharField(max_length=1000)
	
	def __str__(self):
	    return self.album_adi + '-' + self.sanatci
	

	
	
	
class Sarkilar(models.Model):
	album = models.ForeignKey(Albumler, on_delete=models.CASCADE)
	sarki_adi = models.CharField(max_length=250)
	dosya_turu = models.CharField(max_length=10)
	favori_mi = models.BooleanField(default=False)
	
	
	
	
	
	
	
	
	
	

