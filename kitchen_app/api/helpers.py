
from kitchen_app.models import Request as ItemRequest

def find_user_location(user):
	return "????"


def create_item(username, datetime, item_id, employee_location):
	return ItemRequest(
		requester=username,
		request_time=datetime,
		item=item_id,
		employee_location=employee_location,
		status=0)

def delete_item(request_id):
	'''
	Deletes an item from the db, returns True if it found the
	item to delete and deleted it. If it didn't then it'll 
	return false 
	'''
	item_request = ItemRequest.objects.filter(id=request_id)
	if item_request is not None:
		item_request.delete()
		return True
	return False