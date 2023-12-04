from typing import List

from project.robots.base_robot import BaseRobot
from project.robots.female_robot import FemaleRobot
from project.robots.male_robot import MaleRobot
from project.services.base_service import BaseService
from project.services.main_service import MainService
from project.services.secondary_service import SecondaryService


class RobotsManagingApp:
    VALID_SERVICES = {'MainService': MainService, 'SecondaryService': SecondaryService}
    VALID_ROBOTS = {'MaleRobot': MaleRobot, 'FemaleRobot': FemaleRobot}

    def __init__(self):
        self.robots: List[BaseRobot] = []
        self.services: List[BaseService] = []

    def add_service(self, service_type: str, name: str):
        valid_service = self.VALID_SERVICES.get(service_type)

        if valid_service is None:
            raise Exception('Invalid service type!')

        service = valid_service(name)
        self.services.append(service)
        return f'{service_type} is successfully added.'

    def add_robot(self, robot_type: str, name: str, kind: str, price: float):
        r_class = self.VALID_ROBOTS.get(robot_type)

        if r_class is None:
            raise Exception('Invalid robot type!')

        robot = r_class(name, kind, price)
        self.robots.append(robot)
        return f'{robot_type} is successfully added.'

    def add_robot_to_service(self, robot_name: str, service_name: str):
        robot = next((r for r in self.robots if r.name == robot_name))
        service = next((s for s in self.services if s.name == service_name))

        if (robot.__class__.__name__ == 'FemaleRobot' and service.__class__.__name__ == 'MainService') \
                or (robot.__class__.__name__ == 'MaleRobot' and service.__class__.__name__ == 'SecondaryService'):
            return 'Unsuitable service.'

        if len(service.robots) == service.capacity:
            raise Exception('Not enough capacity for this robot!')

        self.robots.remove(robot)
        service.robots.append(robot)
        return f'Successfully added {robot_name} to {service_name}.'

    def remove_robot_from_service(self, robot_name: str, service_name: str):
        service = next((s for s in self.services if s.name == service_name))
        robot = next((r for r in service.robots if r.name == robot_name), None)

        if robot is None:
            raise Exception('No such robot in this service!')

        service.robots.remove(robot)
        self.robots.append(robot)
        return f'Successfully removed {robot_name} from {service_name}.'

    def feed_all_robots_from_service(self, service_name: str):
        service = next((s for s in self.services if s.name == service_name))

        [r.eating() for r in service.robots]

        return f'Robots fed: {len(service.robots)}.'

    def service_price(self, service_name: str):
        service = next((s for s in self.services if s.name == service_name))
        total_price = sum(r.price for r in service.robots)

        return f'The value of service {service_name} is {total_price:.2f}.'

    def __str__(self):
        result = [s.details() for s in self.services]

        return '\n'.join(result)
