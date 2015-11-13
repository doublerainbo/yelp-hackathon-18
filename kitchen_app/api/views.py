import json

from datetime import datetime
from django.core import serializers
from django.http import HttpResponse
from django.http import HttpResponseNotAllowed

from kitchen_app.models import Item
from kitchen_app.models import Request as ItemRequest
from kitchen_app.api.helpers import find_user_location
from kitchen_app.api.helpers import create_item
from kitchen_app.api.helpers import delete_item


ok_resp = json.dumps({'ok' : 'ok'})
bad_resp = json.dumps({'ok' : 'no'})
forbidden = 'method forbidden'

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
	request_id = request.POST['request_id']
	if delete_item(request_id):
		return ok_resp
	return bad_resp


def ack_request(request):
	request_id = request.POST['request_id']
	delivery_person = ''
	if 'delivery_person' in request.POST:
		delivery_person = request.POST['delivery_person']
	# let them know somehow
	return ok_resp


def fulfill_request(request):
	request_id = request.POST['request_id']
	delivery_person = ''
	return_url = YELP_LOVE_URL
	if 'delivery_person' in request.POST:
		delivery_person = request.POST['delivery_person']
		return_url += '?recipient=%s' % delivery_person
	return json.dumps({'url': return_url})


def current_requests(request):
	name = request.POST['name']
	requests = ItemRequest.objects.filter(requester=name)
	return serializers.serialize("json", requests)


def kitchen_requests(request):
	# find the snacks on the floor
	pass


def available_items(request):
	pass


def clear_database(request):
	pass


def add_item(request):
	pass