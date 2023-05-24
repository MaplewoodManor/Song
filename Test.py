description: 
from earsketch import *

# Music
beat1 = "";
#beat1 = "0---0---0---0+++"
x = 0 #index

insertMedia(GREGORYAFTON_CYMBOL, 7, 60)

#intro beats(?)
makeBeat(OS_KICK01, 7, 1, beat1)

#main 3 tracks
y = 0
for x in range(1, 60, 4):
    fitMedia(MILKNSIZZ_CRASH_PAD_GUITAR, 4, x, (x + 2))
for x in range(3, 60, 4):
    fitMedia(AK_UNDOG_ACOUSTIC_GUITAR_2, 5, x, (x+2))
for x in range(36, 60, 8):
    fitMedia(JWOLF_COTG_THEME_BASS_CHORUS, 6, x, (x+4))
for x in range(1, 35, 5):
    fitMedia(JWOLF_COTG_VOX_MISC_BLOODLINE, 6, x, (x+2))
fitMedia(GREGORYAFTON_EARBLEED, 8, 55, 60)


fitMedia(RD_CINEMATIC_SCORE_STRINGS_4, 1, 2, 61)
fitMedia(RD_CINEMATIC_SCORE_HARP_4, 2, 2, 61)
fitMedia(RD_CINEMATIC_SCORE_STRINGS_10, 3, 2, 61)

#sets the tempo
setTempo(120)
