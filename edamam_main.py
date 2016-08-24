import edamamAPI

#sample input
query = 'vegetarian gluten free low fat low sugar salad'
num_results = 1
#get results
Results = edamamAPI.adamam_funct(query, num_results)
#sample output

for i in range(len(Results['labels'])):
	print('\n===== Result %s: %s =====' %(i+1,Results['labels'][i]))
	print('   image url: %s' %Results['images_url'][i])
	print('   recipe url: %s' %Results['recipes'][i])
	print('   incredients:')
	for j in range(len(Results['ingredients'][i])):
		print('       %s' %Results['ingredients'][i][j])
	print('   total calory: %.2f' %Results['totalCalories'][i])
	print('   yield: %s' %Results['yield'][i])
	print('   calory per serve: %.2f' %(Results['totalCalories'][i]/Results['yield'][i]))
	print('   nutrients per serve:')
	for j in Results['totalDaily'][i]:
		print('       %s: %.2f %s (%.2f %%)' %(Results['totalNutrients'][i][j]['label'],Results['totalNutrients'][i][j]['quantity']/Results['yield'][i],Results['totalNutrients'][i][j]['unit'],Results['totalDaily'][i].get(j).get('quantity')/Results['yield'][i]))