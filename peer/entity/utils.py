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

from django.conf import settings

NAMESPACES = {
    'md': 'urn:oasis:names:tc:SAML:2.0:metadata',
    'mdui': 'urn:oasis:names:tc:SAML:metadata:ui',
    'ds': 'http://www.w3.org/2000/09/xmldsig#',
    'xml': 'http://www.w3.org/XML/1998/namespace',
    }

SAML_METADATA_NAMESPACE = NAMESPACES['md']


def addns(node_name, namespace=SAML_METADATA_NAMESPACE):
    '''Return a node name qualified with the XML namespace'''
    return '{' + namespace + '}' + node_name


def delns(node, namespace=SAML_METADATA_NAMESPACE):
    return node.replace('{' + namespace + '}', '')


def add_previous_revisions(revisions):
    prev, revs = '', []
    for rev in revisions[::-1]:
        if prev:
            rev['previous'] = prev
        prev = rev['versionid']
        revs.append(rev)
    return reversed(revs)


def expand_settings_permissions(include_xpath=True):
    if not hasattr(settings, 'METADATA_PERMISSIONS'):
        return None
    permissions = list()
    if hasattr(settings, 'METADATA_PERMISSIONS'):
        return None
    perm_setts = settings.METADATA_PERMISSIONS
    for prefix in ('add', 'delete', 'modify'):
        for xpath, name, desc in perm_setts:
            perm_class = '_'.join(('Can', prefix.capitalize(), name))
            perm_desc = ' '.join((prefix, desc))
            exp_perms = [perm_class, perm_desc]
            if include_xpath:
                exp_perms.insert(0, xpath)
            permissions.append(tuple(exp_perms))
    return tuple(permissions)


