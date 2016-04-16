TARGET = jpmap
TEMPLATE = aux

system(kmap2qmap jp.kmap jp.qmap)

map.files = jp.qmap 
map.path = /usr/share/qt5/keymaps/

INSTALLS = map

OTHER_FILES += \
    patch/patch.json \
    patch/unified_diff.patch \
    rpm/bt-keyboa.spec \
    jp.kmap \
    LICENSE \
    README.md
