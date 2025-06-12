import time
import httpx
import dns.resolver
import asyncio
async def gen_asyncio_get_param(domain, path):
    resolver = dns.resolver.Resolver()
    resolver.nameservers = ['223.5.5.5']
    answer = resolver.resolve(domain, "A")
    ip = answer[0].to_text()
    url = (f"https://{ip}", {path})
    headers = {"Host": domain}
    return (url, headers)
