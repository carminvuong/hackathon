from careerjet_api_client import CareerjetAPIClient

cj = CareerjetAPIClient("en_GB")


result_json = cj.search({
                        'location': 'new york',
                        'keywords': 'basketball',
                        'affid': '213e213hd12344552',
                        'user_ip': '11.22.33.44',
                        'url': 'http://www.example.com/jobsearch?q=python&l=london',
                        'user_agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:31.0) Gecko/20100101 Firefox/31.0'
                        })

for job in result_json['jobs']:
    for key in job.keys():
        print(key)
