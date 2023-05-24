# description: 
from earsketch import *

# Music
beat1 = "";
#beat1 = "0---0---0---0+++"
x = 0 #index

insertMedia(GREGORYAFTON_CYMBOL, 7, 60)

#intro beats(?)
makeBeat(OS_KICK01, 7, 1, beat1)

#main 3 tracks
fitMedia(RD_CINEMATIC_SCORE_STRINGS_4, 1, 2, 61)
fitMedia(RD_CINEMATIC_SCORE_HARP_4, 2, 2, 61)
fitMedia(RD_CINEMATIC_SCORE_STRINGS_10, 3, 2, 61)

#sets the tempo
setTempo(120)
