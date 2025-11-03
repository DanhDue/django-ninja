from typing import List, Any
from datetime import datetime
from ninja import Schema
from pydantic import EmailStr


class WaitlistEntryCreationSchema(Schema):
    # POST(Create) -> Data
    # WaitlistEntryIN
    email: EmailStr


class ErrorWaitlistEntryCreationSchema(Schema):
    # POST(Create) -> Data
    # WaitlistEntryIN
    email: List[Any]
    # non_field_errors: List[dict] = []


class WaitlistEntryListSchema(Schema):
    # GET(Retrieve) -> Data
    # WaitlistEntryOut
    id: int
    email: EmailStr
    created_at: datetime
    updated_at: datetime


class WaitlistEntryDetailSchema(Schema):
    # GET(Retrieve) -> Data
    # WaitlistEntryOut
    email: EmailStr
    created_at: datetime
    updated_at: datetime
