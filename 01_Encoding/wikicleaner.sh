#Set up temp files
file1=$(mktemp)
file2=$(mktemp)
file3=$(mktemp)

#Grep non-alphabet characters, count and sort. Write to temp file1 Add blankline at start of file for later paste operation
grep -Piwo "[^äëïöüA-ZÂÊÉÔÛÚó0-9 \p{Mn}\p{P}]" wiki.txt | sort | uniq -c | sort -n | sed '1i\\' > $file1

#Make file without counts for uniname later from file1 into file2
grep -Piwo "[^0-9	 ]+" $file1 > $file2

#For each non-alphabetic character in file2, write the unicode name of the character into file3
uniname <$file2 -bcpeAu > $file3 

#merge file1 (character with count) and file3(unicode name), write to frequencyListCharacters.txt
paste $file1 $file3 | cat > frequencyListCharacters.txt

#Take everything that is a valid character, and write to cleanLinesEncoding.txt
grep -Pi "[äëïöüA-ZÂÊÉÔÛÚó0-9 \p{Mn}\p{P}]+" wiki.txt | cat > cleanLinesEncoding.txt

#Set up new temp files
file4=$(mktemp)
file5=$(mktemp)
file6=$(mktemp)

#In cleaned string, pull all spacing and formatting symbols, write to temp with unicode names (Same process as above)
grep -Pio "[\p{Zs}\p{Cf}]" cleanLinesEncoding.txt | sort | uniq -c | sort -n > $file4
grep -Piwo "[^0-9        ]+" $file4 > $file5
uniname < $file5 -bcpeAu > $file6
paste $file4 $file6 | cat > spacingFormatingCharacters.txt


