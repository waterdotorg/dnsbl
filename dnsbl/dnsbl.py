#!/usr/bin/env python3

import asyncio
import smtplib

from email.mime.text import MIMEText

from dnsbl.settings import BLACKHOLE_PROVIDERS
from dnsbl.settings_private import EMAIL_FROM, EMAIL_TO


class DNSBLCheck(object):

    def __init__(self, ips=[], blackhole_providers=[], **kwargs):
        self.ips = ips
        self.blackhole_providers = blackhole_providers or BLACKHOLE_PROVIDERS
        self.loop = asyncio.get_event_loop()
        self.ips_blacklisted = {}

    def ip_reversed(self, ip):
        return '.'.join(reversed(ip.split('.')))

    def build_query(self, ip, bp):
        return '{ip_reversed}.{bp}.'.format(ip_reversed=self.ip_reversed(ip),
                                            bp=bp)

    @asyncio.coroutine
    def run_query(self):
        for ip in self.ips:
            for bp in self.blackhole_providers:
                q = self.build_query(ip, bp)
                try:
                    r = yield from self.loop.getaddrinfo(q, 80)
                    if ip in self.ips_blacklisted:
                        self.ips_blacklisted[ip].append(bp)
                    else:
                        self.ips_blacklisted[ip] = [bp]
                except:
                    pass

    def mail_results(self):
        text = ''
        for ip in self.ips_blacklisted:
            text += '{ip}: {bps}\n\n'.format(ip=ip,
                                             bps=self.ips_blacklisted[ip])
        msg = MIMEText(text)
        msg['Subject'] = 'DNSBL Check - {}'.format(len(self.ips_blacklisted))
        msg['From'] = EMAIL_FROM
        msg['To'] = EMAIL_TO

        s = smtplib.SMTP('localhost')
        s.send_message(msg)
        s.quit()

    def run(self):
        self.loop.run_until_complete(self.run_query())
        self.mail_results()
