def to_country_name(country_code):
    """
    This function is responsable for convert the country code into a real country name.
    
    It's pretty simple to use. Just input the code and return the name.
    
    """
    
    countries = {
        1: 'India',
        14: 'Australia',
        30: 'Brazil',
        37: 'Canada',
        94: 'Indonesia',
        148: 'New Zeland',
        162: 'Philippines',
        166: 'Qatar',
        184: 'Singapure',
        189: 'South Africa',
        191: 'Sri Lanka',
        208: 'Turkey',
        214: 'United Arab Emirates',
        215: 'England',
        216: 'United States of America'
    }
    
    return countries[country_code]

def convert_price_range(price_range):
    """
    This function will translate the prince range into a cost category, as follows:
    
    1 -> cheap
    2 -> normal
    3 -> expensive
    Up to 4 -> gourmet
    
    """
    
    if price_range == 1:
        return 'cheap'
    
    elif price_range == 2:
        return 'normal'
    
    elif price_range == 3:
        return 'expensive'
    
    else:
        return 'gourmet'
    
def to_color_name(color_code):
    """
    This function receives a number which represents a rating color and convert it into a color name.
    
    """
    
    colors = {
        '3F7E00': 'darkgreen',
        '5BA829': 'green',
        '9ACD32': 'lightgreen',
        'CDD614': 'orange',
        'FFBA00': 'red',
        'CBCBC8': 'pink',
        'FF7800': 'darkred'
    }
    
    return colors[color_code]

def split_cuisines(cuisines_name):
    """
    This function splits the Cuisines column data by comma into a list and returns only the first elements. 
    
    """
    
    new_cuisines = cuisines_name.split(',')[0]
    
    return new_cuisines