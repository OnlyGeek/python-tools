# -*- coding: utf-8 -*-
import os
import time
import json


# This is  for specific log requirment.
TIME_FORMAT = "%d %b %Y:%M:%S"
MSG_FORMAT = "%(now)s - %(category)s - %(data)s\n\n"

if not os.path.exists(/var/log/ansible/hosts):
    os.makedirs("/var/log/ansible/hosts")

def log(host, category, data):
    if type(data) == dict:
        if 'verbose_override' in data:
            data = 'omitted'
        else:
            data = data.copy()
            invocation = data.pop('invocation', None)
            data = json.dumps(data)
            if invocation is not None:
                data = json.dumps(invocation) + " => %s " % data

    path = os.path.join("/var/log/ansible/hosts", host)
    now = time.strftime(TIME_FORMAT, time.localtime())
    with open(path, "a") as f:
        f.write(MSG_FORMAT % dict(now=now, category=category, data=data))

class CallbackModule(object):
    """
    logging the playbook results, per host, in /var/log/ansible/hosts/
    """

    def on_any(self, *args, **kwargs):
        pass

    def runner_on_failed(self, host, res, ignore_errors=False):
        log(host, 'Failed!', res)

    def runner_on_ok(self, host, res):
        log(host, 'Ok', res)

    def runner_on_skipped(self, host, item=None):
        log(host, 'Skipped', '...')

    def runner_on_unreachable(self, host, res):
        log(host, 'Ureachable', res)

    def runner_on_no_hosts(self):
        pass

    def runner_on_async_poll(self, host, res, jid, clock):
        pass

    def runner_on_async_ok(self, host, res, jid):
        pass

    def runner_on_async_failed(self, host, res, jid):
        log(host, 'Async_failed!', res)

    def playbook_on_start(self):
        pass

    def playbook_on_notify(self, host, handler):
        pass

    def playbook_on_hosts_matched(self):
        pass

    def playbook_on_no_hosts_remaining(self):
        pass

    def playbook_on_task_start(self, name, is_conditional):
        pass

    def playbook_on_vars_prompt(self, varname, private=True,
        prompt=None, encrypt=None, confirm=False, salt_size=None,
        salt=None, default=None):
        pass

    def playbook_on_vars_setup(self):
        pass

    def playbook_on_import_for_host(self, host, imported_file):
        log(host, 'Imported', imported_file)

    def playbook_on_not_import_for_host(self, host, missing_file):
        log(host, 'Notimported', missing_file)

    def playbook_on_play_start(self, name):
        pass

    def playbook_on_stats(self, stats):
        pass

    

    












