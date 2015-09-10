from charmhelpers.core import templating, hookenv


MUNIN_NODE_CONF = '/etc/munin/munin-node.conf'
RESTART_MAP = {
    MUNIN_NODE_CONF: ['munin-node'],
    }


def render_munin_node_conf(allowed_cidrs):
    templating.render('munin-node.conf', MUNIN_NODE_CONF,
                      {'allowed_cidrs': allowed_cidrs,
                       'log_level': hookenv.config('log-level'),
                       'log_file': hookenv.config('log-file'),
                       'plugin_timeout': hookenv.config('plugin-timeout')},
                      perms=0o644)
    hookenv.log("%s rendered" % MUNIN_NODE_CONF)


def get_munin_servers(format_as_cidr=True):
    munin_servers = []
    for rid in hookenv.relation_ids("munin"):
        ip = hookenv.relation_get("private-address", rid=rid)
        if format_as_cidr:
            munin_servers.append("%s/32" % ip)
        else:
            munin_servers.append(ip)

    return munin_servers
