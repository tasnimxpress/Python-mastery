# ====================== CHECK CONNECTION ======================
# import psycopg2

# conn = psycopg2.connect(dbname="Derby",
#                         user="postgres",
#                         host="localhost",
#                         password="1234",
#                         port="5432")
# cursor = conn.cursor()
# cursor.execute('SELECT * FROM public.derby')
# rows = cursor.fetchall()
# for table in rows:
#     print(table) 
# conn.close() 



# ==================== DATA MIGRATION ==========================
import psycopg2

def transfer_data():
    # Database connection details
    source_db_config = {
        "user": "postgres",
        "password": "1234",
        "host": "localhost",
        "port": "5432", 
        "database": "Derby"
    }
    
    target_db_config = {
        "user": "postgres",
        "password": "1234",
        "host": "localhost",
        "port": "5432", 
        "database": "dwh"
    }
    
    try:
        # Connect to source (transactional) database
        source_conn = psycopg2.connect(**source_db_config)
        source_cursor = source_conn.cursor()
        
        # Connect to target (data warehouse) database
        target_conn = psycopg2.connect(**target_db_config)
        target_cursor = target_conn.cursor()
        
        # Step 1: Fetch data from the source database
        source_query = "SELECT * FROM public.derby;"
        source_cursor.execute(source_query)
        data = source_cursor.fetchall()
        
        if not data:
            print("No data found to transfer.")
            return
        
        # Step 2: Insert data into the target database
        target_query = """
            INSERT INTO ecrm_prod_wh.derby_wh (
            contact_date,
            contact_id,
            contact_no,
            primary_brand_name,
            secondary_brand_name,
            p_category,
            s_category,
            rnk,
            before_june_24,
            after_june_24
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        
        # Execute insertion
        target_cursor.executemany(target_query, data)
        target_conn.commit()
        
        print(f"Successfully transferred {len(data)} rows from source to target database.")
    
    except Exception as e:
        print("An error occurred:", e)
    
    finally:
        # Close all connections
        if 'source_cursor' in locals():
            source_cursor.close()
        if 'source_conn' in locals():
            source_conn.close()
        if 'target_cursor' in locals():
            target_cursor.close()
        if 'target_conn' in locals():
            target_conn.close()

if __name__ == "__main__":
    transfer_data()
