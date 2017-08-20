# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import base64

from django.http import JsonResponse
from front_site.models import User, Events
import requests

from new_hackaton.settings import TRUEFACE_API_KEY


def test_spoof(file_path):
    headers = {
        "x-api-key": TRUEFACE_API_KEY,
        "Content-Type": "image/jpeg",

    }

    url = "https://api.chui.ai/v1/spdetect"

    r = requests.post(url, data=open(file_path, 'rb').read(), headers=headers)

    return r.json().get('success', False)


def identify(file_path, collection_id):
    headers = {
        "x-api-key": TRUEFACE_API_KEY,
    }

    url = "https://api.chui.ai/v1/identify"

    data = {
        "img": base64.b64encode(open(file_path, 'rb').read()),
        "collection_id": collection_id
    }

    r = requests.post(url, json=data, headers=headers)

    return r.json().get('data', {}).get('key', '')


def update_collection(enroll_id, collection_id):
    headers = {
        "content-type": TRUEFACE_API_KEY,
        "x-api-key": "chui-api-key"

    }

    url = "https://api.chui.ai/v1/collection"

    data = {
        "enrollment_id": enroll_id,
        "collection_id": collection_id
    }

    r = requests.put(url, json=data, headers=headers)

    print r.json()


def get_my_event(request):
    file_path = request.POST.get("file_path", '')
    collection_id = request.POST.get("collection_id", '')

    if test_spoof(file_path):
        user_key = identify(file_path, collection_id)
        update_collection(user_key, collection_id)
        user = User.objects.filter(enroll_id=user_key).first()
        data = Events.objects.filter(users=user).order_by('-time_start').first().__dict__
    else:
        data = {
            "error": "Incorrect user"
        }

    return JsonResponse(data=data, safe=False)


def get_help(request):
    file_path = request.POST.get("file_path", '')
    collection_id = request.POST.get("collection_id", '')

    if test_spoof(file_path):
        user_key = identify(file_path, collection_id)
        update_collection(user_key, collection_id)
        user = User.objects.filter(enroll_id=user_key).first()
        event_creator = Events.objects.filter(users=user).order_by('-time_start').first().company.user
        data = event_creator.__dict__
    else:
        data = {
            "error": "Incorrect user"
        }

    return JsonResponse(data=data, safe=False)
