clientid = "ReplaceWithYourClientID"
clientsecret = "ReplaceWithYourClientSecret"

import requests

oauthlink = f"https://eu.battle.net/oauth/token?grant_type=client_credentials"

oauthreq = requests.post(oauthlink, auth=(clientid, clientsecret))

oauth = oauthreq.json()['access_token']

while True:
	raiderio = input("raiderio: ").split('/')
	realm = raiderio[5]
	character = raiderio[6].split('?')[0]

	link = f"https://eu.api.blizzard.com/profile/wow/character/{realm}/{character.lower()}/achievements?namespace=profile-eu&locale=en_US&access_token={oauth}"


	r = requests.get(link).json()

	achis = r['achievements']
	achis.sort(key = (lambda obj: obj.get('completed_timestamp') or obj.get('timestamp') or 0))

	for achi in achis:
		try:
			isCurve = (achi['achievement']['name'].startswith("Ahead of the Curve:") or achi['achievement']['name'].startswith("Cutting Edge:"))

			if isCurve:
				print(achi['achievement']['name'])

		except KeyError as e:
			pass

	print('\r')
