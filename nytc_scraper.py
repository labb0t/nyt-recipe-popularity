'''
This script connects to cooking.nytimes.com and uses Beautiful Soup to scrape 
recipes from the top 40 pages of recipes tagged "Dinner". The data is 
saved in pickle files.
'''
from bs4 import BeautifulSoup
import requests
import numpy as np


def get_recipe_urls(destination_list):
    '''
    Scrape recipe links from search results page and append to the destination list.
    Current range is set to the first 40 pages of results, dating back to ~2014.

    Parameters
    ----------
    destination_list : the list to which URLs will be appended
    
    Returns
    -------
    None.

    '''
    for p in range(1,41,1):
        url = "https://cooking.nytimes.com/search?filters%5Bmeal_types%5D%5B%5D=dinner&q=&page="+str(p)
        r = requests.get(url)
        soup = BeautifulSoup(r.content,features="lxml")
        for i in soup.find_all('article', {'class': 'card recipe-card'}):
            link_string = i.find('a')['href']
            destination_list.append('https://cooking.nytimes.com'+link_string)
    return destination_list

 

def get_recipe_details(recipe_url):
    '''
    Creates a dictionary of the categories of scraped data for each recipe. Returns NaN for unavailable data.

    Parameters
    ----------
    url : the url for a recipe on cooking.nytimes.com

    Returns
    -------
    A dictionary of scraped data for the recipe
    '''
    # request HTML and parse
    recipe_response = requests.get(recipe_url)
    page = recipe_response.text
    soup = BeautifulSoup(page, "lxml")
    
    # title
    try:
        title = soup.find('h1', {'class': 'recipe-title title name'}).text.strip()
    except:
        title = np.NaN
    
    # date of the original image post date
    try:
        img = str(soup.find('meta', {'property': 'og:image'}))
        img_start = 'images/'
        img_date = img.split(img_start)[1][:10]
    except:
        img_date = np.NaN
    
    # upload date
    try:
        app_json = str(soup.find('script', {'type': 'application/ld+json'}))
        start = '"uploadDate":"'
        upload_date = app_json.split(start)[1][:10]
    except:
        upload_date = np.NaN
    
    # instances of article features
    try:    
        features_html = soup.find('p', {'class': "related-article"}).find_all('a')
        features = []
        for f in features_html:
            feature = f.text.strip()
            features.append(feature)
    except:
        features = np.NaN
    
    # calories per serving
    try:
        calories = soup.find('span', {'class': 'calorie-count'}).text
    except:
        calories = np.NaN
    
    # cook time
    try:
        cook_time = soup.find_all('span', {'class': 'recipe-yield-value'})[1].text
        #cook_time = soup.find('p', {'class': 'cooking-time'}).text
    except:
        cook_time = np.NaN
    
    #recipe steps
    try:
        recipe_steps_html = soup.find('ol',{'class':'recipe-steps'}).find_all('li')
        recipe_steps = []
        for r in recipe_steps_html:
            step = r.text.strip()
            recipe_steps.append(step)
        num_steps = len(recipe_steps)
    except:
        recipe_steps = np.NaN
        num_steps = np.NaN
        
    # author
    try:
        author = soup.find('div', {'class': 'nytc---recipebyline---bylinePart'}).find('a').text
    except:
        author = np.NaN
    
    # ingredients and number of ingredients  
    try:
        ingredients_html = soup.find_all('span',{'class':'ingredient-name'})
        ingredients = []
        for i in ingredients_html:
            ingredient = i.text.strip()
            ingredients.append(ingredient)
        num_ingredients = len(ingredients)
        #str_ingredients = ",".join(ingredients)
    except:
        ingredients = np.NaN
        num_ingredients = np.NaN
        #str_ingredients = np.NaN
    
    # tags
    try:
        
        tags_html = soup.find_all('a',{'class':'tag'})
        tags = []
        for t in tags_html:
            tags.append(t.text)
    except:
        tags = np.NaN

    # topnote
    try:
        topnote = soup.find('div', {'class': 'topnote'}).find('p').text
    except:
        topnote = np.NaN
        
    # rating count
    try:
        rating_start = '"ratingCount":'
        rating_count = app_json.split(rating_start)[1].split('}')[0]
    except:
        rating_count = np.NaN
        
    # avg rating
    try:
        avg_rating_start = '"ratingValue":'
        avg_rating = app_json.split(avg_rating_start)[1].split(',')[0]
    except:
        avg_rating = np.NaN
    
    # add all features to dict
    headers = ['title','img_date', 'upload_date', 'features', 'calories', 'cook_time', 'recipe_steps', 'num_steps', 'author',
                                     'ingredients','num_ingredients', 'tags', 'topnote', 'rating_count', 'avg_rating']
    recipe_dict = dict(zip(headers, [title, img_date, upload_date, features, calories, cook_time, recipe_steps, num_steps, author,
                                     ingredients, num_ingredients, tags, topnote, rating_count, avg_rating]))
    return(recipe_dict)


