#function to get Endpoint
def edamamAPI_getEndpoint(type = 'food') :
  endpoints = {
    'food' : 'https://api.edamam.com/search'
  }
  return endpoints.get(type)

import requests 
import json

def adamam_funct(*input_info): #there may be only one input argument: search content, or two arguments: search content and number of results to be shown
  input_num = 1 
  if len(input_info) == 2: #two arguments input
    if type(input_info[0]) == type('str'):
      query_q = input_info[0]
      if type(input_info[1]) == type(1):
        to = input_info[1]
      else:
        to = 10 #set the default number of output results to be 10
        input_num = 0
    else:
        print('Please input the food name and number of results')
  if len(input_info) == 1: #search content is the only input
    if type(input_info[0]) == type('str'):
      query_q = input_info[0]
      to = 10
      input_num = 0
    else:
      print('Please input the food name and number of results')

  if len(input_info) > 2:
    print('Too many inputs, please input the food name and number of results')

#app id and key
  cred = {
    'app_id' : 'fa03f952',
    'app_key' : '2e8f40ea6f39bfd2d44b35b1ea3db155'
  }

  query = {
    'q':query_q,
    'from': 0,
    'to' : to,
    'health':[],
    'diet':[]
  }

  diet = {
    'balanced',
    'low carb',
    'low fat',
    'low sodium',
    'high fiber',
    'high protein'
  }


  allergies = {
    'gluten free',
    'dairy free',
    'egg free',
    'soy free',
    'wheat free',
    'fish free',
    'shellfish free',
    'tree nut free',
    'peanut free',
    'alcohol free',
    'low sugar',
    'sugar conscious',
    #'low fat abs', https://developer.edamam.com/edamam-docs-recipe-api
    'vegetarian',
    'vegan',
    'paleo',
    'low potassium',
    'no oil added',
    'kidney friendly',
  }

#split search content (a sentence) so that we can analyze it.
  q_split = query['q'].split(' ')
  for allergy_name in allergies:
    if allergy_name in query['q']:
      query['health'].append(allergy_name.replace(' ','-'))
      allergy_name_split = allergy_name.split(' ')
      for i in allergy_name_split:
        del q_split[q_split.index(i)]
  for diet_name in diet:
    if diet_name in query['q']:
      query['diet'].append(diet_name.replace(' ','-'))
      diet_name_split = diet_name.split(' ')
      for i in diet_name_split:
        del q_split[q_split.index(i)]

###########################################################################

  query['q'] = ' '.join(q_split)

  query.update(cred)
  endpoint = edamamAPI_getEndpoint('food')
  response = requests.get(endpoint, params = query)
  '''
    -> output selection
  '''
  #print(response.text)
  #print(response.url)

  data_json = response.text.encode('ascii','ignore') #generate string only for online jsonviewer for output analyzing

  data = json.loads(response.text)

#output we are interested in.
  recipes = []
  ingredients = []
  images_url = []
  totalCalories = []
  labels = []
  totalNutrients = []
  totalDaily = []
  yields = []
  for i in range(len(data['hits'])):
    recipes.append((data['hits'][i]['recipe']['url']))  
    ingredients.append(data['hits'][i]['recipe']['ingredientLines'])
    images_url.append(data['hits'][i]['recipe']['image'])
    totalCalories.append(data['hits'][i]['recipe']['calories'])
    labels.append(data['hits'][i]['recipe']['label'])
    totalNutrients.append(data['hits'][i]['recipe']['totalNutrients'])
    totalDaily.append(data['hits'][i]['recipe']['totalDaily'])
    yields.append(data['hits'][i]['recipe']['yield'])

#just to show the search content and number of results for checking purpose
  print('------------------------------------')
  print('Health option: %s' %query['health']) 
  print('Diet option: %s' %query['diet'])
  print('search: %s' %query['q'])
  if input_num == 1:
    print('number of results: %s' %to)
  else:
    print('number of results: %s (default)' %to)
  print('------------------------------------')
  return {
    'recipes': recipes,
    'ingredients': ingredients,
    'images_url':images_url,
    'totalCalories':totalCalories,
    'labels':labels,
    'yield':yields,
    'totalNutrients':totalNutrients,
    'totalDaily':totalDaily
    }

