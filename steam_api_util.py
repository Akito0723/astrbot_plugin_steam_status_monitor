import httpx
import ssl

async def gen_asyncio_get_param(domain, path):
    ip = '104.68.104.163'
    url = (f"https://{ip}", {path})
    headers = {"Host": domain}
    return (url, headers)


def gen_transport():
    context = ssl.create_default_context()
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE
    transport = httpx.AsyncHTTPTransport(verify=context)
    return transport
