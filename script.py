# clean = open('2007jan.csv').read().replace('\n', ',')
# print clean

# FILER_ID,FREPORT_ID,TRANSACTION_CODE,E_YEAR,T3_TRID,DAT1_10,DATE2_12,CONTRIB_CODE_20, CONTRIB_TYPE_CODE_25,CORP_30,FIRST_NAME_40,MID_INIT_42,LAST_NAME_44,ADDR_1_50,CITY_52,STATE_54,ZIP_56,CHECK_NO_60,CHECK_DATE_62,AMOUNT_70,AMOUNT2_72,DESCRIPTION_80,OTHER_RECPT_CODE_90,PURPOSE_CODE1_100,PURPOSE_CODE2_102,EXPLANATION_110,XFER_TYPE_120,CHKBOX_130,CREREC_UID,CREREC_DATE,

f = open('2007jan.out')
contents = f.read()

new_contents = contents.replace('\r\n', ',')
new_contents = contents.replace('\"', '')
f = open('2007jan_cleaned.csv', 'w')
f.write(new_contents)
f.close()
