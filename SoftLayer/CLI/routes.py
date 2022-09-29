"""
    SoftLayer.CLI.routes
    ~~~~~~~~~~~~~~~~~~~~~
    This is how all commands are registered with the CLI.

    :license: MIT, see LICENSE for more details.
"""

ALL_ROUTES = [
    ('shell', 'SoftLayer.shell.core:cli'),

    ('call-api', 'SoftLayer.CLI.call_api:cli'),

    ('account', 'SoftLayer.CLI.account'),
    ('account:invoice-detail', 'SoftLayer.CLI.account.invoice_detail:cli'),
    ('account:invoices', 'SoftLayer.CLI.account.invoices:cli'),
    ('account:events', 'SoftLayer.CLI.account.events:cli'),
    ('account:bandwidth-pools-detail', 'SoftLayer.CLI.account.bandwidth_pools_detail:cli'),
    ('account:event-detail', 'SoftLayer.CLI.account.event_detail:cli'),
    ('account:licenses', 'SoftLayer.CLI.account.licenses:cli'),
    ('account:summary', 'SoftLayer.CLI.account.summary:cli'),
    ('account:billing-items', 'SoftLayer.CLI.account.billing_items:cli'),
    ('account:item-detail', 'SoftLayer.CLI.account.item_detail:cli'),
    ('account:cancel-item', 'SoftLayer.CLI.account.cancel_item:cli'),
    ('account:orders', 'SoftLayer.CLI.account.orders:cli'),
    ('account:bandwidth-pools', 'SoftLayer.CLI.account.bandwidth_pools:cli'),

    ('virtual', 'SoftLayer.CLI.virt'),
    ('virtual:bandwidth', 'SoftLayer.CLI.virt.bandwidth:cli'),
    ('virtual:billing', 'SoftLayer.CLI.virt.billing:cli'),
    ('virtual:cancel', 'SoftLayer.CLI.virt.cancel:cli'),
    ('virtual:capture', 'SoftLayer.CLI.virt.capture:cli'),
    ('virtual:create', 'SoftLayer.CLI.virt.create:cli'),
    ('virtual:create-options', 'SoftLayer.CLI.virt.create_options:cli'),
    ('virtual:detail', 'SoftLayer.CLI.virt.detail:cli'),
    ('virtual:dns-sync', 'SoftLayer.CLI.virt.dns:cli'),
    ('virtual:edit', 'SoftLayer.CLI.virt.edit:cli'),
    ('virtual:list', 'SoftLayer.CLI.virt.list:cli'),
    ('virtual:pause', 'SoftLayer.CLI.virt.power:pause'),
    ('virtual:power-off', 'SoftLayer.CLI.virt.power:power_off'),
    ('virtual:power-on', 'SoftLayer.CLI.virt.power:power_on'),
    ('virtual:rescue', 'SoftLayer.CLI.virt.power:rescue'),
    ('virtual:resume', 'SoftLayer.CLI.virt.power:resume'),
    ('virtual:ready', 'SoftLayer.CLI.virt.ready:cli'),
    ('virtual:reboot', 'SoftLayer.CLI.virt.power:reboot'),
    ('virtual:reload', 'SoftLayer.CLI.virt.reload:cli'),
    ('virtual:storage', 'SoftLayer.CLI.virt.storage:cli'),
    ('virtual:upgrade', 'SoftLayer.CLI.virt.upgrade:cli'),
    ('virtual:usage', 'SoftLayer.CLI.virt.usage:cli'),
    ('virtual:credentials', 'SoftLayer.CLI.virt.credentials:cli'),
    ('virtual:authorize-storage', 'SoftLayer.CLI.virt.authorize_storage:cli'),
    ('virtual:capacity', 'SoftLayer.CLI.virt.capacity:cli'),
    ('virtual:placementgroup', 'SoftLayer.CLI.virt.placementgroup:cli'),
    ('virtual:migrate', 'SoftLayer.CLI.virt.migrate:cli'),
    ('virtual:access', 'SoftLayer.CLI.virt.access:cli'),
    ('virtual:monitoring', 'SoftLayer.CLI.virt.monitoring:cli'),
    ('virtual:notifications', 'SoftLayer.CLI.virt.notifications:cli'),
    ('virtual:add-notification', 'SoftLayer.CLI.virt.add_notification:cli'),

    ('dedicatedhost', 'SoftLayer.CLI.dedicatedhost'),
    ('dedicatedhost:list', 'SoftLayer.CLI.dedicatedhost.list:cli'),
    ('dedicatedhost:create', 'SoftLayer.CLI.dedicatedhost.create:cli'),
    ('dedicatedhost:create-options', 'SoftLayer.CLI.dedicatedhost.create_options:cli'),
    ('dedicatedhost:detail', 'SoftLayer.CLI.dedicatedhost.detail:cli'),
    ('dedicatedhost:cancel', 'SoftLayer.CLI.dedicatedhost.cancel:cli'),
    ('dedicatedhost:cancel-guests', 'SoftLayer.CLI.dedicatedhost.cancel_guests:cli'),
    ('dedicatedhost:list-guests', 'SoftLayer.CLI.dedicatedhost.list_guests:cli'),

    ('cdn', 'SoftLayer.CLI.cdn'),
    ('cdn:detail', 'SoftLayer.CLI.cdn.detail:cli'),
    ('cdn:edit', 'SoftLayer.CLI.cdn.edit:cli'),
    ('cdn:list', 'SoftLayer.CLI.cdn.list:cli'),
    ('cdn:origin-add', 'SoftLayer.CLI.cdn.origin_add:cli'),
    ('cdn:origin-list', 'SoftLayer.CLI.cdn.origin_list:cli'),
    ('cdn:origin-remove', 'SoftLayer.CLI.cdn.origin_remove:cli'),
    ('cdn:purge', 'SoftLayer.CLI.cdn.purge:cli'),

    ('config', 'SoftLayer.CLI.config'),
    ('config:setup', 'SoftLayer.CLI.config.setup:cli'),
    ('config:show', 'SoftLayer.CLI.config.show:cli'),
    ('setup', 'SoftLayer.CLI.config.setup:cli'),

    ('dns', 'SoftLayer.CLI.dns'),
    ('dns:import', 'SoftLayer.CLI.dns.zone_import:cli'),
    ('dns:record-add', 'SoftLayer.CLI.dns.record_add:cli'),
    ('dns:record-edit', 'SoftLayer.CLI.dns.record_edit:cli'),
    ('dns:record-list', 'SoftLayer.CLI.dns.record_list:cli'),
    ('dns:record-remove', 'SoftLayer.CLI.dns.record_remove:cli'),
    ('dns:zone-create', 'SoftLayer.CLI.dns.zone_create:cli'),
    ('dns:zone-delete', 'SoftLayer.CLI.dns.zone_delete:cli'),
    ('dns:zone-list', 'SoftLayer.CLI.dns.zone_list:cli'),
    ('dns:zone-print', 'SoftLayer.CLI.dns.zone_print:cli'),

    ('block', 'SoftLayer.CLI.block'),
    ('block:access-authorize', 'SoftLayer.CLI.block.access.authorize:cli'),
    ('block:access-list', 'SoftLayer.CLI.block.access.list:cli'),
    ('block:access-revoke', 'SoftLayer.CLI.block.access.revoke:cli'),
    ('block:access-password', 'SoftLayer.CLI.block.access.password:cli'),
    ('block:duplicate-convert-status', 'SoftLayer.CLI.block.duplicate_convert_status:cli'),
    ('block:subnets-list', 'SoftLayer.CLI.block.subnets.list:cli'),
    ('block:subnets-assign', 'SoftLayer.CLI.block.subnets.assign:cli'),
    ('block:subnets-remove', 'SoftLayer.CLI.block.subnets.remove:cli'),
    ('block:replica-failback', 'SoftLayer.CLI.block.replication.failback:cli'),
    ('block:replica-failover', 'SoftLayer.CLI.block.replication.failover:cli'),
    ('block:disaster-recovery-failover', 'SoftLayer.CLI.block.replication.disaster_recovery_failover:cli'),
    ('block:replica-order', 'SoftLayer.CLI.block.replication.order:cli'),
    ('block:replica-partners', 'SoftLayer.CLI.block.replication.partners:cli'),
    ('block:replica-locations', 'SoftLayer.CLI.block.replication.locations:cli'),
    ('block:snapshot-cancel', 'SoftLayer.CLI.block.snapshot.cancel:cli'),
    ('block:snapshot-create', 'SoftLayer.CLI.block.snapshot.create:cli'),
    ('block:snapshot-delete', 'SoftLayer.CLI.block.snapshot.delete:cli'),
    ('block:snapshot-disable', 'SoftLayer.CLI.block.snapshot.disable:cli'),
    ('block:snapshot-set-notification', 'SoftLayer.CLI.block.snapshot.set_notify_status:cli'),
    ('block:snapshot-get-notification-status', 'SoftLayer.CLI.block.snapshot.get_notify_status:cli'),
    ('block:snapshot-enable', 'SoftLayer.CLI.block.snapshot.enable:cli'),
    ('block:snapshot-schedule-list', 'SoftLayer.CLI.block.snapshot.schedule_list:cli'),
    ('block:snapshot-list', 'SoftLayer.CLI.block.snapshot.list:cli'),
    ('block:snapshot-order', 'SoftLayer.CLI.block.snapshot.order:cli'),
    ('block:snapshot-restore', 'SoftLayer.CLI.block.snapshot.restore:cli'),
    ('block:volume-cancel', 'SoftLayer.CLI.block.cancel:cli'),
    ('block:volume-count', 'SoftLayer.CLI.block.count:cli'),
    ('block:volume-detail', 'SoftLayer.CLI.block.detail:cli'),
    ('block:volume-duplicate', 'SoftLayer.CLI.block.duplicate:cli'),
    ('block:volume-list', 'SoftLayer.CLI.block.list:cli'),
    ('block:volume-modify', 'SoftLayer.CLI.block.modify:cli'),
    ('block:volume-order', 'SoftLayer.CLI.block.order:cli'),
    ('block:volume-set-lun-id', 'SoftLayer.CLI.block.lun:cli'),
    ('block:volume-limits', 'SoftLayer.CLI.block.limit:cli'),
    ('block:volume-refresh', 'SoftLayer.CLI.block.refresh:cli'),
    ('block:volume-convert', 'SoftLayer.CLI.block.convert:cli'),
    ('block:volume-options', 'SoftLayer.CLI.block.options:cli'),
    ('block:volume-set-note', 'SoftLayer.CLI.block.set_note:cli'),
    ('block:object-list', 'SoftLayer.CLI.block.object_list:cli'),
    ('block:object-storage-detail', 'SoftLayer.CLI.block.object_storage_detail:cli'),
    ('block:object-storage-permission', 'SoftLayer.CLI.block.object_storage_permission:cli'),

    ('email', 'SoftLayer.CLI.email'),
    ('email:list', 'SoftLayer.CLI.email.list:cli'),
    ('email:detail', 'SoftLayer.CLI.email.detail:cli'),
    ('email:edit', 'SoftLayer.CLI.email.edit:cli'),

    ('licenses', 'SoftLayer.CLI.licenses'),
    ('licenses:create-options', 'SoftLayer.CLI.licenses.create_options:cli'),

    ('event-log', 'SoftLayer.CLI.event_log'),
    ('event-log:get', 'SoftLayer.CLI.event_log.get:cli'),
    ('event-log:types', 'SoftLayer.CLI.event_log.types:cli'),

    ('file', 'SoftLayer.CLI.file'),
    ('file:access-authorize', 'SoftLayer.CLI.file.access.authorize:cli'),
    ('file:access-list', 'SoftLayer.CLI.file.access.list:cli'),
    ('file:access-revoke', 'SoftLayer.CLI.file.access.revoke:cli'),
    ('file:duplicate-convert-status', 'SoftLayer.CLI.file.duplicate_convert_status:cli'),
    ('file:replica-failback', 'SoftLayer.CLI.file.replication.failback:cli'),
    ('file:replica-failover', 'SoftLayer.CLI.file.replication.failover:cli'),
    ('file:disaster-recovery-failover', 'SoftLayer.CLI.file.replication.disaster_recovery_failover:cli'),
    ('file:replica-order', 'SoftLayer.CLI.file.replication.order:cli'),
    ('file:replica-partners', 'SoftLayer.CLI.file.replication.partners:cli'),
    ('file:replica-locations', 'SoftLayer.CLI.file.replication.locations:cli'),
    ('file:snapshot-cancel', 'SoftLayer.CLI.file.snapshot.cancel:cli'),
    ('file:snapshot-create', 'SoftLayer.CLI.file.snapshot.create:cli'),
    ('file:snapshot-delete', 'SoftLayer.CLI.file.snapshot.delete:cli'),
    ('file:snapshot-disable', 'SoftLayer.CLI.file.snapshot.disable:cli'),
    ('file:snapshot-enable', 'SoftLayer.CLI.file.snapshot.enable:cli'),
    ('file:snapshot-set-notification', 'SoftLayer.CLI.file.snapshot.set_notify_status:cli'),
    ('file:snapshot-get-notification-status', 'SoftLayer.CLI.file.snapshot.get_notify_status:cli'),
    ('file:snapshot-schedule-list', 'SoftLayer.CLI.file.snapshot.schedule_list:cli'),
    ('file:snapshot-list', 'SoftLayer.CLI.file.snapshot.list:cli'),
    ('file:snapshot-order', 'SoftLayer.CLI.file.snapshot.order:cli'),
    ('file:snapshot-restore', 'SoftLayer.CLI.file.snapshot.restore:cli'),
    ('file:volume-cancel', 'SoftLayer.CLI.file.cancel:cli'),
    ('file:volume-count', 'SoftLayer.CLI.file.count:cli'),
    ('file:volume-detail', 'SoftLayer.CLI.file.detail:cli'),
    ('file:volume-duplicate', 'SoftLayer.CLI.file.duplicate:cli'),
    ('file:volume-list', 'SoftLayer.CLI.file.list:cli'),
    ('file:volume-modify', 'SoftLayer.CLI.file.modify:cli'),
    ('file:volume-order', 'SoftLayer.CLI.file.order:cli'),
    ('file:volume-limits', 'SoftLayer.CLI.file.limit:cli'),
    ('file:volume-refresh', 'SoftLayer.CLI.file.refresh:cli'),
    ('file:volume-convert', 'SoftLayer.CLI.file.convert:cli'),
    ('file:volume-options', 'SoftLayer.CLI.file.options:cli'),
    ('file:volume-set-note', 'SoftLayer.CLI.file.set_note:cli'),

    ('firewall', 'SoftLayer.CLI.firewall'),
    ('firewall:add', 'SoftLayer.CLI.firewall.add:cli'),
    ('firewall:cancel', 'SoftLayer.CLI.firewall.cancel:cli'),
    ('firewall:detail', 'SoftLayer.CLI.firewall.detail:cli'),
    ('firewall:edit', 'SoftLayer.CLI.firewall.edit:cli'),
    ('firewall:list', 'SoftLayer.CLI.firewall.list:cli'),
    ('firewall:monitoring', 'SoftLayer.CLI.firewall.monitoring:cli'),

    ('globalip', 'SoftLayer.CLI.globalip'),
    ('globalip:assign', 'SoftLayer.CLI.globalip.assign:cli'),
    ('globalip:cancel', 'SoftLayer.CLI.globalip.cancel:cli'),
    ('globalip:create', 'SoftLayer.CLI.globalip.create:cli'),
    ('globalip:list', 'SoftLayer.CLI.globalip.list:cli'),
    ('globalip:unassign', 'SoftLayer.CLI.globalip.unassign:cli'),

    ('image', 'SoftLayer.CLI.image'),
    ('image:delete', 'SoftLayer.CLI.image.delete:cli'),
    ('image:detail', 'SoftLayer.CLI.image.detail:cli'),
    ('image:edit', 'SoftLayer.CLI.image.edit:cli'),
    ('image:list', 'SoftLayer.CLI.image.list:cli'),
    ('image:import', 'SoftLayer.CLI.image.import:cli'),
    ('image:export', 'SoftLayer.CLI.image.export:cli'),
    ('image:datacenter', 'SoftLayer.CLI.image.datacenter:cli'),

    ('ipsec', 'SoftLayer.CLI.vpn.ipsec'),
    ('ipsec:configure', 'SoftLayer.CLI.vpn.ipsec.configure:cli'),
    ('ipsec:detail', 'SoftLayer.CLI.vpn.ipsec.detail:cli'),
    ('ipsec:list', 'SoftLayer.CLI.vpn.ipsec.list:cli'),
    ('ipsec:subnet-add', 'SoftLayer.CLI.vpn.ipsec.subnet.add:cli'),
    ('ipsec:subnet-remove', 'SoftLayer.CLI.vpn.ipsec.subnet.remove:cli'),
    ('ipsec:translation-add', 'SoftLayer.CLI.vpn.ipsec.translation.add:cli'),
    ('ipsec:translation-remove', 'SoftLayer.CLI.vpn.ipsec.translation.remove:cli'),
    ('ipsec:translation-update', 'SoftLayer.CLI.vpn.ipsec.translation.update:cli'),
    ('ipsec:update', 'SoftLayer.CLI.vpn.ipsec.update:cli'),
    ('ipsec:order', 'SoftLayer.CLI.vpn.ipsec.order:cli'),
    ('ipsec:cancel', 'SoftLayer.CLI.vpn.ipsec.cancel:cli'),

    ('loadbal', 'SoftLayer.CLI.loadbal'),
    ('loadbal:detail', 'SoftLayer.CLI.loadbal.detail:cli'),
    ('loadbal:list', 'SoftLayer.CLI.loadbal.list:cli'),
    ('loadbal:health', 'SoftLayer.CLI.loadbal.health:cli'),
    ('loadbal:member-add', 'SoftLayer.CLI.loadbal.members:add'),
    ('loadbal:member-del', 'SoftLayer.CLI.loadbal.members:remove'),
    ('loadbal:l7policies', 'SoftLayer.CLI.loadbal.layer7_policy_list:policies'),
    ('loadbal:pool-add', 'SoftLayer.CLI.loadbal.pools:add'),
    ('loadbal:pool-edit', 'SoftLayer.CLI.loadbal.pools:edit'),
    ('loadbal:pool-del', 'SoftLayer.CLI.loadbal.pools:delete'),
    ('loadbal:l7pool-add', 'SoftLayer.CLI.loadbal.pools:l7pool_add'),
    ('loadbal:l7pool-del', 'SoftLayer.CLI.loadbal.pools:l7pool_del'),
    ('loadbal:order', 'SoftLayer.CLI.loadbal.order:order'),
    ('loadbal:order-options', 'SoftLayer.CLI.loadbal.order:order_options'),
    ('loadbal:cancel', 'SoftLayer.CLI.loadbal.order:cancel'),

    ('loadbal:ns-detail', 'SoftLayer.CLI.loadbal.ns_detail:cli'),
    ('loadbal:ns-list', 'SoftLayer.CLI.loadbal.ns_list:cli'),

    ('metadata', 'SoftLayer.CLI.metadata:cli'),

    ('nas', 'SoftLayer.CLI.nas'),
    ('nas:list', 'SoftLayer.CLI.nas.list:cli'),
    ('nas:credentials', 'SoftLayer.CLI.nas.credentials:cli'),

    ('licenses', 'SoftLayer.CLI.licenses'),
    ('licenses:create', 'SoftLayer.CLI.licenses.create:cli'),
    ('licenses:cancel', 'SoftLayer.CLI.licenses.cancel:cli'),

    ('object-storage', 'SoftLayer.CLI.object_storage'),

    ('object-storage:accounts', 'SoftLayer.CLI.object_storage.list_accounts:cli'),
    ('object-storage:endpoints', 'SoftLayer.CLI.object_storage.list_endpoints:cli'),
    ('object-storage:credential', 'SoftLayer.CLI.object_storage.credential:cli'),

    ('order', 'SoftLayer.CLI.order'),
    ('order:category-list', 'SoftLayer.CLI.order.category_list:cli'),
    ('order:item-list', 'SoftLayer.CLI.order.item_list:cli'),
    ('order:package-list', 'SoftLayer.CLI.order.package_list:cli'),
    ('order:place', 'SoftLayer.CLI.order.place:cli'),
    ('order:preset-list', 'SoftLayer.CLI.order.preset_list:cli'),
    ('order:package-locations', 'SoftLayer.CLI.order.package_locations:cli'),
    ('order:place-quote', 'SoftLayer.CLI.order.place_quote:cli'),
    ('order:quote-list', 'SoftLayer.CLI.order.quote_list:cli'),
    ('order:quote-detail', 'SoftLayer.CLI.order.quote_detail:cli'),
    ('order:quote-save', 'SoftLayer.CLI.order.quote_save:cli'),
    ('order:quote', 'SoftLayer.CLI.order.quote:cli'),
    ('order:lookup', 'SoftLayer.CLI.order.lookup:cli'),

    ('hardware', 'SoftLayer.CLI.hardware'),
    ('hardware:bandwidth', 'SoftLayer.CLI.hardware.bandwidth:cli'),
    ('hardware:cancel', 'SoftLayer.CLI.hardware.cancel:cli'),
    ('hardware:cancel-reasons', 'SoftLayer.CLI.hardware.cancel_reasons:cli'),
    ('hardware:create', 'SoftLayer.CLI.hardware.create:cli'),
    ('hardware:create-options', 'SoftLayer.CLI.hardware.create_options:cli'),
    ('hardware:detail', 'SoftLayer.CLI.hardware.detail:cli'),
    ('hardware:billing', 'SoftLayer.CLI.hardware.billing:cli'),
    ('hardware:edit', 'SoftLayer.CLI.hardware.edit:cli'),
    ('hardware:list', 'SoftLayer.CLI.hardware.list:cli'),
    ('hardware:power-cycle', 'SoftLayer.CLI.hardware.power:power_cycle'),
    ('hardware:power-off', 'SoftLayer.CLI.hardware.power:power_off'),
    ('hardware:power-on', 'SoftLayer.CLI.hardware.power:power_on'),
    ('hardware:reboot', 'SoftLayer.CLI.hardware.power:reboot'),
    ('hardware:reload', 'SoftLayer.CLI.hardware.reload:cli'),
    ('hardware:credentials', 'SoftLayer.CLI.hardware.credentials:cli'),
    ('hardware:update-firmware', 'SoftLayer.CLI.hardware.update_firmware:cli'),
    ('hardware:reflash-firmware', 'SoftLayer.CLI.hardware.reflash_firmware:cli'),
    ('hardware:rescue', 'SoftLayer.CLI.hardware.power:rescue'),
    ('hardware:ready', 'SoftLayer.CLI.hardware.ready:cli'),
    ('hardware:toggle-ipmi', 'SoftLayer.CLI.hardware.toggle_ipmi:cli'),
    ('hardware:authorize-storage', 'SoftLayer.CLI.hardware.authorize_storage:cli'),
    ('hardware:dns-sync', 'SoftLayer.CLI.hardware.dns:cli'),
    ('hardware:storage', 'SoftLayer.CLI.hardware.storage:cli'),
    ('hardware:upgrade', 'SoftLayer.CLI.hardware.upgrade:cli'),
    ('hardware:sensor', 'SoftLayer.CLI.hardware.sensor:cli'),
    ('hardware:monitoring', 'SoftLayer.CLI.hardware.monitoring:cli'),
    ('hardware:notifications', 'SoftLayer.CLI.hardware.notifications:cli'),
    ('hardware:add-notification', 'SoftLayer.CLI.hardware.add_notification:cli'),

    ('securitygroup', 'SoftLayer.CLI.securitygroup'),
    ('securitygroup:list', 'SoftLayer.CLI.securitygroup.list:cli'),
    ('securitygroup:detail', 'SoftLayer.CLI.securitygroup.detail:cli'),
    ('securitygroup:create', 'SoftLayer.CLI.securitygroup.create:cli'),
    ('securitygroup:edit', 'SoftLayer.CLI.securitygroup.edit:cli'),
    ('securitygroup:delete', 'SoftLayer.CLI.securitygroup.delete:cli'),
    ('securitygroup:rule-list', 'SoftLayer.CLI.securitygroup.rule:rule_list'),
    ('securitygroup:rule-add', 'SoftLayer.CLI.securitygroup.rule:add'),
    ('securitygroup:rule-edit', 'SoftLayer.CLI.securitygroup.rule:edit'),
    ('securitygroup:rule-remove', 'SoftLayer.CLI.securitygroup.rule:remove'),
    ('securitygroup:interface-list',
     'SoftLayer.CLI.securitygroup.interface:interface_list'),
    ('securitygroup:interface-add',
     'SoftLayer.CLI.securitygroup.interface:add'),
    ('securitygroup:interface-remove',
     'SoftLayer.CLI.securitygroup.interface:remove'),
    ('securitygroup:event-log', 'SoftLayer.CLI.securitygroup.event_log:get_by_request_id'),

    ('sshkey', 'SoftLayer.CLI.sshkey'),
    ('sshkey:add', 'SoftLayer.CLI.sshkey.add:cli'),
    ('sshkey:remove', 'SoftLayer.CLI.sshkey.remove:cli'),
    ('sshkey:edit', 'SoftLayer.CLI.sshkey.edit:cli'),
    ('sshkey:list', 'SoftLayer.CLI.sshkey.list:cli'),
    ('sshkey:print', 'SoftLayer.CLI.sshkey.print:cli'),

    ('ssl', 'SoftLayer.CLI.ssl'),
    ('ssl:add', 'SoftLayer.CLI.ssl.add:cli'),
    ('ssl:download', 'SoftLayer.CLI.ssl.download:cli'),
    ('ssl:edit', 'SoftLayer.CLI.ssl.edit:cli'),
    ('ssl:list', 'SoftLayer.CLI.ssl.list:cli'),
    ('ssl:remove', 'SoftLayer.CLI.ssl.remove:cli'),

    ('subnet', 'SoftLayer.CLI.subnet'),
    ('subnet:cancel', 'SoftLayer.CLI.subnet.cancel:cli'),
    ('subnet:create', 'SoftLayer.CLI.subnet.create:cli'),
    ('subnet:edit', 'SoftLayer.CLI.subnet.edit:cli'),
    ('subnet:detail', 'SoftLayer.CLI.subnet.detail:cli'),
    ('subnet:list', 'SoftLayer.CLI.subnet.list:cli'),
    ('subnet:lookup', 'SoftLayer.CLI.subnet.lookup:cli'),
    ('subnet:edit-ip', 'SoftLayer.CLI.subnet.edit_ip:cli'),
    ('subnet:route', 'SoftLayer.CLI.subnet.route:cli'),
    ('subnet:clear-route', 'SoftLayer.CLI.subnet.clear_route:cli'),

    ('tags', 'SoftLayer.CLI.tags'),
    ('tags:cleanup', 'SoftLayer.CLI.tags.cleanup:cli'),
    ('tags:list', 'SoftLayer.CLI.tags.list:cli'),
    ('tags:set', 'SoftLayer.CLI.tags.set:cli'),
    ('tags:details', 'SoftLayer.CLI.tags.details:cli'),
    ('tags:delete', 'SoftLayer.CLI.tags.delete:cli'),
    ('tags:taggable', 'SoftLayer.CLI.tags.taggable:cli'),

    ('ticket', 'SoftLayer.CLI.ticket'),
    ('ticket:create', 'SoftLayer.CLI.ticket.create:cli'),
    ('ticket:detail', 'SoftLayer.CLI.ticket.detail:cli'),
    ('ticket:list', 'SoftLayer.CLI.ticket.list:cli'),
    ('ticket:update', 'SoftLayer.CLI.ticket.update:cli'),
    ('ticket:upload', 'SoftLayer.CLI.ticket.upload:cli'),
    ('ticket:subjects', 'SoftLayer.CLI.ticket.subjects:cli'),
    ('ticket:summary', 'SoftLayer.CLI.ticket.summary:cli'),
    ('ticket:attach', 'SoftLayer.CLI.ticket.attach:cli'),
    ('ticket:detach', 'SoftLayer.CLI.ticket.detach:cli'),

    ('user', 'SoftLayer.CLI.user'),
    ('user:list', 'SoftLayer.CLI.user.list:cli'),
    ('user:detail', 'SoftLayer.CLI.user.detail:cli'),
    ('user:permissions', 'SoftLayer.CLI.user.permissions:cli'),
    ('user:edit-permissions', 'SoftLayer.CLI.user.edit_permissions:cli'),
    ('user:notifications', 'SoftLayer.CLI.user.notifications:cli'),
    ('user:edit-notifications', 'SoftLayer.CLI.user.edit_notifications:cli'),
    ('user:edit-details', 'SoftLayer.CLI.user.edit_details:cli'),
    ('user:create', 'SoftLayer.CLI.user.create:cli'),
    ('user:delete', 'SoftLayer.CLI.user.delete:cli'),
    ('user:device-access', 'SoftLayer.CLI.user.device_access:cli'),
    ('user:vpn-manual', 'SoftLayer.CLI.user.vpn_manual:cli'),
    ('user:vpn-subnet', 'SoftLayer.CLI.user.vpn_subnet:cli'),
    ('user:remove-access', 'SoftLayer.CLI.user.remove_access:cli'),

    ('vlan', 'SoftLayer.CLI.vlan'),
    ('vlan:create', 'SoftLayer.CLI.vlan.create:cli'),
    ('vlan:create-options', 'SoftLayer.CLI.vlan.create_options:cli'),
    ('vlan:detail', 'SoftLayer.CLI.vlan.detail:cli'),
    ('vlan:edit', 'SoftLayer.CLI.vlan.edit:cli'),
    ('vlan:list', 'SoftLayer.CLI.vlan.list:cli'),
    ('vlan:cancel', 'SoftLayer.CLI.vlan.cancel:cli'),

    ('summary', 'SoftLayer.CLI.summary:cli'),

    ('report', 'SoftLayer.CLI.report'),
    ('report:bandwidth', 'SoftLayer.CLI.report.bandwidth:cli'),
    ('report:datacenter-closures', 'SoftLayer.CLI.report.dc_closures:cli'),

    ('autoscale', 'SoftLayer.CLI.autoscale'),
    ('autoscale:list', 'SoftLayer.CLI.autoscale.list:cli'),
    ('autoscale:detail', 'SoftLayer.CLI.autoscale.detail:cli'),
    ('autoscale:delete', 'SoftLayer.CLI.autoscale.delete:cli'),
]

ALL_ALIASES = {
    'hw': 'hardware',
    'lb': 'loadbal',
    'meta': 'metadata',
    'my': 'metadata',
    'sg': 'securitygroup',
    'server': 'hardware',
    'vm': 'virtual',
    'vs': 'virtual',
    'dh': 'dedicatedhost',
    'pg': 'placementgroup',
}
