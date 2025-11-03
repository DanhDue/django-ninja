from typing import List

from django.shortcuts import get_object_or_404
from ninja import Router

import helpers

from .models import WaitlistEntry
from .schemas import (
    WaitlistEntryCreationSchema,
    WaitlistEntryDetailSchema,
    WaitlistEntryListSchema,
)

router = Router()


def allow_annon(request):
    if not request.user.is_authenticated:
        return True


@router.get(
    "",
    response=List[WaitlistEntryListSchema],
    auth=helpers.api_auth_user_required,
)
def list_waitlist_entries(request):
    # Logic to retrieve waitlist entries from the database
    qs = WaitlistEntry.objects.filter(user=request.user)
    return qs


@router.post(
    "",
    response=WaitlistEntryDetailSchema,
    auth=helpers.api_auth_user_or_annon,
)
def create_waitlist_entry(request, data: WaitlistEntryCreationSchema):
    obj = WaitlistEntry(**data.dict())
    print(request.user)
    if request.user.is_authenticated:
        obj.user = request.user
    obj.save()
    return obj


@router.get(
    "/{id}",
    response=WaitlistEntryListSchema,
    auth=helpers.api_auth_user_required,
)
def list_waitlist_entry(request, id: int):
    # Logic to retrieve a specific waitlist entry from the database
    obj = get_object_or_404(
        WaitlistEntry,
        id=id,
        user=request.user,
    )
    return obj
