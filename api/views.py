import math

from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from Accounts.models import Account
from MainApp.models import Events, EventsMembers
from rest_framework import generics, mixins
from rest_framework import permissions
from .serializers import *
from .permissions import IsAdmin


class EventsViewSet(APIView):
    permission_classes = [IsAdmin]
    permission_classes = [IsAdmin]

    @action(methods=['get'], detail=False)
    def get(self, request):
        queryset = Events.objects.all()
        token = request.META.get('HTTP_AUTHORIZATION')
        if request.GET.get('page'):
            page = int(request.GET.get('page'))
        else:
            page = 1
        if request.GET.get('archive'):
            queryset = queryset.filter(archive=True)
        else:
            queryset = queryset.filter(archive=False)
        items_for_page = 25
        offset = (page - 1) * items_for_page
        limit = items_for_page + offset
        if token:
            user = Token.objects.get(key=token.split()[1]).user
        if page > 1:
            prev = "?page=" + str(page - 1)
        else:
            prev = None
        if page * items_for_page < queryset.count():
            next = "?page=" + str(page + 1)
        else:
            next = None
        max = math.ceil(queryset.count() / items_for_page)
        print(offset, limit)
        q = queryset.order_by("-id")[offset:limit]
        serializer = EventsSerializer(q, many=True)
        return Response(
            {"results": serializer.data, "prev": prev, "next": next, "max": max, "page": page})


class ProfileViewSet(APIView):
    def get(self, request, pk=None):
        if pk is None:
            token = request.META.get('HTTP_AUTHORIZATION')
            if token:
                user = Token.objects.get(key=token.split()[1]).user
            pk = user.id
        queryset = Account.objects.get(pk=pk)
        serializer = ProfileSerializer(queryset)
        events = Events.objects.filter(volunteer__user=queryset)
        e = EventsSerializer(events, many=True)

        return Response({"user": serializer.data, "events": e.data})
class UsersViewSet(APIView):
    permission_classes = [IsAdmin]

    @action(methods=['get'], detail=False)
    def get(self,request):
        queryset = Account.objects.all().filter(is_superuser=False)
        token = request.META.get('HTTP_AUTHORIZATION')
        if request.GET.get('page'):
            page = int(request.GET.get('page'))
        else:
            page = 1
        items_for_page = 25
        offset = (page - 1) * items_for_page
        limit = items_for_page+offset
        if token:
            user = Token.objects.get(key=token.split()[1]).user
        if user.role == "head_teacher":
            queryset = queryset.filter(building_id=user.building_id)
        if page > 1:
            prev = "?page=" + str(page - 1)
        else:
            prev = None
        if page * items_for_page < queryset.count():
            next = "?page=" + str(page + 1)
        else:
            next = None
        max = math.ceil(queryset.count()/items_for_page)
        print(offset, limit)
        q = queryset.order_by("-id")[offset:limit]
        serializer = UsersSerializer(q, many=True)
        statictic = {
            "staff": queryset.filter(role="methodist").count(),
            "parents": queryset.filter(role="parent").count(),
            "students": queryset.filter(role="student").count(),
            "all": queryset.count(),

        }
        print(statictic)
        return Response({"results": serializer.data, "prev": prev, "next": next, "max": max, "page": page, "statictic": statictic})
