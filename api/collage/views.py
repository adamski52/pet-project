import os
from rest_framework.response import Response
from django.conf import settings
from rest_framework import viewsets
from random import shuffle

    
class CollageViewSet(viewsets.ViewSet):
    def list(self, request):
        content = []

        os.chdir(settings.COLLAGE_THUMBNAIL_DIRECTORY)

        num_results = 0
        for filename in os.listdir(os.getcwd()):
          if num_results >= settings.COLLAGE_MAX_RESULTS:
            break

          if not os.path.isfile(filename):
            continue

          if not os.path.exists(settings.COLLAGE_FULL_DIRECTORY + filename):
            continue

          extension = filename.split(".")[-1]
          if not extension in settings.COLLAGE_ALLOWED_TYPES:
            continue

          content.append({
            "thumbnail": settings.COLLAGE_WEB_THUMBNAIL_DIRECTORY + filename,
            "full": settings.COLLAGE_WEB_FULL_DIRECTORY + filename
          })
          num_results += 1

        #easy bake fancifier
        shuffle(content)
          
        return Response(content)