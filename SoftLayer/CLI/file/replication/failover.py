"""Failover to a replicant volume."""
# :license: MIT, see LICENSE for more details.

import click
import SoftLayer
from SoftLayer.CLI import environment


@click.command(cls=SoftLayer.CLI.command.SLCommand, )
@click.argument('volume-id')
@click.option('--replicant-id', help="ID of the replicant volume")
@environment.pass_env
def cli(env, volume_id, replicant_id):
    """Failover a file volume to the given replicant volume."""
    file_storage_manager = SoftLayer.FileStorageManager(env.client)

    success = file_storage_manager.failover_to_replicant(
        volume_id,
        replicant_id
    )

    if success:
        click.echo("Failover to replicant is now in progress.")
    else:
        click.echo("Failover operation could not be initiated.")
