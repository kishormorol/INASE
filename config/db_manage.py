from config.crud_operation import DBManager

def DBmanage(collection_name, data):
    db = DBManager(collection_name=collection_name)
    print('*' * 60)
    prev_data = db.CountDocuments()
    print(f'Previous data : {prev_data}')
    ids = db.InsertMany(data)
    print(f'Inserted data : {len(ids)}')
    prev_data = db.CountDocuments()
    print(f'Total data    : {prev_data}')
    print('*' * 60)

    print('-' * 60)
    print(' ' * 25 + 'Cleaning data')
    print('-' * 60)
    ids.clear()
    print('Data Cleaned Successfully.')
    print('-' * 60)
