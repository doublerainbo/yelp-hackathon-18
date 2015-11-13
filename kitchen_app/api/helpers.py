import json
import subprocess
import re
from django.core import serializers
from django.http import HttpResponse
from kitchen_app.models import Request as ItemRequest
from kitchen_app.models import ItemLocation
from kitchen_app.models import Employee
from kitchen_app.models import Item
desk_regex = re.compile(r'Desk: \d+\-\d+')

def find_user_location(user):
	# use finger to locate user
	cmd = ['finger', user]
	proc = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	output = proc.communicate()[0]  # grab only the stdout
	# run a regex on it, if it says Desk: ##-### then its a desk, if it doesn't
	# then their seat is undocumented
	result = desk_regex.findall(output)
	if len(result) > 0:
		return result[0]
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

def populate_database():
	# clear out the db before starting
	ItemRequest.objects.all().delete()
	ItemLocation.objects.all().delete()
	Item.objects.all().delete()
	Employee.objects.all().delete()

	users = [('Zhao', 'Bo', 'bozhao'),
			('Pino', 'Daniel', 'dapino'),
			('Choudhari', 'Ajay', 'ajayc'),
			('Chan', 'Desmond', 'deschan'),
			]

	for user in users:
		e = Employee(last_name=user[0], first_name=user[1], username=user[2])
		e.save()

	snacks = ['Oatmeal', 
				'Other Oatmeal', 
				'Waffles',
				'Welchs',
				'Jerky',
				'Corn',
				'Larabars',
				'Coconut Water',
				'Ito En green tea']

	for snack in snacks:
		s = Item(name=snack)
		s.save()

	all_items = Item.objects.all()

	for x in xrange(2, 14):
		for item in all_items:
			i_loc = ItemLocation(floor=x, item=item)
			i_loc.save()


	Item(name="Sun Chips").save()
	Item(name="Mocha").save()
	# add some unique ones on 8
	i_loc = ItemLocation(floor=8, item=Item.objects.get(name="Sun Chips"))
	i_loc.save()
	i_loc = ItemLocation(floor=8, item=Item.objects.get(name="Mocha"))
	i_loc.save()