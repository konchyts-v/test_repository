from .util import get_groups
from django.conf import settings

def groups_processor(request):
	return {'GROUPS': get_groups(request)}