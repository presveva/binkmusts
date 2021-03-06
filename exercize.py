"""Main assignment module."""
import csv

import utils


def get_must_dict():
    """Read the csv and return the Orderdict."""
    musts_file = open("Mobile Phone Masts.csv", "r")
    must_dict = csv.DictReader(musts_file)
    return must_dict


def first_five_lowest_current_rent():
    """Produce a list sorted by Current Rent in ascending order and return the fisrt five."""
    musts = get_must_dict()
    sorted_musts = sorted(list(musts), key=lambda x: float(x["Current Rent"]))
    return sorted_musts[:5]


def twenty_five_lease():
    """Produce a list of musts  with Lease Years = 25 years and return them."""
    musts = get_must_dict()
    musts = [must for must in musts if int(must["Lease Years"]) == 25]
    return musts


def total_rent(musts):
    """Sum up the Current Rent of the given musts."""
    total_rent = sum([float(must["Current Rent"]) for must in musts])
    return total_rent


def tenants():
    """Create a dictionary containing tenant name and related count of masts."""
    must_dict = get_must_dict()
    final = dict()
    for must in must_dict:
        name = utils.clean_tenant_name(must["Tenant Name"])
        final[name] = final.setdefault(name, 0) + 1
    return final


def list_rental_by_lease_date():
    """List rental by lease date and filter by given dates."""
    must_dict = get_must_dict()
    final = list()
    start, end = utils.str2date("1 Jun 1999"), utils.str2date("31 Aug 2007")
    for must in must_dict:
        lease_date = utils.str2date(must["Lease Start Date"])
        if start < lease_date < end:
            final.append(must)
    return final
