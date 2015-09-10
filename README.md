# Overview

This charm provides [munin-node](http://munin-monitoring.org/).

# Usage

You can deploy munin-node and relate it to any container with:

    juju deploy ubuntu
    juju deploy munin-node
    juju deploy munin
    juju add-relation munin-node ubuntu
    juju add-relation munin-node munin

# Configuration

Standard configuration options are provided, munin-node package installation
will enable all the suggested plugins by `munin-node-configure`
