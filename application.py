from module.base_module import BaseModule
from structure.cluster import Cluster


class Application:
    def __init__(self):
        pass

    def run_modules(self, modules: list):
        module: BaseModule
        cluster = Cluster()
        for module in modules:
            command = module.get_command()
            cluster = command(cluster)
        print()