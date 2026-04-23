from config.db_config import GetDB

class DBManager:
    def __init__(self, collection_name):
        self.db = GetDB()
        self.collection = self.db[collection_name]
    
    def InsertMany(self, data):
        if len(data) > 0:
            ids = self.collection.insert_many(data).inserted_ids
            return ids
        else:
            return []
        
    def FindAll(self):
        data = self.collection.find()
        return list(data)
    
    def CountDocuments(self):
        count = self.collection.count_documents({})
        return count
    