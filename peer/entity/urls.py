# Copyright 2011 Terena. All rights reserved.

# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:

#    1. Redistributions of source code must retain the above copyright notice,
#       this list of conditions and the following disclaimer.

#    2. Redistributions in binary form must reproduce the above copyright notice,
#       this list of conditions and the following disclaimer in the documentation
#        and/or other materials provided with the distribution.

# THIS SOFTWARE IS PROVIDED BY TERENA ``AS IS'' AND ANY EXPRESS OR IMPLIED
# WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO
# EVENT SHALL TERENA OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
# PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
# LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE
# OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF
# ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

# The views and conclusions contained in the software and documentation are those
# of the authors and should not be interpreted as representing official policies,
# either expressed or implied, of Terena.

from django.conf.urls.defaults import patterns, url

from peer.entity.feeds import EntitiesFeed, ChangesFeed

urlpatterns = patterns(
    'peer.entity.views',
    url(r'^$', 'entities_list', name='entities_list'),
    url(r'^rss$', EntitiesFeed(), name='entities_feed'),
    url(r'^add$', 'entity_add', name='entity_add'),
    url(r'^(?P<domain_name>\w.+)/add$', 'entity_add_with_domain',
        name='entity_add_with_domain'),
    url(r'^search$', 'search_entities', name='search_entities'),
    url(r'^pygments.css$', 'get_pygments_css', name='get_pygments_css'),
    url(r'^(?P<entity_id>\d+)$', 'entity_view', name='entity_view'),
    url(r'^(?P<entity_id>\d+)/remove/$', 'entity_remove', name='entity_remove'),
    url(r'^(?P<entity_id>\d+)/edit/$', 'entity_edit', name='entity_edit'),
    url(r'^(?P<entity_id>\d+)/edit_metadata/$', 'edit_metadata', name='edit_metadata'),
    url(r'^(?P<entity_id>\d+)/text_edit_metadata/$', 'text_edit_metadata', name='text_edit_metadata'),
    url(r'^(?P<entity_id>\d+)/file_edit_metadata/$', 'file_edit_metadata', name='file_edit_metadata'),
    url(r'^(?P<entity_id>\d+)/remote_edit_metadata/$', 'remote_edit_metadata', name='remote_edit_metadata'),
    url(r'^(?P<entity_id>\d+)/sharing/$', 'sharing', name='sharing'),
    url(r'^(?P<entity_id>\d+)/list_delegates/$', 'list_delegates', name='list_delegates'),
    url(r'^(?P<entity_id>\d+)/make_owner/$', 'make_owner', name='make_owner'),
    url(r'^(?P<entity_id>\d+)/remove_delegate/(?P<user_id>\d+)$', 'remove_delegate', name='remove_delegate'),
    url(r'^(?P<entity_id>\d+)/add_delegate/(?P<username>\w+)$', 'add_delegate', name='add_delegate'),
    url(r'^(?P<entity_id>\d+)/get_diff/(?P<r1>\w+)/(?P<r2>\w+)$', 'get_diff', name='get_diff'),
    url(r'^(?P<entity_id>\d+)/get_revision/(?P<rev>\w+)$', 'get_revision', name='get_revision'),
    url(r'^(?P<entity_id>\d+)/latest_metadata/$', 'get_latest_metadata',
        name='get_latest_metadata'),
    url(r'^(?P<entity_id>\d+)/rss$', ChangesFeed(), name='changes_feed'),
)
