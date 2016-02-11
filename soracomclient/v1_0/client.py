# Copyright 2016 Yuji Azama
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#     Unless required by applicable law or agreed to in writing, software
#     distributed under the License is distributed on an "AS IS" BASIS,
#     WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#     See the License for the specific language governing permissions and
#     limitations under the License.
#

import time

from soracomclient.v1_0.auth import Auth
from soracomclient.v1_0.credential import Credential
from soracomclient.v1_0.event_handler import EventHandler
from soracomclient.v1_0.group import Group
from soracomclient.v1_0.operator import Operator
from soracomclient.v1_0.stats import Stats
from soracomclient.v1_0.subscriber import Subscriber
from soracomclient.v1_0.user import User


class Client(object):

    status = ""

    def __init__(self, email, password, timeout=86400):
        self.auth = Auth(email=email, password=password, timeout=timeout)
        self.credential = Credential(self.auth)
        self.group = Group(self.auth)
        self.stats = Stats(self.auth)
        self.subscriber = Subscriber(self.auth)
        self.user = User(self.auth)

    def auth(self):
        return Auth(self.auth)

    def list_subscribers(self, tag_name=None, tag_value=None,
                         tag_value_match_mode="exact", status_filter=None,
                         speed_class_filter=None, limit=None,
                         last_evaluated_key=None):
        """List subscribers."""
        status, body = self.subscriber.list_subscribers(
            tag_name=tag_name, tag_value=tag_value,
            tag_value_match_mode=tag_value_match_mode,
            status_filter=status_filter,
            speed_class_filter=speed_class_filter, limit=limit,
            last_evaluated_key=last_evaluated_key)
        return body

    def register_subscriber(self, imsi, registration_secret, group_id=None,
                            tags={}):
        """Register subscriber."""
        status, body = self.subscriber.register(imsi, registration_secret,
                                                group_id, tags)
        return body

    def activate_subscriber(self, imsi):
        """Activate subscriber."""
        status, body = self.subscriber.activate_subscriber(imsi)
        return body

    def deactivate_subscriber(self, imsi):
        """Deactivate subscriber."""
        status, body = self.subscriber.deactivate_subscriber(imsi)
        return body

    def terminate_subscriber(self, imsi):
        """Terminate subscriber"""
        status, body = self.subscriber.terminate_subscriber(imsi)
        return body

    def enable_termination(self, imsi):
        """Enable termination of subscriber."""
        status, body = self.subscriber.enable_termination(imsi)
        return body

    def disable_termination(self, imsi):
        """Disable termination of subscriber."""
        status, body = self.subscriber.disable_termination(imsi)
        return body

    def update_subscriber_tags(self, imsi, tags):
        """Bulk insert or update subscriber tags."""
        status, body = self.subscriber.update_subscriber_tags(imsi, tags)
        return body

    def delete_subscriber_tag(self, imsi, tag_name):
        """Delete subscriber tag."""
        status, body = self.subscriber.delete_subscriber_tag(imsi, tag_name)
        return body

    def update_subscriber_speed_class(self, imsi, speed_class):
        """Update subscriber speed class."""
        status, body = self.subscriber.update_subscriber_speed_class(
            imsi, speed_class)
        return body

    def set_expiry_time(self, imsi, expiry_time):
        """Update expiry time of subscriber."""
        status, body = self.subscriber.set_expiry_time(imsi, expiry_time)
        return body

    def unset_expiry_time(self, imsi):
        """Delete expiry time of subscriber."""
        status, body = self.subscriber.unset_expiry_time(imsi)
        return body

    def set_group(self, imsi, group_id):
        """Set group to subscriber."""
        status, body = self.subscriber.set_group(imsi, group_id)
        return body

    def unset_group(self, imsi):
        """Unset group to subscriber."""
        status, body = self.subscriber.unset_group(imsi)
        return body

    def list_groups(self, group_id=None, tag_name=None, tag_value=None,
                    limit=None, tag_value_match_mode=None,
                    last_evaluated_key=None):
        """List groups."""

        status, body = self.group.list_groups(
            group_id=group_id, tag_name=tag_name,
            tag_value=tag_value, limit=limit,
            tag_value_match_mode=tag_value_match_mode,
            last_evaluated_key=last_evaluated_key)
        return body

    def create_group(self, tags=None):
        """Create group."""
        status, body = self.group.create_group(tags)
        return body

    def delete_group(self, group_id):
        """Delete group."""
        status, body = self.group.delete_group(group_id)
        return body

    def list_subscribers_in_group(self, group_id, limit=None,
                                  last_evaluated_key=None):
        """List subscribers in a group."""
        status, body = self.group.list_subscribers_in_group(
            group_id=group_id, limit=limit,
            last_evaluated_key=last_evaluated_key)
        return body

    def update_group_configuration(self, group_id, namespace, params):
        """Update group configuration parameters."""
        status, body = self.group.update_group_configuration(
            group_id=group_id, namespace=namespace, params=params)
        return body

    def delete_group_configuration(self, group_id, namespace, name):
        """Delete group configuration parameters."""
        status, body = self.group.delete_group_configuration(
            group_id=group_id, namespace=namespace, name=name)
        return body

    def update_group_tags(self, group_id, tags={}):
        """Update group tags."""
        status, body = self.group.update_group_tags(group_id, tags)
        return body

    def delete_group_tags(self, group_id, name):
        """Delete group tag."""
        status, body = self.group.delete_group_tags(group_id, name)
        return body

    def list_event_handlers(self, handler_id=None, target=None, imsi=None):
        """List event handlers."""
        status, body = self.event_handler.list_event_handlers(
            handler_id=handler_id, target=target, imsi=imsi)
        return body

    def create_event_handler(self, request):
        """Create event handler."""
        status, body = self.event_handler.create_event_handler(request)
        return body

    def get_event_handler(self, handler_id):
        """Get event handler."""
        status, body = self.event_handler.get_event_handler(handler_id)
        return body

    def delete_event_handler(self, handler_id):
        """Delete event handler."""
        status, body = self.event_handler.delete_event_handler(handler_id)
        return body

    def update_event_handler(self, handler_id, req):
        """Update event handler."""
        status, body = self.event_handler.update_event_handler(handler_id, req)
        return body

    def get_air_usage(self, imsi,
                      from_unixtime=int(time.time() - 24 * 60 * 60),
                      to_unixtime=int(time.time()), period='minutes'):
        """Get air usage report of subscriber."""
        status, body = self.stats.get_air_usage(
            imsi, from_unixtime=from_unixtime, to_unixtime=to_unixtime,
            period=period)
        return body

    def get_beam_usage(self, imsi,
                       from_unixtime=int(time.time() - 24 * 60 * 60),
                       to_unixtime=int(time.time()), period='minutes'):
        """Get beam usage report of subscriber."""
        status, body = self.stats.get_beam_usage(
            imsi, from_unixtime=from_unixtime, to_unixtime=to_unixtime,
            period=period)
        return body

    def export_air_usage(self, operator_id=None,
                         from_unixtime=int(time.time() - 24 * 60 * 60 * 30),
                         to_unixtime=int(time.time()), period="day"):
        """Export air usage report of all subscribers."""
        if operator_id is None:
            operator_id = self.auth.operator_id
        status, body = self.stats.export_air_usage(operator_id, from_unixtime,
                                                   to_unixtime, period)
        return body

    def export_beam_usage(self, operator_id=None,
                          from_unixtime=int(time.time() - 24 * 60 * 60 * 30),
                          to_unixtime=int(time.time()), period="day"):
        """Export beam usage report of all subscribers."""
        if operator_id is None:
            operator_id = self.auth.operator_id
        status, body = self.stats.export_beam_usage(operator_id, from_unixtime,
                                                    to_unixtime, period)
        return body

    def list_credentials(self):
        """List credentials."""
        status, body = self.credential.list_credentials()
        return body

    def create_credential(self, credentials_id, credentials):
        """Create credential."""
        status, body = self.credential.create_credential(credentials_id,
                                                         credentials)
        return body

    def delete_credential(self, credentials_id):
        """Delete credential."""
        status, body = self.credential.delete_credential(credentials_id)
        return body

    def list_users(self):
        """List users."""
        status, body = self.user.list_users()
        return body

    def delete_user(self, username):
        """Delete user."""
        status, body = self.user.delete_user(username)
        return body

    def get_user(self, username):
        """Get user."""
        status, body = self.user.get_user(username)
        return body

    def create_user(self, username, description=""):
        """Create user."""
        status, body = self.user.create_user(username, description)
        return body

    def update_user(self, username, description=""):
        """Update user."""
        status, body = self.user.update_user(username, description)
        return body

    def list_user_auth_keys(self, username):
        """List user auth keys."""
        status, body = self.user.list_user_auth_keys(username)
        return body

    def generate_user_auth_key(self, username):
        """Generate auth key."""
        status, body = self.user.generate_user_auth_key(username)
        return body

    def delete_user_auth_key(self, username, auth_key_id):
        """Delete user auth key."""
        status, body = self.user.delete_user_auth_key(username, auth_key_id)
        return body

    def get_user_auth_key(self, username, auth_key_id):
        """Get auth key."""
        status, body = self.user.get_user_auth_key(username, auth_key_id)
        return body

    def delete_user_password(self, username):
        """Delete password."""
        status, body = self.user.delete_user_password(username)
        return body

    def has_user_password(self, username):
        """Has user password."""
        status, body = self.user.has_user_password(username)
        return body

    def create_user_password(self, username, password):
        """Create password."""
        status, body = self.user.create_user_password(username, password)
        return body

    def get_user_permission(self, username):
        """Get user permission."""
        status, body = self.user.get_user_permission(username)
        return body

    def update_user_permission(self, username, permission="", description=""):
        """Update permission to user."""
        status, body = self.user.update_user_permission(username, permission,
                                                        description)
        return body
