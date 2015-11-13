import json

from datetime import datetime
from django.core import serializers
from django.http import HttpResponse
from django.http import HttpResponseNotAllowed

from kitchen_app.models import Item
from kitchen_app.models import Request as ItemRequest
from kitchen_app.api.helpers import find_user_location


ok_resp = json.dumps({'ok' : 'ok'})
bad_resp = json.dumps({'ok' : 'no'})
forbidden = 'method forbidden'

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
		new_item = ItemRequest(
			requester=request.POST['name'],
			request_time=str(datetime.now()),
			item=request.POST['item_id'],
			employee_location=user_location,
			status=0)
		# store it into the database
		new_item.save()
		return ok_resp
	return HttpResponseNotAllowed(['POST'])


def cancel_request(request):
	request_id = request.POST['request_id']
	item_request = ItemRequest.objects.filter(id=request_id)
	if item_request is not None:
		item_request.delete()
		return ok_resp
	return bad_resp


def ack_request(request):
	request_id = request.POST['request_id']
	if 'delivery_person' in request.POST:
		delivery_person = request.POST['delivery_person']
	pass


def fulfill_request(request):
	pass


def current_requests(request):
	pass


def available_items(request):
	pass


def clear_database(request):
	pass


def add_item(request):
	pass