from datetime import date

def normalize_path_params(identifier=None, duration_min=1, duration_max=400, limit=50, offset=0, **data):
    if not identifier==None:
        return {
            'identifier': identifier,
            'date_created': str(date.today()), 
            'duration_min': duration_min,
            'duration_max': duration_max,
            'limit':limit,
            'offset':offset
        }
    return {
        'date_created': str(date.today()), 
        'duration_min': duration_min,
        'duration_max': duration_max,
        'limit':limit,
        'offset':offset
        
        
        }

query_with_identifier="SELECT duration, fhr_value, identifier FROM db.test WHERE identifier=%s AND DATE_FORMAT(date_created, '%Y-%m-%d')=%s AND duration>=%s AND duration<=%s ORDER BY identifier, duration asc LIMIT %s OFFSET %s"
query_without_identifier="SELECT duration, fhr_value, identifier FROM db.test WHERE DATE_FORMAT(date_created, '%Y-%m-%d')=%s AND duration>=%s AND duration<=%s ORDER BY identifier, duration asc LIMIT %s OFFSET %s"

query_3 = "SELECT duration, fhr_value, identifier FROM db.test WHERE identifier IN(%s) AND DATE_FORMAT(date_created, '%Y-%m-%d')='2021-01-27' AND duration>=5 AND duration<=50 ORDER BY identifier, duration asc LIMIT 50"
join_1 = "SELECT t.duration, t.fhr_value, t.date_created, t.identifier, t.device_id FROM db.test as t inner join db.monitoring as m on t.identifier=m.identifier WHERE DATE_FORMAT(t.date_created, '%Y-%m-%d')=%s AND t.duration>=%s AND t.duration<=%s AND m.status=1 ORDER BY t.duration  LIMIT %s OFFSET %s"
join_2 = "SELECT t.duration, t.fhr_value, t.date_created, t.identifier, t.device_id FROM db.test as t inner join db.monitoring as m on t.identifier=m.identifier WHERE t.IDENTIFIER=%s AND DATE_FORMAT(t.date_created, '%Y-%m-%d')=%s AND t.duration>=%s AND t.duration<=%s AND m.status=1 ORDER BY t.duration  LIMIT %s OFFSET %s"