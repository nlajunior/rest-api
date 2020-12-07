def normalize_path_params(token=None, frh_valeu_min=0, frh_valeu_max=5, limit=50, offset=0, **dados):
    if token:
        return { 
            'token':token,
            'frh_valeu_min': frh_valeu_min,
            'frh_valeu_max': frh_valeu_max,
            'limit':limit,
            'offset':offset
            }
        return { 
            'frh_valeu_min': frh_valeu_min,
            'frh_valeu_max': frh_valeu_max,
            'limit':limit,
            'offset':offset
            }

query_without_token ="SELECT * FROM tests \
                WHERE (fhr_valeu >=%s AND fhr_valeu <=%s) \
                LIMIT % OFFSET %"

query_with_token = "SELECT * FROM tests \
                WHERE token=%s AND \
                (fhr_valeu >= %s AND fhr_valeu <=%s) \
                LIMIT %s OFFSET %s"