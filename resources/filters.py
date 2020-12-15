def normalize_path_params(#session_id=None, 
    fhr_value_min=130, fhr_value_max=160, limit=50, offset=0, **data):
    #if session_id:
     #   return { 
            #'session_id':session_id,
      #      'fhr_value_min': fhr_value_min,
       #     'fhr_value_max': fhr_value_max,
        #    'limit':limit,
         #   'offset':offset
          #  }
    return { 
        'fhr_value_min': fhr_value_min,
        'fhr_value_max': fhr_value_max,
        'limit':limit,
        'offset':offset
        }

query_without_token ="SELECT * FROM test \
                WHERE (fhr_value >=%s AND fhr_value <=%s) \
                LIMIT %s OFFSET %s"

query_test="SELECT * FROM db.test WHERE fhr_value>=%s AND fhr_value<=%s"

query_with_token = "SELECT * FROM test \
                WHERE session_id=%s AND \
                (fhr_value >= %s AND fhr_value <=%s) \
                LIMIT %s OFFSET %s"