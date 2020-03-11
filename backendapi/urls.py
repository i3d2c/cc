from django.urls import include, path
from backendapi.models import Project, Folder
from rest_framework.response import Response
from django.http import Http404

from rest_framework import routers, serializers, viewsets, permissions, status

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
    queryset = Project.objects.filter(active=True)
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            instance.active = False
            instance.save()
        except Http404:
            pass
        return Response(status=status.HTTP_204_NO_CONTENT)


class FolderViewSet(viewsets.ModelViewSet):
    queryset = Folder.objects.filter(active=True)
    serializer_class = FolderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            instance.active = False
            instance.save()
        except Http404:
            pass
        return Response(status=status.HTTP_204_NO_CONTENT)


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
