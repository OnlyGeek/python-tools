#!/usr/bin/python3
#-*- coding:utf-8 -*-


import os
try:
    import configparser
except ImportError:
    import ConfigParser as configparser

import jinja2


NAMES = ["server_ip","inside_ip"]


def render(tpl_path, **kwargs):
    path, filename = os.path.split(tpl_path)
    return jinja2.Environment(
        loader=jinja2.FileSystemLoader(path or '.')
    ).get_template(filename).render(**kwargs)


def parser_vars_into_globals(filename):
    parser = configparser.ConfigParser()
    parser.read(filename)
    

    for name in NAMES:
        globals()[name] = parser.get('UPTIME', name)


def main():
    parser_vars_into_globals('base.cfg')
    with open("hydee_out.xml", 'w') as f:
        f.write(render('hydee.xml', **globals()))


if __name__ == '__main__':
    main()        








