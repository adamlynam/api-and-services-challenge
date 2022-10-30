class InMemoryPersistenceService:
    store = {}

    def save(self, key, configuration):
        self.store[key] = configuration
        return configuration

    def get(self, key):
        return self.store[key]
