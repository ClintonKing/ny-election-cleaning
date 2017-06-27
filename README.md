# ny-election-cleaning
quick cleaning of ascii delimited data


So basically these files are ASCII delimited, which means they have different separators within the same file to delimit different things — unlike a CSV or TSV, which is delimited only by one separator.

The TXT file included when you download each data file explains how the files are delimited. Here I used January 2007 as an example. Here is the TXT file: 

`NEW YORK STATE BOARD OF ELECTIONS

RECORD LAYOUT FOR EFS DISCLOSURE TRANSACTIONS

                        DELIMITED ASCII

Note: Filer ID: 	A#####  = State Filers
		C#####  = County Filers

 FIELD                        LOCATION               TYPE        FORMAT                         EFS IMPORT


 FILER_ID                       01                   CHAR                                       REQUIRED
 FREPORT_ID                     02                   CHAR                                       REQUIRED
 TRANSACTION_CODE               03                   CHAR                                       REQUIRED
 E_YEAR                         04                   CHAR                                       REQUIRED
 T3_TRID                        05                   INTEGER
 DATE1_10                       06                   DATE        'MM/DD/YYYY'
 DATE2_12                       07                   DATE        'MM/DD/YYYY'
 CONTRIB_CODE_20                08                   CHAR
 CONTRIB_TYPE_CODE_25           09                   CHAR
 CORP_30                        10                   CHAR
 FIRST_NAME_40                  11                   CHAR
 MID_INIT_42                    12                   CHAR
 LAST_NAME_44                   13                   CHAR
 ADDR_1_50                      14                   CHAR
 CITY_52                        15                   CHAR
 STATE_54                       16                   CHAR
 ZIP_56                         17                   CHAR
 CHECK_NO_60                    18                   CHAR
 CHECK_DATE_62                  19                   DATE        'MM/DD/YYYY'
 AMOUNT_70                      20                   FLOAT
 AMOUNT2_72                     21                   FLOAT
 DESCRIPTION_80                 22                   CHAR
 OTHER_RECPT_CODE_90            23                   CHAR
 PURPOSE_CODE1_100              24                   CHAR
 PURPOSE_CODE2_102              25                   CHAR
 EXPLANATION_110                26                   CHAR
 XFER_TYPE_120                  27                   CHAR
 CHKBOX_130                     28                   CHAR
 CREREC_UID                     29                   CHAR
 CREREC_DATE                    30                   DATE        'MM/DD/YYYY HH24:MI:SS'

(RecordSeparator): CR-LF
(FieldSeparator): ,
(FieldStartDelimiter): "
(FieldEndDelimiter): "
(FieldDelimitStyle): all
(StripLeadingBlanks): True
(StripTrailingBlanks): True`


So if you look at those listed separators at the bottom, you can see an explanation for how the files are delimited. What we want to do is change the record separator to a comma (to make a CSV) and then strip the file of all the quotes just so we don't run into any issues there.

This is pretty simple to do in python — just put the `jan2007.out` file next to the `clean.py` file in this repository. Then, open up your terminal or command line, navigate to the location of both files, and run `python clean.py`. Now, you'll see a file called `jan2007_cleaned.csv` in that directory!

The last issue we run into is that there are no headers for this csv file. To remedy this, simply open the CSV file in a text editor (I used TextEdit on my Mac) and paste the headers at the top. I made this list from the TXT file provided by the BOE: 

`FILER_ID,FREPORT_ID,TRANSACTION_CODE,E_YEAR,T3_TRID,DATE1_10,DATE2_12,CONTRIB_CODE_20,CONTRIB_TYPE_CODE_25,CORP_30,FIRST_NAME_40,MID_INIT_42,LAST_NAME_44,ADDR_1_50,CITY_52,STATE_54,ZIP_56,CHECK_NO_60,CHECK_DATE_62,AMOUNT_70,AMOUNT2_72,DESCRIPTION_80,OTHER_RECPT_CODE_90,PURPOSE_CODE1_100,PURPOSE_CODE2_102,EXPLANATION_110,XFER_TYPE_120,CHKBOX_130,CREREC_UID,CREREC_DATE,`

Now if you save the file, you should be able to open it up in Excel. The data may still be dirty/there may still be other issues, so if you need more help, let me know!


