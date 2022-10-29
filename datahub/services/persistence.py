class PersistenceService:
    store = {}

    def save(self, sensor_id, configuration):
        self.store[sensor_id] = configuration
        return configuration

    def get(self, sensor_id):
        return self.store[sensor_id]
