
(function($) {
    var UI = {
        "clearEntityAttrs": function() {
            $("div#entityattrs > div.content").empty();
        },
        "addEntityAttr": function(entityattr) {
            var randID = Math.floor(Math.random() * 10000 + 1000);
            var entityattrHTML = '<fieldset><legend>Attribute</legend>' +
                '<div class="entityattrfield">' +
                    '<label for="entityattr-' + randID + '-NameFormat">Name format: </label>' +
                    '<input type="text" name="entityattr-' + randID + '-NameFormat-name" id="entityattr-' + randID + '-NameFormat" value="' + (entityattr.nameFormat || '') + '" />' +
                '</div>' +

                '<div class="entityattrfield">' +
                    '<label for="entityattr-' + randID + '-Name">Name: </label>' +
                    '<input type="text" name="entityattr-' + randID + '-Name-name" id="entityattr-' + randID + '-Name" value="' + (entityattr.name || '') + '" />' +
                '</div>' +

                '<div class="entityattrfield">' +
                    '<label for="entityattr-' + randID + '-FriendlyName">Friendly name: </label>' +
                    '<input type="text" name="entityattr-' + randID + '-FriendlyName-name" id="entityattr-' + randID + '-FriendlyName" value="' + (entityattr.friendlyName || '') + '" />' +
                '</div>' +

                '<div class="entityattrfield">' +
                    '<label for="entityattr-' + randID + '-values">Value: </label>' +
                    '<input type="text" name="entityattr-' + randID + '-values-name" id="entityattr-' + randID + '-values" value="' + (entityattr.values || '')+ '" />' +
                '</div>' +

                '<button style="display: block; clear: both" class="remove">Remove</button>' +

            '</fieldset>';

            $(entityattrHTML).appendTo("div#entityattrs > div.content").find('button.remove').click( function(e) {
                e.preventDefault();
                $(e.target).closest('fieldset').remove();
            });
        }
    };

    SAMLmetaJS.plugins.entityattrs = {
        tabClick: function (handler) {
            handler($("a[href='#entityattrs']"));
        },

        addTab: function (pluginTabs) {
            pluginTabs.list.push('<li><a href="#entityattrs">Entity attrs</a></li>');
            pluginTabs.content.push(
                '<div id="entityattrs">' +
                    '<div class="content"></div>' +
                    '<div><button class="addentityattr">Add new attribute</button></div>' +
                '</div>'
            );
        },

        setUp: function () {
            $("div#entityattrs button.addentityattr").click(function(e) {
                e.preventDefault();
                UI.addEntityAttr({});
            });
        },

    fromXML: function (entitydescriptor) {
            var attr;

            // Clear contacts
            UI.clearEntityAttrs();
            
            // Add existing contacts (from XML)            
            if (entitydescriptor.entityAttributes) {
                for (attr in entitydescriptor.entityAttributes) {
          if (entitydescriptor.entityAttributes.hasOwnProperty(attr)) {
                      UI.addEntityAttr(entitydescriptor.entityAttributes[attr]);
          }
                }
            }
        },

        toXML: function (entitydescriptor) {
            $('div#entityattrs fieldset').each(function (index, element) {
                var newEntityAttr = {'values': []}, i;

                //--------------------------------------------------
                // if (!$(element).find('input').eq(3).attr('values')) {
                //     return;
                // }
                //-------------------------------------------------- 

                newEntityAttr.nameFormat = $(element).find('input').eq(0).attr('value').trim();
                newEntityAttr.name = $(element).find('input').eq(1).attr('value').trim();
                newEntityAttr.friendlyName = $(element).find('input').eq(2).attr('value').trim();
                newEntityAttr.values.push($(element).find('input').eq(3).attr('value').trim());
                //--------------------------------------------------
                // vals = $(element).find('input').eq(3).attr('value');
                // values = vals.split(',');
                // for (i = 0; i < values.length; i++) {
                //    newEntityAttr.values.push(values[i].trim());
                // }
                if (!entitydescriptor.entityAttributes) { entitydescriptor.entityAttributes = []; }
                entitydescriptor.entityAttributes.push(newEntityAttr);
            });
        }
    };

}(jQuery));
