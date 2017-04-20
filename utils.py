import datetime

def get_type(s):
    try:        
        int(s)
        return 'int'
    except ValueError:
        try:
            float(s)
            return 'float'
        except ValueError:
            try:
                datetime.datetime.strptime(s, '%m/%d/%Y')
                return 'datetime'
            except ValueError:
                try:
                    datetime.datetime.strptime(s, '%H:%M:%S')
                    return 'timestamp'
                except ValueError:
                    return 'string'