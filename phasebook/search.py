from flask import Blueprint, request
from .data.search_data import USERS

bp = Blueprint("search", __name__, url_prefix="/search")

@bp.route("")
def search():
    return search_users(request.args.to_dict()), 200

def search_users(args):
            
    search_results = []
    matched_name, matched_age, matched_occupation = [], [], []
    
    user_id, user_name, user_age, user_occupation  = args.get("id"), args.get("name", "").lower() ,args.get("age"), args.get("occupation", "").lower() 
    
    for search_entry in USERS:
                
        entry_id, entry_name, entry_age, entry_occupation  = search_entry.get("id"), search_entry.get("name", "").lower() , search_entry.get("age"), search_entry.get("occupation", "").lower()    
        
        if "id" in args and user_id == entry_id:
            search_results.append(search_entry)
            
        if "name" in args and user_name in entry_name:
            matched_name.append(search_entry)
            
        if "age" in args and user_age: 
            # lower_limit = int(user_age) - 1
            # upper_limit = int(user_age) + 1 
            # age_range = list(range(lower_limit, upper_limit))
            # if entry_age in age_range : 
            if int(entry_age) > int(user_age) - 2 and int(entry_age) < int(user_age) + 2:
                matched_age.append(search_entry)
                    
        if "occupation" in args and user_occupation in entry_occupation :
            matched_occupation.append(search_entry)

    search_results.extend(matched_name)
    search_results.extend(matched_age)
    search_results.extend(matched_occupation)

    filtered = [] # remove duplicated
    for data in search_results:
        if data not in filtered:
            filtered.append(data)
            
    return filtered
    
    
