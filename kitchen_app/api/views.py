import json

from datetime import datetime
from django.core import serializers
from django.http import HttpResponse
from django.http import HttpResponseNotAllowed

from kitchen_app.models.item import Item
from kitchen_app.models.request import Request as ItemRequest
from kitchen_app.models.item_location import ItemLocation
from kitchen_app.api.helpers import find_user_location
from kitchen_app.api.helpers import create_item
from kitchen_app.api.helpers import delete_item


ok_resp = json.dumps({'ok' : 'ok'})
bad_resp = json.dumps({'ok' : 'no'})

YELP_LOVE_URL = 'https://yelplove.appspot.com/'


def index(request):
    return HttpResponse("Main API page")


def create_request(request):
	'''
	add a new item request to the Request table
	'''
	if request.method == 'POST':
		user = request.POST['name']
		# check to see if requester has specified an override location
		if 'user_location' in request.POST:
			user_location = request.POST['user_location']
		else:
			# no location specified, find out where the user sits
			user_location = find_user_location(user)
		# create the new item	
		
		new_item = create_item(
			user,
			str(datetime.now()),
			request.POST['item_id'],
			user_location)
		# store it into the database
		new_item.save()
		return ok_resp
	return HttpResponseNotAllowed(['POST'])


def cancel_request(request):
	if request.method == 'POST':
		request_id = request.POST['request_id']
		if delete_item(request_id):
			return ok_resp
		return bad_resp
	return HttpResponseNotAllowed(['POST'])


def ack_request(request):
	if request.method == 'POST':
		request_id = request.POST['request_id']
		delivery_person = ''
		if 'delivery_person' in request.POST:
			delivery_person = request.POST['delivery_person']
		# let them know somehow
		return ok_resp
	return HttpResponseNotAllowed(['POST'])


def fulfill_request(request):
	if request.method == 'POST':
		request_id = request.POST['request_id']
		if not delete_item(request_id):
			return bad_resp
		return_url = YELP_LOVE_URL
		if 'delivery_person' in request.POST:
			delivery_person = request.POST['delivery_person']
			return_url += '?recipient=%s' % delivery_person
		return json.dumps({'url': return_url})
	return HttpResponseNotAllowed(['POST'])


def current_requests(request):
	if request.method == 'POST':
		name = request.POST['name']
		requests = ItemRequest.objects.filter(requester=name)
		return serializers.serialize('json', requests)
	return HttpResponseNotAllowed(['POST'])


def kitchen_requests(request):
	if request.method == 'POST':
		# find the snacks on the floor
		floor = request.POST['floor']
		# apparently django does joins internally?? O.o 
		requests = ItemRequest.objects.filter(item__floor=floor)
		return serializers.serialize('json', request)
	return HttpResponseNotAllowed(['POST'])


def available_items(request):
	if request.method == 'POST':
		floor = request.POST['floor']
		items = ItemLocation.objects.filter(floor=floor)
		return serializers.serializers('json', items)
	return HttpResponseNotAllowed(['POST'])


def clear_database(request):
	if request.method == 'POST':
		ItemRequest.objects.all().delete()
		return ok_resp
	return HttpResponseNotAllowed(['POST'])


def add_item(request):
	if request.method == 'POST':
		floor = request.POST['floor']
		item_id = request.POST['item_id']
		# see if this item already exists
		item_location = ItemLocation.objects.filter(floor=floor).filter(item=item_id)
		if not item_location:
			item_location = ItemLocation(floor=floor, item=item_id)
			item_location.save()
			return ok_resp
		else:
			return bad_resp
	return HttpResponseNotAllowed(['POST'])


def delete_item(request):
	if request.method == 'POST':
		floor = request.POST['floor']
		item_id = request.POST['item_id']
		# see if this item actually exists
		item_location = ItemLocation.objects.filter(floor=floor).filter(item=item_id)
		if item_location:
			item_location = ItemLocation(floor=floor, item=item_id)
			item_location.save()
			return ok_resp
		else:
			return bad_resp
	return HttpResponseNotAllowed(['POST'])


def bulk_edit(request):
	if request.method == 'POST':
		floor = request.POST['floor']
		available_items = request.POST['available_items']
		# find the diffs
		# first delete all that isn't in this new set
		to_delete = ItemLocation.objects
			.filter(floor=floor)
			.exclude(item__in=available_items)
		to_delete.delete()
		# now find out which isn't in there
		# grab all the ones already on the floor
		current_items = ItemLocation.objects.filter(floor=floor)
		current_ids = []
		for current_item in current_items:
			current_ids.append(current_item.item)
		# insert the new items
		for available_item in available_items:
			if available_item not in current_ids:
				ItemLocation(floor=floor, item=available_item).save()

		return ok_resp
		
	return HttpResponseNotAllowed(['POST'])
