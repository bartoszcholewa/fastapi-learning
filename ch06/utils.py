from datetime import date, datetime

from bson import ObjectId
from constants import DATETIME_FORMAT


def date_to_datetime(value: date, datetime_format=DATETIME_FORMAT) -> datetime:
    return datetime.strptime(value.strftime(datetime_format), datetime_format)


def string_to_date(value: str, string_format=DATETIME_FORMAT) -> date:
    return datetime.strptime(value, string_format).date()


def json_serialize_date(obj):
    if isinstance(obj, (date, datetime)):
        return obj.strftime(DATETIME_FORMAT)
    raise TypeError(f"The type {type(obj)} is not date serializable")


def json_serialize_oid(obj):
    if isinstance(obj, ObjectId):
        return str(obj)
    elif isinstance(obj, date):
        return obj.isoformat()
    raise TypeError("The type %s not serializable." % type(obj))


def json_serial(obj):
    if isinstance(obj, (datetime, date)):
        return obj.strftime(DATETIME_FORMAT)
    raise TypeError("The type %s not serializable." % type(obj))
