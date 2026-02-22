import pytest
from unittest.mock import MagicMock
from multi_region_scanner import check_public_acl

def test_public_acl():
    acl = {'Grants': [{'Grantee': {'URI': 'http://acs.amazonaws.com/groups/global/AllUsers'}}]}
    assert check_public_acl(acl) == True
