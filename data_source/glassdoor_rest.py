import urllib2, sys
import ipdb
import json
import requests

def getGlassdoorInfo(company):
	url = "http://api.glassdoor.com/api/api.htm?t.p=55690&t.k=em66CFmfXYu&userip=172.23.227.50&useragent=Mozilla&format=json&v=1&action=employers&q="
	hdr = {'User-Agent': 'Mozilla/5.0'}
	finalURL = url + urllib2.quote(company)
	req_encoded = urllib2.Request(finalURL, headers=hdr)

	print finalURL
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

print getGlassdoorInfo('Juniper Network')
