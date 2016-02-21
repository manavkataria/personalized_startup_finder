from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
from .models import CbObjects

import urllib2, sys
import json

def index(request):
    value = compile_user_params()
    return JsonResponse({'result': value})

def detail(request, normalized_name):
    return HttpResponse("You're looking at company %s." % normalized_name)

def results(request, normalized_name):	
    response = "You're looking at the results of company %s."
    return HttpResponse(response % normalized_name)


USERS = {
    'manav': {
        'domains':'medical, analytics, health, education',
        'location':'CA',
    }
}


def compile_user_params(username='manav'):
    """
    :param username:
    :return: json object to Frontend API call
    """
    userdata = USERS.get(username) # from frontend
    domains = userdata.get('domains').replace(',','').split() # from fronend
    location = userdata.get('location')

    return ranking(domains, location)
     #Vizualize Ranking



def ranking(domains, location):
    """
    Filter Half a million entities down to a few companies best suited for my preference
    :return:
    """
    # All Categories
    # categories = CbObjects.objects.filter(entity_type='company').values('category_code')
    # cat_set = set(cat.get('category_code') for cat in categories)

    # All Tags
    # tags_set = set()
    # tags_list_str_db = CbObjects.objects.filter(entity_type='Company').values('tag_list')
    #
    # for tag_list_str in tags_list_str_db:
    #
    #     if tag_list_str is not None:
    #         tags_csv_record = tag_list_str.get('tag_list')
    #         if tags_csv_record is not None or '':
    #             tag_record = tags_csv_record.replace(',','').split()
    #
    #     for t in tag_record:
    #         tags_set.add(t)
    #
    # print tags_set
    # Both Categories and Tags, Combined

    # companies = CbObjects.objects.filter(entity_type='company').values('name')
    # companies_set = set(companies_dict.get('name') for companies_dict in companies)
    return getGlassdoorInfo('apple')

    # for company in companies_set:
    #     rating = getGlassdoorInfo(company)


    # TODO: write into mysqldb.


def getGlassdoorInfo(company):
	url = "http://api.glassdoor.com/api/api.htm?t.p=55690&t.k=em66CFmfXYu&userip=172.23.227.50&useragent=Mozilla&format=json&v=1&action=employers&q="
	hdr = {'User-Agent': 'Mozilla/5.0'}
	finalURL = url + urllib2.quote(company)
	req_encoded = urllib2.Request(finalURL, headers=hdr)

	# print finalURL
	# req_encoded = urllib2.quote(req, safe='')
	response_json = urllib2.urlopen(req_encoded)

	employer_top = None

	if response_json.getcode() == 200:
		response = json.load(response_json).get('response')

		if response:
			employers = response.get('employers')
			if employers and len(employers) > 0:
				employer_top = employers[0]

	# id, name, website, numberOfRatings, squareLogo, overallRating
	# cultureAndValuesRating: "4.1",
	# seniorLeadershipRating: "3.5",
	# compensationAndBenefitsRating: "4.1",
	# careerOpportunitiesRating: "3.5",
	# workLifeBalanceRating: "3.3",
	# recommendToFriendRating: "0.8",

	return employer_top