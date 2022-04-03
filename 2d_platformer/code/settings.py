level_map = [
'                                           ',
'                                          X',
'                                          X',
' XX    XXX            XX                  X',
' XX P          D                X         ',
' XXXX         XX         XX     X         ',
' XXXX       XX               XXXXX        ',
' XX    X  XXXX    XX  XX    XX            ',
'       X  XXXX    XX  XXX   XX            ',
'    XXXX  XXXXXX  XX  XXXX  XX            ',
'XXXXXXXX  XXXXXX  XX  XXXX              XX']

tile_size = 64
screen_width = 1000
# We want height to be relative to the level_map
screen_height = len(level_map) * tile_size