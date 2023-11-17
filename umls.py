import json
import requests


class UMLS:
    def __init__(self, api_key):
        self.__api_key = api_key
        self.__base_url = "https://uts-ws.nlm.nih.gov/rest"

   
    def retrieve_cuis(self, query, version='current',inputType='atom',includeObsolete=False,includeSuppressible=False,returnIdType='concept',sabs=[],
                     searchType='words',partialSearch=False,pageNumber=1,pageSize=25):
        search_endpoint = f"{self.__base_url}/search/{version}"

        params = {
            "string": query,
            "apiKey": self.__api_key,
            "inputType":inputType,
            "searchType":searchType,
            "pageNumber":pageNumber,
            "pageSize":pageSize,
            "returnIdType":returnIdType
        }

        if (includeObsolete):
            params["includeObsolete"] = 'true'
        else:
            params["includeObsolete"] = 'false'

        if (includeSuppressible):
            params["includeSuppressible"] = 'true'
        else:
            params["includeSuppressible"] = 'false'

        if (partialSearch):
            params["partialSearch"] = 'true'
        else:
            params["partialSearch"] = 'false'
        
        if (len(sabs)==1):
            params["sabs"] = sabs[0]
        elif(len(sabs)>1):
            sabsString = ','.join(sabs)
            params["sabs"] = sabsString

        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        response = requests.get(search_endpoint, params=params,headers=headers)
        data = response.json()

        if response.status_code == 200:
            return data
        else:
            raise Exception(f"Search failed. Status code: {response.status_code}")
        
    def retrieve_cui_info(self, cui, version='current'):
        search_endpoint = f"{self.__base_url}/content/{version}/CUI/{cui}"
        params = {"apiKey":self.__api_key}

        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        response = requests.get(search_endpoint, params=params,headers=headers)
        data = response.json()

        if response.status_code == 200:
            return data
        else:
            raise Exception(f"Search failed. Status code: {response.status_code}")

        
    

    def retrieve_cui_atoms(self, cui, version='current', preferred=False,includeObsolete=True,includeSuppressible=True,sabs=[],language='',ttys=[]
                          ,pageNumber=1,pageSize=25):
        search_endpoint = f"{self.__base_url}/content/{version}/CUI/{cui}/atoms"
        if preferred:
            search_endpoint += "/"+"preferred"
        params = {
            "apiKey": self.__api_key,
            "pageNumber":pageNumber,
            "pageSize":pageSize,
        }

        if (len(sabs)==1):
            params["sabs"] = sabs[0]
        elif(len(sabs)>1):
            sabsString = ','.join(sabs)
            params["sabs"] = sabsString

        if (len(ttys)==1):
            params["ttys"] = ttys[0]
        elif(len(ttys)>1):
            ttysString = ','.join(ttys)
            params["ttys"] = ttysString
        
        if (includeObsolete):
            params["includeObsolete"] = 'true'
        else:
            params["includeObsolete"] = 'false'

        if (includeSuppressible):
            params["includeSuppressible"] = 'true'
        else:
            params["includeSuppressible"] = 'false'

        if (language != ''):
            params['language'] = language


        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        response = requests.get(search_endpoint, params=params,headers=headers)
        data = response.json()

        if response.status_code == 200:
            return data
        else:
            raise Exception(f"Search failed. Status code: {response.status_code}")
        

    
    def retrieve_cui_definitions(self, cui, version='current',sabs=[], pageNumber=1, pageSize=25):
        search_endpoint = f"{self.__base_url}/content/{version}/CUI/{cui}/definitions"
        
        params = {
            "apiKey": self.__api_key,
            "pageNumber":pageNumber,
            "pageSize":pageSize,
        }

        if (len(sabs)==1):
            params["sabs"] = sabs[0]
        elif(len(sabs)>1):
            sabsString = ','.join(sabs)
            params["sabs"] = sabsString


        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        response = requests.get(search_endpoint, params=params,headers=headers)
        data = response.json()

        if response.status_code == 200:
            return data
        else:
            raise Exception(f"Search failed. Status code: {response.status_code}")
        

    def retrieve_cui_relations(self, cui, version='current', includeRelationLabels=[],includeAdditionalRelationLabels=[],includeObsolete=False,includeSuppressible=False,sabs=[]
                          ,pageNumber=1,pageSize=25):
        search_endpoint = f"{self.__base_url}/content/{version}/CUI/{cui}/relations"
        params = {
            "apiKey": self.__api_key,
            "pageNumber":pageNumber,
            "pageSize":pageSize,
        }

        if (len(sabs)==1):
            params["sabs"] = sabs[0]
        elif(len(sabs)>1):
            sabsString = ','.join(sabs)
            params["sabs"] = sabsString
        
        if (len(includeRelationLabels)==1):
            params["includeRelationLabels"] = includeRelationLabels[0]
        elif(len(includeRelationLabels)>1):
            labels = ','.join(includeRelationLabels)
            params["includeRelationLabels"] = labels
        
        if (len(includeAdditionalRelationLabels)==1):
            params["includeAdditionalRelationLabels"] = includeAdditionalRelationLabels[0]
        elif(len(includeAdditionalRelationLabels)>1):
            labels = ','.join(includeAdditionalRelationLabels)
            params["includeAdditionalRelationLabels"] = labels
        
        if (includeObsolete):
            params["includeObsolete"] = 'true'
        else:
            params["includeObsolete"] = 'false'

        if (includeSuppressible):
            params["includeSuppressible"] = 'true'
        else:
            params["includeSuppressible"] = 'false'


        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        response = requests.get(search_endpoint, params=params,headers=headers)
        data = response.json()

        if response.status_code == 200:
            return data
        else:
            raise Exception(f"Search failed. Status code: {response.status_code}")
        
    
    def retrieve_source_asserted_id_info(self,id,source,version='current'):
        search_endpoint = f"{self.__base_url}/content/{version}/source/{source}/{id}"
        params = {
            "apiKey": self.__api_key,
        }

        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        response = requests.get(search_endpoint, params=params,headers=headers)
        data = response.json()

        if response.status_code == 200:
            return data
        else:
            raise Exception(f"Search failed. Status code: {response.status_code}")


    
    def retrieve_source_asserted_id_atoms(self,id,source,version='current'):
        search_endpoint = f"{self.__base_url}/content/{version}/source/{source}/{id}/atoms"
        params = {
            "apiKey": self.__api_key,
        }

        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        response = requests.get(search_endpoint, params=params,headers=headers)
        data = response.json()

        if response.status_code == 200:
            return data
        else:
            raise Exception(f"Search failed. Status code: {response.status_code}")
    

    def retrieve_source_asserted_id_parents(self,id,source,version='current',pageNumber=1,pageSize=25):
        search_endpoint = f"{self.__base_url}/content/{version}/source/{source}/{id}/parents"
        params = {
            "apiKey": self.__api_key,
            "pageNumber":pageNumber,
            "pageSize":pageSize,
        }

        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        response = requests.get(search_endpoint, params=params,headers=headers)
        data = response.json()

        if response.status_code == 200:
            return data
        else:
            raise Exception(f"Search failed. Status code: {response.status_code}")
    
    def retrieve_source_asserted_id_children(self,id,source,version='current',pageNumber=1,pageSize=25):
        search_endpoint = f"{self.__base_url}/content/{version}/source/{source}/{id}/children"
        params = {
            "apiKey": self.__api_key,
            "pageNumber":pageNumber,
            "pageSize":pageSize,
        }

        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        response = requests.get(search_endpoint, params=params,headers=headers)
        data = response.json()

        if response.status_code == 200:
            return data
        else:
            raise Exception(f"Search failed. Status code: {response.status_code}")
        
    def retrieve_source_asserted_id_ancestors(self,id,source,version='current',pageNumber=1,pageSize=25):
        search_endpoint = f"{self.__base_url}/content/{version}/source/{source}/{id}/ancestors"
        params = {
            "apiKey": self.__api_key,
            "pageNumber":pageNumber,
            "pageSize":pageSize,
        }

        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        response = requests.get(search_endpoint, params=params,headers=headers)
        data = response.json()

        if response.status_code == 200:
            return data
        else:
            raise Exception(f"Search failed. Status code: {response.status_code}")
    
    def retrieve_source_asserted_id_descendants(self,id,source,version='current',pageNumber=1,pageSize=25):
        search_endpoint = f"{self.__base_url}/content/{version}/source/{source}/{id}/descendants"
        params = {
            "apiKey": self.__api_key,
            "pageNumber":pageNumber,
            "pageSize":pageSize,
        }

        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        response = requests.get(search_endpoint, params=params,headers=headers)
        data = response.json()

        if response.status_code == 200:
            return data
        else:
            raise Exception(f"Search failed. Status code: {response.status_code}")
        
    
    def retrieve_source_asserted_id_relations(self,id,source,version='current',pageNumber=1,pageSize=25,
                                              includeRelationLabels=[],includeAdditionalRelationLabels=[],includeObsolete=False,includeSuppressible=False):
        search_endpoint = f"{self.__base_url}/content/{version}/source/{source}/{id}/relations"
        params = {
            "apiKey": self.__api_key,
            "pageNumber":pageNumber,
            "pageSize":pageSize,
        }

        if (len(includeRelationLabels)==1):
            params["includeRelationLabels"] = includeRelationLabels[0]
        elif(len(includeRelationLabels)>1):
            labels = ','.join(includeRelationLabels)
            params["includeRelationLabels"] = labels
        
        if (len(includeAdditionalRelationLabels)==1):
            params["includeAdditionalRelationLabels"] = includeAdditionalRelationLabels[0]
        elif(len(includeAdditionalRelationLabels)>1):
            labels = ','.join(includeAdditionalRelationLabels)
            params["includeAdditionalRelationLabels"] = labels
        
        if (includeObsolete):
            params["includeObsolete"] = 'true'
        else:
            params["includeObsolete"] = 'false'

        if (includeSuppressible):
            params["includeSuppressible"] = 'true'
        else:
            params["includeSuppressible"] = 'false'


        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        response = requests.get(search_endpoint, params=params,headers=headers)
        data = response.json()

        if response.status_code == 200:
            return data
        else:
            raise Exception(f"Search failed. Status code: {response.status_code}")
        
    
    def retrieve_source_asserted_id_attributes(self,id,source,version='current',pageNumber=1,pageSize=25,includeAttributeNames=[]):
        search_endpoint = f"{self.__base_url}/content/{version}/source/{source}/{id}/attributes"
        params = {
            "apiKey": self.__api_key,
            "pageNumber":pageNumber,
            "pageSize":pageSize,
        }

        if (len(includeAttributeNames)==1):
            params["includeAttributeNames"] = includeAttributeNames[0]
        elif(len(includeAttributeNames)>1):
            labels = ','.join(includeAttributeNames)
            params["includeAttributeNames"] = labels
        
      
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        response = requests.get(search_endpoint, params=params,headers=headers)
        data = response.json()

        if response.status_code == 200:
            return data
        else:
            raise Exception(f"Search failed. Status code: {response.status_code}")
    
    def retrieve_tui_info(self,id,version='current'):
        search_endpoint = f"{self.__base_url}/semantic-network/{version}/TUI/{id}"
        params = {
            "apiKey": self.__api_key,
        }    
            
      
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        response = requests.get(search_endpoint, params=params,headers=headers)
        data = response.json()

        if response.status_code == 200:
            return data
        else:
            raise Exception(f"Search failed. Status code: {response.status_code}")
    
    
    def crosswalk_vocabs_using_cuis(self,id,source,version='current',targetSource=[],includeObsolete=False,pageNumber=1,pageSize=25):
        search_endpoint = f"{self.__base_url}/crosswalk/{version}/source/{source}/{id}"
        params = {
            "apiKey": self.__api_key,
            "pageNumber":pageNumber,
            "pageSize":pageSize,
        }    

        if (len(targetSource)==1):
            params["targetSource"] = targetSource[0]
        elif(len(targetSource)>1):
            targetSourceString = ','.join(targetSource)
            params["includeAdditionalRelationLabels"] = targetSourceString
        
        if (includeObsolete):
            params["includeObsolete"] = 'true'
        else:
            params["includeObsolete"] = 'false'
      
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        response = requests.get(search_endpoint, params=params,headers=headers)
        data = response.json()

        if response.status_code == 200:
            return data
        else:
            raise Exception(f"Search failed. Status code: {response.status_code}")



    




        




   



