import translate
trans = translate.Translator(to_lang='ja', from_lang='en')
# 1_open the file it should have englis contant
# 2_stor every line of the file into a string list
# 3_loop into the list and write the en sentences to enToJa.txt and then translate sente to ja then wirte it also.
# that is all :-)
try:
    en_file = 'en.txt'
    tran_file = 'enToJa.txt'
    with open(en_file, mode='r') as en_f:
        en_text = en_f.readlines()
    with open(tran_file, mode='w', encoding='utf-8') as ja_f:
        for i in en_text:
            ja_f.write(i)
            print(i)
            ja_f.write(trans.translate(i) + '\n')
            print(trans.translate(i))
except UnicodeEncodeError as err:
    print(err)
except:
    print('You have some issues!!!')
