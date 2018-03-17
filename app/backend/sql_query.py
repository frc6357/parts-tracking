## sql query interface

import psycopg2, sys

from psycopg2 import pool
from psycopg2 import extras

conn_pool = None


def init_db(config_info):
    global conn_pool
    connection_string = "dbname=%s user=%s password=%s host=%s port=%s"
    connection_string_data = (config_info['name'],
                              config_info['user'],
                              config_info['password'],
                              config_info['host'],
                              config_info['port'])
    conn_pool = psycopg2.pool.ThreadedConnectionPool(1, 3, connection_string % connection_string_data)

    DEC2FLOAT = psycopg2.extensions.new_type(
        psycopg2.extensions.DECIMAL.values,
        'DEC2FLOAT',
        lambda value, curs: float(value) if value is not None else None)
    psycopg2.extensions.register_type(DEC2FLOAT)


def execute_query(query, args):
    ## Get connection
    conn = conn_pool.getconn()
    ## get cursor
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    ## Pass the query)
    try:
        cur.execute(query, args)
    except:
        conn.rollback()
        cur.close()
        conn_pool.putconn(conn)
        return {'status': 'exception', 'info': str(sys.exc_info()[0])}
    ## return the result
    result = cur.fetchall()
    ## here's a place to log activity
    ## commit the result
    conn.commit()
    ## close the cursor
    cur.close()
    ## return the connection to the pool
    conn_pool.putconn(conn)

    return result


def close_db():
    conn_pool.closeall()
