from typing import List

from django.shortcuts import get_object_or_404
from ninja import Router

import helpers
import json

from .forms import WaitlistEntryCreationForm
from .models import WaitlistEntry
from .schemas import (
    WaitlistEntryCreationSchema,
    WaitlistEntryDetailSchema,
    WaitlistEntryListSchema,
    ErrorWaitlistEntryCreationSchema,
)

router = Router()


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
    response={
        200: WaitlistEntryDetailSchema,
        400: ErrorWaitlistEntryCreationSchema,
    },
    auth=helpers.api_auth_user_or_anon,
)
def create_waitlist_entry(request, data: WaitlistEntryCreationSchema):
    form = WaitlistEntryCreationForm(data.dict())
    if not form.is_valid():
        # cleaned_data = form.cleaned_data
        # obj = WaitlistEntry(**cleaned_data.dict())
        form_errors = json.loads(form.errors.as_json())
        return 400, form_errors
    obj = form.save(commit=False)
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
