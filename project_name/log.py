import logging, json

#helper that presents a forms errors in a loggable string
badform = lambda msg, form: '%s: [%s]' % (msg, ', '.join(["'%s %s'" % (field, '&'.join(form.errors[field])) for field in form.errors]))

def req(request):
    """
    Helper that extracts some interesting data from the request
    and returns it as a dictionary to be consumed by a logger.
    """

    params = {}

    try:
        params['user'] = request.user.email
    except:
        pass

    return params

#initial implementation from:
#https://github.com/madzak/python-json-logger

class JsonFormatter(logging.Formatter):
    """A custom formatter to format logging records as json objects"""

    def format(self, record):
        record.msg = record.msg.upper()

        log_record = {}

        for formatter in self._fmt:
            try:
                log_record[formatter] = record.__dict__[formatter]
            except:
                log_record[formatter] = None

        return json.dumps(log_record)