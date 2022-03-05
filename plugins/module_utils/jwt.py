from __future__ import absolute_import, division, print_function
__metaclass__ = type

try:
    import jwt
    jwt_not_found = False
except ImportError:
    jwt_not_found = True

try:
    from datetime import datetime, timezone, timedelta
except ImportError:
    pass

from os import environ, getenv
from ansible.errors import AnsibleFilterError, AnsibleFilterTypeError
from ansible.module_utils.six import string_types, integer_types


def jwt_token(payload, expiration_time=30, algorithms="HS256", key_env_name="UUID_TOKEN_SECRET"):
    '''Generate a JWT token with a payload'''
    if jwt_not_found:
        raise AnsibleFilterError("pyjwt module not installed")

    if not isinstance(payload, dict):
        raise AnsibleFilterTypeError("payload passed is required to be a dict, instead we got: %s" % type(payload))

    if not isinstance(algorithms, string_types):
        raise AnsibleFilterTypeError("algorithms passed is required to be a string, instead we got: %s" % type(algorithms))

    if not isinstance(expiration_time, integer_types):
        raise AnsibleFilterTypeError("expiration_time passed is required to be a int, instead we got: %s" % type(expiration_time))

    if key_env_name not in environ:
        raise AnsibleFilterError("%s environment variable not found" % key_env_name)

    key = getenv(key_env_name)
    exp = datetime.now(tz=timezone.utc) + timedelta(seconds=expiration_time)

    if "exp" not in payload:
        payload["exp"] = exp

    token = jwt.encode(payload, key, algorithms)
    return token
