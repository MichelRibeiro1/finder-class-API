from tastypie.resources import ModelResource
from tastypie.constants import ALL

from apiClass.models import Turmas


class ClassResource(ModelResource):
    class Meta:
        queryset = Turmas.objects.all()
        resource_name = 'turmas'
        #filtering = {'title': ALL}
        excludes = ['lixo']