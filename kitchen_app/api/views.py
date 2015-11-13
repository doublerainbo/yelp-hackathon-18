import datetime
import json

from django.core import serializers
from django.http import HttpResponse

from kitchen_app.src.models import Item
from kitchen_app.src.models import Request as ItemRequest
from kitchen_app.src.api.helpers import find_user_location


ok_resp = json.dumps({'ok' : 'ok'})
bad_resp = json.dumps({'ok' : 'no'})

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
			request_time=datetime.datetime.now(),
			item=request.POST['item_id'],
			location=user_location,
			status=0)
		# store it into the database
		new_item.save()


def cancel_request(request):
	pass


def ack_request(request):
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