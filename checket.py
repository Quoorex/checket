import os
from multiprocessing.pool import Pool

import whois

domains = [l.strip("\n") for l in open("domains.txt").readlines()]
keywords = [l.strip("\n") for l in open("keywords.txt").readlines()]
tlds = [l.strip("\n") for l in open("tlds.txt").readlines()]

# Create a possible combinations of keywords and tlds
for keyword in keywords:
    for tld in tlds:
        domains.append(f"{keyword}.{tld}")


def whois_query(domain: str):
    """
    Sends a WHOIS query to check if a domain is available
    """
    try:
        w = whois.whois(domain)
    except whois.parser.PywhoisError:
        return domain

pool = Pool(2)
available_domains = pool.map_async(whois_query, domains)
pool.close()
pool.join()

with open("output.txt", "w") as f:
    for d in available_domains.get():
        if d is not None:
            f.write(d + os.linesep)
