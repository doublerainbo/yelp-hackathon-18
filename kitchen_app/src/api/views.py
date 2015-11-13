from django.core import serializers
from django.http import HttpResponse

def index(request):
    return HttpResponse("Main API page")


def create_request(request):
	pass


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