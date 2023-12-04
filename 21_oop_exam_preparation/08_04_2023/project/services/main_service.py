from project.services.base_service import BaseService


class MainService(BaseService):
    def __init__(self, name: str):
        super().__init__(name, 30)

    def details(self):
        result = f'{self.name} Main Service:\nRobots: '
        robots = ' '.join([r.name for r in self.robots]) if self.robots else 'none'
        result += robots

        return result
