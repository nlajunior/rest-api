from datetime import date

def normalize_path_params(date_created=None, fhr_value_min=0, fhr_value_max=160, limit=50, offset=0, **data):
    if not date_created==None:
        return {
            'date_created': date_created,
            'fhr_value_min': fhr_value_min,
            'fhr_value_max': fhr_value_max,
            'limit':limit,
            'offset':offset

        }
    return {
        'date_created': date.today(), 
        'fhr_value_min': fhr_value_min,
        'fhr_value_max': fhr_value_max,
        'limit':limit,
        'offset':offset
        }

query_without_token ="SELECT * FROM test \
                WHERE (fhr_value >=%s AND fhr_value <=%s) \
                LIMIT %s OFFSET %s"

query_test="SELECT * FROM db.test WHERE DATE_FORMAT(date_created, '%Y-%m-%d')=%s AND fhr_value>=%s AND fhr_value<=%s LIMIT %s OFFSET %s"

query_with_token = "SELECT * FROM test \
                WHERE session_id=%s AND \
                (fhr_value >= %s AND fhr_value <=%s) \
                LIMIT %s OFFSET %s"