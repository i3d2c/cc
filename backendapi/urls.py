from django.urls import include, path
from backendapi.models import Project, Folder

from rest_framework import routers, serializers, viewsets
from rest_framework import permissions

# Serializers define the API representation.
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'name', 'content', 'infos', 'actions', 'folder']


class FolderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Folder
        fields = ['id', 'name', 'parent']
        # id, name & parent are fields used by jstree in frontend


# ViewSets define the view behavior.
class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]


class FolderViewSet(viewsets.ModelViewSet):
    queryset = Folder.objects.all()
    serializer_class = FolderSerializer
    permission_classes = [permissions.IsAuthenticated]


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'projects', ProjectViewSet)
router.register(r'folders', FolderViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls'))
]
