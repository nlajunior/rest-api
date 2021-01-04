from datetime import date

def normalize_path_params(identifier=None, duration_min=0, duration_max=360, limit=50, offset=0, **data):
    if not identifier==None:
        return {
            'identifier': identifier,
            'date_created': date.today(), 
            'duration_min': duration_min,
            'duration_max': duration_max,
            'limit':limit,
            'offset':offset

        }
    return {
        'date_created': date.today(), 
        'duration_min': duration_min,
        'duration_max': duration_max,
        'limit':limit,
        'offset':offset
        }



query_with_identifier="SELECT * FROM db.test WHERE IDENTIFIER=%s AND DATE_FORMAT(date_created, '%Y-%m-%d')=%s AND duration>=%s AND duration<=%s ORDER BY duration LIMIT %s OFFSET %s"

query_without_identifier="SELECT * FROM db.test WHERE DATE_FORMAT(date_created, '%Y-%m-%d')=%s AND duration>=%s AND duration<=%s ORDER BY duration  LIMIT %s OFFSET %s"

