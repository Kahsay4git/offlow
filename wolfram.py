import requests
import xmltodict
import json

def get_json(query):
	APP_ID = 'JP5R63-435U4LVQEY'
	url = 'http://api.wolframalpha.com/v1/query?input=%s&appid=%s' %(query, APP_ID)
	print url
	print 'Requesting content'
	res = requests.get(url)
	print res.status_code
	xml_content = res.content
	dict_content = xmltodict.parse(xml_content)
	results = []
	for pod in dict_content['queryresult'].get('pod'):
		result = {}
		try:
			title = pod['@title']
			result['caption'] = title
			result['image'] = ''
			result['data'] = ''
			print(pod['subpod'])
			img = pod['subpod'].get('img')
			if img:
				link = img.get('@src')
				result['image'] = link
				data = img.get('@alt')
				result['data'] = data
			results.append(result)
		except:
			print("unable to fetch results")
	json_content = json.dumps(results)
	return json_content

def generate_output_string(result_json):
	result_json = json.loads(result_json)
	output_string = ''
	for pod in result_json:
		if pod["caption"]=="Input interpretation":
			output_string += pod["data"]+" ==> \n"
		if pod["caption"]=="Result":
			output_string += pod["data"]
	return output_string

def auto_answer(query):
	return generate_output_string(get_json(query))

