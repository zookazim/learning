from turtle import done


lstHosp = ['rph','scgh','fsh','mid']
lstTableName = ['study','deaths','medicines','posted','prehospital']
lstTableAbbr = ['stud','deat','meds','post','preh']
lstTableExcelTab = ['Study','Deaths','Medicines','PostED','PreHospital']

for i in lstHosp:
    print('df_' + i)
done

print('\n'.join(lstTableName))

