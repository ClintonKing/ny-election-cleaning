import sys
import re
import csv

# clean = open('2007jan.csv').read().replace('\n', ',')
# print clean

HEADER = ['FILER_ID','FREPORT_ID','TRANSACTION_CODE','E_YEAR,T3_TRID','DAT1_10','DATE2_12','CONTRIB_CODE_20', 'CONTRIB_TYPE_CODE_25','CORP_30','FIRST_NAME_40','MID_INIT_42','LAST_NAME_44','ADDR_1_50,CITY_52','STATE_54','ZIP_56','CHECK_NO_60','CHECK_DATE_62','AMOUNT_70','AMOUNT2_72','DESCRIPTION_80','OTHER_RECPT_CODE_90','PURPOSE_CODE1_100','PURPOSE_CODE2_102','EXPLANATION_110','XFER_TYPE_120','CHKBOX_130,CREREC_UID','CREREC_DATE']

def out_to_csv(out_file):

    file_name = re.split(r'\.out(?:\.\w+)?$', out_file)[0]
    cleaned_file = file_name + '_clean.csv'

    f = open(out_file)
    contents = f.read()

    new_contents = contents.replace('\r\n', ',')
    new_contents = contents.replace('\"', '')

    with open(cleaned_file, 'w') as f:
        w = csv.writer(f)
        w.writerow(HEADER)
        f.write(new_contents)
        f.close()
        print "Conversion successful. Check " + cleaned_file

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('Filename required')
        sys.exit()

    out_file = str(sys.argv[1])
    out_to_csv(out_file)
