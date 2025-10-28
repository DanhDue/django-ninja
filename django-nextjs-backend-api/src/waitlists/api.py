from typing import List
from ninja import Router
from ninja_jwt.authentication import JWTAuth

from django.shortcuts import get_object_or_404

from .models import WaitlistEntry
from .schemas import WaitlistEntryListSchema

router = Router()


@router.get(
    "",
    response=List[WaitlistEntryListSchema],
    auth=JWTAuth(),
)
def list_waitlist_entries(request):
    # Logic to retrieve waitlist entries from the database
    qs = WaitlistEntry.objects.all()
    return qs


@router.get(
    "/{id}",
    response=WaitlistEntryListSchema,
    auth=JWTAuth(),
)
def list_waitlist_entry(request, id: int):
    # Logic to retrieve a specific waitlist entry from the database
    obj = get_object_or_404(WaitlistEntry, id=id)
    return obj
