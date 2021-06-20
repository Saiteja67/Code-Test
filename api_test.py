import requests

"""
Assumptions:
1. All the fields in the json is mandatory, if any field is missed we will define it as ERROR.
"""

if __name__ == "__main__":

        # URL
        rest_api = 'https://eacp.energyaustralia.com.au/codingtest/api/v1/festivals'
        print(rest_api)

        # Hitting the API
        resp = requests.get(rest_api, headers={"content-type": "text"})
        code =  resp.status_code
        print("Resp code: {}".format(code))

        # Handling scenario:1
        if code == 429:
            print("ERROR!..Too many requests to the server: error code: {}".format(code))
            exit(1)

        elif code == 200:
            resp_data = resp.json()
            print("Response data: {}".format(resp_data))
            # Handling scenario:2
            if resp_data == "":
                print("The response from the API is empty")
                exit(1)
            else:
                for item in resp_data:
                    name = item.get('name', None)

                    # Scenario:3
                    if 'bands' not in item.keys():
                        print("ERROR!..The data format is not in the right format!"
                              "bands key is not found in the response!, data:{}".format(item))
                        exit(1)

                    band_data = item.get('bands')

                    for bdata in band_data:
                        if 'name' not in bdata.keys() or 'recordLabel' not in bdata.keys():
                            print("ERROR!..The data format is not in the right format"
                                  "\n either name or recordLabel is not found in the bands object,"
                                  "data:{}".format(item))
                            exit(1)

                # Scenario 5
                print("Success! Response is received with right format!")

        # Handling scenario 4
        else:
            print("ERROR! Something went wrong with status code:{}".format(code))

