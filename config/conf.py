
DB_SCHEMA_NAME = 'ddb_pl' # This will be changed according to market

def get_db_name():
    if DB_SCHEMA_NAME == 'ddb_mx':
        return "sqlite:///./dynamicModeling.db"
    if DB_SCHEMA_NAME == 'ddb_pl':
        return "sqlite:///./dynamicModeling_pl.db"