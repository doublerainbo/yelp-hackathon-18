import json
from django.core import serializers
from django.http import HttpResponse
from kitchen_app.models import Request as ItemRequest
from kitchen_app.models import ItemLocation
from kitchen_app.models import Employee

def find_user_location(user):
	return "????"


def create_item(username, datetime, item_id, employee_location):
	item = ItemLocation.objects.get(id=item_id)
	employee = Employee.objects.get(username=username)
	if not item or not employee:
		return None
	return ItemRequest(
		requester=employee,
		request_time=datetime,
		item=item,
		employee_location=employee_location,
		status=0)

def delete_item(request_id):
	'''
	Deletes an item from the db, returns True if it found the
	item to delete and deleted it. If it didn't then it'll 
	return false 
	'''
	item_request = ItemRequest.objects.get(id=request_id)
	if item_request is not None:
		item_request.delete()
		return True
	return False


def create_serialized_response(to_serialize):
	# the base serializer adds extra info like primary key and stuff,
	# need to work around it only return the relevant stuff
	json_data = serializers.serialize('json', to_serialize)
	python_serialized = json.loads(json_data)
	actual_data = [d['fields'] for d in python_serialized]
	output = json.dumps(actual_data)
	return HttpResponse(output)