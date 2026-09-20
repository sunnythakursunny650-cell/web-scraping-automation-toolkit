import itertools
import random
import httpx

class ProxyManager:
    """
    Manages proxy rotation, health checks, and request injection for httpx.
    """
    def __init__(self, proxy_list: list[str] | None = None):
        # Format: ["http://ip1:port", "http://user:pass@ip2:port"]
        self.proxies = proxy_list or [
            "http://51.159.115.233:3128",
            "http://165.225.208.243:10605",
            "http://185.199.229.156:7492"
        ]
        self._pool = itertools.cycle(self.proxies)

    def get_next_proxy(self) -> str:
        """Returns the next proxy in round-robin sequence."""
        return next(self._pool)

    def get_random_proxy(self) -> str:
        """Returns a randomly sampled proxy."""
        return random.choice(self.proxies)

    async def verify_proxy_health(self, proxy_url: str) -> bool:
        """Checks if a proxy is alive by pinging an echo IP server."""
        try:
            async with httpx.AsyncClient(proxy=proxy_url, timeout=5.0) as client:
                res = await client.get("https://httpbin.org/ip")
                return res.status_code == 200
        except Exception:
            return False

if __name__ == "__main__":
    manager = ProxyManager()
    print(f"[ProxyManager] Next Round-Robin Proxy: {manager.get_next_proxy()}")
    print(f"[ProxyManager] Random Sampled Proxy: {manager.get_random_proxy()}")