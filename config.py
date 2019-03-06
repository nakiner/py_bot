class Config:

    api_id = 411310
    api_hash = 'a857081a17a549b09d75d7fd4316b2b1'
    session = 'default'

    def __getattr__(self, attr):
        return attr
