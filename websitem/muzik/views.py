# -*- coding: utf-8 -*-
from django.http import Http404
from .models import Albumler, Sarkilar
from django.shortcuts import render, get_object_or_404

def ana_sayfa(request):
	tum_albumler = Albumler.objects.all() 
	context = {	'tum_albumler': tum_albumler,}
	return render(request, 'muzik/index.html', context)
	
	
	
def detay(request, album_id):
	# album = Albumler.objects.get(pk = album_id)
	album = get_object_or_404(Albumler, pk= album_id)
	return render(request, 'muzik/detay.html', {'album': album})
	

	
def favori(request, album_id):
	album = get_object_or_404(Albumler, pk=album_id)
	try:
		secilen_sarki = album.sarkilar_set.get(pk=request.POST['sarki'])
	except (KeyError, Sarkilar.DoesNotExist):
		return render(request, 'muzik/detay.html', {
		'album':album,
		'hata_mesaji':'Geçerli bir şarkı seçmediniz!',
		})
	else:
		if secilen_sarki.favori_mi:
			secilen_sarki.favori_mi=False
		else:
			secilen_sarki.favori_mi=True
		secilen_sarki.save()
		return render(request, 'muzik/detay.html', {'album': album})