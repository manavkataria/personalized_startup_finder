from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
from .models import CbObjects

import urllib2, sys
import json, ipdb
import pickle

def index(request):
    value = compile_user_params(username=request.GET['user'])
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
    },
    'appy': {
        'domains':['software, web'],
        'location': 'CA',
    },
    'web': {
        'domains':'web',
        'location':'CA',
    },
    'software': {
        'domains':'software',
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

    result =  getRanking(domains, location)
    return result
     #Vizualize Ranking


def getRanking(domains, location):
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

    companies = CbObjects.objects.filter(entity_type='company').exclude(category_code=None).exclude(funding_total_usd=None).values('name')
    companies_set = set(companies_dict.get('name') for companies_dict in companies)
    # TODO: write into mysqldb.
    # companies_set = set(['IBM', 'Apple', 'Juniper Networks', 'Google', 'Microsoft', 'Intel', 'Theranos', 'Uber', 'Pintrest'])

    ranking = []
    LIMIT = 500
    MILESTONE = 0
    i = 0

    try:
        for company in companies_set:
            if i < MILESTONE:
                i = i+1
                continue
            elif i > LIMIT:
                break
            else:
                print i
                i = i+1

            if company is '' or company is None or company is u'':
                continue

            info = None
            overallRating = None

            info = getGlassdoorInfo(company)

            if info is not None:
                overallRating = info.get('overallRating', None)

            if overallRating:
                ranking.append(info)
    except Exception, e:
        pass
        # pickle.dump(ranking, open("ranking.manav.pkl", "wb" ) )
        # print len(ranking)
        # raise e
        # continue

    sorted_ranking = sorted(ranking, key=lambda k: k['overallRating'], reverse=True)

    return sorted_ranking



def getGlassdoorInfo(company):

    filename = 'pkl/' + company + ".glassdoor.pkl"
    f = open(filename, 'rb')

    if (f):
        return pickle.load(f)

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

    if employer_top is not None:
        result = {
            'id': employer_top.get('id', None),
            'name': employer_top.get('name', None),
            'website': employer_top.get('website', None),
            'numberOfRatings': employer_top.get('numberOfRatings', None),
            'squareLogo': employer_top.get('squareLogo', None),
            'overallRating': employer_top.get('overallRating', None),
        }
    else:
        result = None

    pickle.dump(result, open(company + ".glassdoor.pkl", "wb"))
    return result