from rest_framework.throttling import UserRateThrottle

class BasicUserRateThrottle(UserRateThrottle):
    scope = "basic"

