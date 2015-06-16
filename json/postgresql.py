import psycopg2
import psycopg2.extras


def main():
    conn_string = "host='127.0.0.1' dbname='surm' user='marvin' password='marvint'"
    # print the connection string we will use to connect
    print("Connecting to database\n\t-->%s\n" % (conn_string))

    conn = psycopg2.connect(conn_string)

    # HERE IS THE IMPORTANT PART, by specifying a name for the cursor
    # psycopg2 creates a server-side cursor, which prevents all of the
    # records from being downloaded at once from the server.
    cursor = conn.cursor('cursor_unique_name', cursor_factory=psycopg2.extras.DictCursor)
    cursor.execute('SELECT * FROM surm.meeting')

    # Because cursor objects are iterable we can just call 'for - in' on
    # the cursor object and the cursor will automatically advance itself
    # each iteration.
    # This loop should run 1000 times, assuming there are at least 1000
    # records in 'surm.room'
    row_count = 0
    for row in cursor:
        row_count += 1
        print("row:%s | %s\n" % (row_count, row))


if __name__ == "__main__":
    main()
