from enum import Enum

class RentEnum(Enum):
    AVAILABLE = "available"
    ON_RENT = "on rent"
    MAINTENANCE = "maintenance"
    RETURNED = "returned"
    NOT_YET = "not yet"
    USER_ID_PREFIX = "USR"
    CAR_ID_PREFIX = "CAR"
    CUSTOMER_ID_PREFIX = "CST"
    RENT_ID_PREFIX = "RNT"