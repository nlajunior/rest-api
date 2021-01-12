from datetime import date

def normalize_path_params(identifier=None, duration_min=-1, duration_max=400, limit=50, offset=0, **data):
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


query_with_identifier="SELECT * FROM db.test WHERE IDENTIFIER=%s AND DATE_FORMAT(date_created, '%Y-%m-%d')=%s AND duration>=%s AND duration<=%s ORDER BY duration LIMIT %s OFFSET %s"

query_without_identifier="SELECT * FROM db.test WHERE DATE_FORMAT(date_created, '%Y-%m-%d')=%s AND duration>=%s AND duration<=%s ORDER BY duration  LIMIT %s OFFSET %s"

join_1 = "SELECT t.duration, t.fhr_value, t.date_created, t.identifier, t.device_id FROM db.test as t inner join db.monitoring as m on t.identifier=m.identifier WHERE DATE_FORMAT(t.date_created, '%Y-%m-%d')=%s AND t.duration>=%s AND t.duration<=%s AND m.status=1 ORDER BY t.duration  LIMIT %s OFFSET %s"
join_2 = "SELECT t.duration, t.fhr_value, t.date_created, t.identifier, t.device_id FROM db.test as t inner join db.monitoring as m on t.identifier=m.identifier WHERE t.IDENTIFIER=%s AND DATE_FORMAT(t.date_created, '%Y-%m-%d')=%s AND t.duration>=%s AND t.duration<=%s AND m.status=1 ORDER BY t.duration  LIMIT %s OFFSET %s"