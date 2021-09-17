
import KnobScripter




try:
    import shortcuteditor
    shortcuteditor.nuke_setup()
except Exception:
    import traceback
    traceback.print_exc()

import duplicateWithInputs

nuke.menu('Nuke').addCommand('Scripts/Duplicate with Inputs/copy','duplicateWithInputs.copyWithInputs()', 'ctrl+alt+c')
nuke.menu('Nuke').addCommand('Scripts/Duplicate with Inputs/paste','duplicateWithInputs.pasteWithInputs()', 'ctrl+alt+v')
nuke.menu('Nuke').addCommand('Scripts/Duplicate with Inputs/duplicate','duplicateWithInputs.duplicateWithInputs()', 'ctrl+e') 


# MagicTools
toolbar = nuke.menu('Nodes')
MagicMenu = toolbar.addMenu('MagicTools', icon='MagicTools.png')
MagicMenu.addCommand('MagicDefocus', 'nuke.createNode("MagicDefocus")')

###import W_backdropper

###nuke.knobDefault("FilterErode.filter","gaussian")


cur_menu = nuke.menu(u'Nodes')
m = cur_menu.findItem(u'Channel/ChannelMerge')
if m is not None:
    m.setShortcut(u'Alt+O')


cur_menu = nuke.menu(u'Nuke')
m = cur_menu.findItem(u'Workspace/Toggle Hide Floating Viewers')
if m is not None:
    m.setShortcut(u'')

m = cur_menu.findItem(u'Edit/Node/Connect')
if m is not None:
    m.setShortcut(u'`')


# ShortcutEditor generated snippet:
cur_menu = nuke.menu('Nodes')
m = cur_menu.findItem('Merge/Merges/Stencil')
if m is not None:
    m.setShortcut(u'Alt+[')

m = cur_menu.findItem('Merge/Merges/Mask')
if m is not None:
    m.setShortcut(u'Alt+]')



import AlignDots

nuke.menu('Nuke').addCommand('Extra/Align Dots', "AlignDots.AlignDots()", ",", shortcutContext=2)



# StickyNote > default text size: 40pt  
nuke.knobDefault("StickyNote.note_font_size", "40")  
nuke.knobDefault("StickyNote.tile_color", "0x050505FF")

# ShortcutEditor generated snippet:
cur_menu = nuke.menu(u'Nodes')
m = cur_menu.findItem(u'Other/StickyNote')
if m is not None:
    m.setShortcut(u'Alt+Shift+N')



