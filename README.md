# ny-election-cleaning
quick cleaning of ascii delimited data


So basically these files are ASCII delimited, which means they have different separators within the same file to delimit different things — unlike a CSV or TSV, which is delimited only by one separator.

The TXT file included when you download each data file explains how the files are delimited. Here I used January 2007 as an example. Open up `EFSRECB.TXT`.

So if you look at those listed separators at the bottom:

`(RecordSeparator): CR-LF
(FieldSeparator): ,
(FieldStartDelimiter): "
(FieldEndDelimiter): "
(FieldDelimitStyle): all
(StripLeadingBlanks): True
(StripTrailingBlanks): True`

...you can see an explanation for how the files are delimited. What we want to do is change the record separator to a comma (to make a CSV) and then strip the file of all the quotes just so we don't run into any issues there.

This is pretty simple to do in Python — just put the `jan2007.out` file next to the `clean.py` file in this repository. Then, open up your terminal or command line, navigate to the location of both files, and run `python clean.py`. Now, you'll see a file called `jan2007_cleaned.csv` in that directory!

The last issue we run into is that there are no headers for this csv file. To remedy this, simply open the CSV file in a text editor (I used TextEdit on my Mac) and paste the headers at the top. I made this list from the TXT file provided by the BOE: 

`FILER_ID,FREPORT_ID,TRANSACTION_CODE,E_YEAR,T3_TRID,DATE1_10,DATE2_12,CONTRIB_CODE_20,CONTRIB_TYPE_CODE_25,CORP_30,FIRST_NAME_40,MID_INIT_42,LAST_NAME_44,ADDR_1_50,CITY_52,STATE_54,ZIP_56,CHECK_NO_60,CHECK_DATE_62,AMOUNT_70,AMOUNT2_72,DESCRIPTION_80,OTHER_RECPT_CODE_90,PURPOSE_CODE1_100,PURPOSE_CODE2_102,EXPLANATION_110,XFER_TYPE_120,CHKBOX_130,CREREC_UID,CREREC_DATE,`

Now if you save the file, you should be able to open it up in Excel. The data may still be dirty/there may still be other issues, so if you need more help, let me know!


