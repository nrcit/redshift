import os
import sys
import redshift_connector

sql_path = os.getenv("SQL_PATH")
execution_order = os.getenv("EXECUTION_ORDER")

# https://docs.aws.amazon.com/redshift/latest/mgmt/python-connect-examples.html
# https://www.learndatasci.com/solutions/python-check-if-files-exist/

conn = redshift_connector.connect(
    host=os.getenv("REDSHIFT_HOST"),
    port=int(os.getenv("REDSHIFT_PORT")),
    database=os.getenv("REDSHIFT_DB"),
    user=os.getenv("REDSHIFT_USER"),
    password=os.getenv("REDSHIFT_PASSWORD"),
)
cursor = conn.cursor()

def run_sql_file(filepath):
    print(f"Running {filepath}...")
    try:
        with open(filepath, "r") as f:
            sql = f.read()
            cursor.execute(sql)
            conn.commit()
        print(f"Success: {filepath}")
    except Exception as e:
        print(f"Error in {filepath}: {e}")
        conn.rollback()
        sys.exit(1)

if os.path.isfile(sql_path):
    run_sql_file(sql_path)
else:
    if execution_order:
        files = [f.strip() for f in execution_order.split(",")]
    else:
        files = sorted([f for f in os.listdir(sql_path) if f.endswith(".sql")])

    for file in files:
        run_sql_file(os.path.join(sql_path, file))

cursor.close()
conn.close()
