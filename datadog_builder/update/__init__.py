# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import logging

from datadog_builder import common
from datadog_builder.update import monitors

LOG = logging.getLogger(__name__)


def add_arguments(subparsers):
    parser = common.create_subcommand(subparsers,
                                      'update',
                                      update_command,
                                      help='Update datadog monitors')

    parser.add_argument('-n', '--dry-run',
                        action='store_true',
                        dest='dry_run',
                        help="Don't perform commands just test")

    parser.add_argument('--no-delete',
                        action='store_false',
                        dest='delete',
                        help="Don't delete unknown monitors")


def update_command(args):
    common.initialize(args)
    config = common.load_config(args)

    monitors.update_monitors(args, config)
