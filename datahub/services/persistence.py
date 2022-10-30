class InMemoryPersistenceService:
    store = {}

    def save(self, key, configuration):
        self.store[key] = configuration
        return configuration

    def get(self, key):
        if (key not in self.store):
            return None

        return self.store[key]
