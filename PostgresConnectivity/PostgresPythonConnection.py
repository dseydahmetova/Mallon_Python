import psycopg
conn = None
# Connect to an existing database
try:
    with psycopg.connect("dbname='postgres' user='postgres' host='localhost' password='postgres'") as conn:
        # Open a cursor to perform database operations
        with conn.cursor() as cur:
            # First drop the relkation if it exists
            cur.execute("DROP TABLE IF EXISTS public.test")

            # Execute a command: this creates a new table
            cur.execute("""
            CREATE TABLE public.test (
                id serial PRIMARY KEY,
                num integer,
                data text)
            """)

            # Pass data to fill a query placeholders and let Psycopg perform
            # the correct conversion (no SQL injections!)
            cur.execute("INSERT INTO public.test (num, data) VALUES (%s, %s)",
                        (100, "abc'def"))
            cur.execute("INSERT INTO public.test (num, data) VALUES (%s, %s)",
                        (101, "ghi'jkl"))
            cur.execute("INSERT INTO public.test (num, data) VALUES (%s, %s)",
                        (102, "mno'pqr"))

            # Make the changes to the database persistent
            conn.commit()

            cur.execute("UPDATE public.test SET data = 'updated abcdef' where num = 100")
            cur.execute("DELETE FROM public.test where num = 102")

            # Query the database and obtain data as Python objects.
            cur.execute("SELECT * FROM public.test")
            records = cur.fetchall()
            # will return:
            #              (1, 100, "abc'def")
            #              (2, 101, "ghi'jkl")

            # You can use `cur.fetchmany()`, `cur.fetchall()` to return a list
            # of several records, or even iterate on the cursor
            for record in records:
                print(record)
except Exception as error:
    print(error)
finally:
    if conn is not None:
        conn.close()

