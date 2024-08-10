This Python script adds custom RNP approaches and SIDS for five Alaskan Airports to the PMDG 737 Navigation Database. The original nav data files are from Trevor Lahey on AVSIM.net, uploaded March 31st 2018.

************
INSTRUCTIONS
************

1) Open _paths.py in a text editor, and change the second line "COMMUNITY_FOLDER = " to point to your MSFS Community Folder.
2) Run update.py to automatically create a backup of your existing files, and add the custom nav data to your PMDG 737 database.
3) Restore.py can be used to restore your PMDG Nav Database back to the original state. This assumes you ran the backup first. 

*******************
Procedure Specifics
*******************

Minimum altitudes for specific IAF (Initial Approach Fixes). The min altitudes are based on flying up and down Southeast Alaska and are safe within 20NM of the fix. In many cases you can get sufficiently lower but these will keep you clear of terrain. 

The only exception is if you are inbound from Canada to the east. The altitudes are much higher in that quadrant, so use caution if inbound from the east. They are as high as 12,400 in that direction. 
	
    ANN   7000
	BKA   7500  
	CUSHI 8000
	DOOZI 8000
	FLIPS 7500
	FUNTR 8000
	IRUNE 10,000
	LVD   8000
	KAJBU 10,000
	KASAN 7000
	MITKF 10,000
	MOHTU 10,000
	ODECO 10,000
	RODMN 7500
	SSR   8000
	STVNS 10,000
	TNAKY 8000
	UDENE 6100


Some initial approach fixes are not natively in the FMC database. Load the departure and/or approach and they will load into the legs page. 
These are suggested routes because you may not have charts. The last fix in these routes are an IAF for the respective approach procedures.

PAJN > PAPG GLAZZ1 ODECO
PAJN > PAKT GLAZZ1 LVD DOOZI
PAJN > PASI RODMN1 RODMN
PAJN > PAWG GLAZZ1 LVD

PAKT > PAJN DOOZI2 LVD (FUNTR RNW08) (STVNS RNW26)
PAKT > PAPG DOOZI2 LVD 
PAKT > PASI UDENE3 FLIPS
PAKT > PAWG DOOZI2 (DOOZI RNW 28) (LVD RNW 10)

PAPG > PAJN GORBY4 GORBY STVNS
PAPG > PAKT HURAS2 LVD DOOZI
PAPG > PASI GORBY4 GORBY FLIPS
PAPG > PAWG HURAS2 MITKF

PAWG > PAJN KAJBU5 KAJBU STVNS (Expedite climb through 6000, RNW 28)
PAWG > PAKT KAJBU5 KAJBU DOOZI (Expedite climb through 6000, RNW 28)
PAWG > PAPG KAJBU5 KAJBU
PAWG > PASI KAJBU5 KAJBU LVD FLIPS


Procedure Minimums. These are not the exact numbers but are close. 

	PAJN
		RNAV (RNP) M 08
			DA = 6800 Vis Required 1 NM
		RNAV (RNP) M 26
			DA = 2800 Vis required 3/4 NM

	PAKT
		RNAV (RNP) M 11
			DA = 4300 Vis required 3/4 NM
		RNAV (RNP) M 29
			DA = 3700 Vis required 1/2 NM

    PAPG
		RNAV (RNP) M 05
			DA = 3800 Vis required 3/4 NM
		RNAV (RNP) M 23
			DA = 3800 Vis required 1/2 NM

	PASI 
		RNAV (RNP) M 11
			DA = 2800 Vis required 3/4 NM
		RNAV (RNP) M 29
			DA = 4000 Vis required 1 1/8 NM
	
	PAWG 
		RNAV (RNP) M 10
			DA = 3000 Vis required 3/4 NM
		RNAV (RNP) M 28
			DA = 3800 Vis required 1 NM 