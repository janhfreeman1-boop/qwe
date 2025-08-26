import yaml
import random

class ProxyManager:
    def __init__(self, config_path):
        with open(config_path, 'r') as f:
            self.config = yaml.safe_load(f)
        self.proxies = self.config['proxies']
        self.user_agents = self.config['user_agents']

    def get_proxy(self):
        proxy = random.choice(self.proxies)
        return {"server": f"http://{proxy['ip']}:{proxy['port']}"}

    def get_random_user_agent(self):
        return random.choice(self.user_agents)
