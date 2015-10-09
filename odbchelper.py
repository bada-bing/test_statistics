__author__ = 'Milan'

def buildConnectionString(params):
    """
    Function doc string:
    :param params:
    :return: db connection string
    """
    return ";".join(["%s=%s" % (k, v) for k, v in params.items()])

if __name__ == "__main__":
        myParams = {
            "server":"mpilgrim",
            "database":"master",
            "user_id":"sa",
            "password":"secret"
        }
if __name__ == "__main__":
    print(buildConnectionString(myParams))
else:
    print(__name__)
    print(__author__)