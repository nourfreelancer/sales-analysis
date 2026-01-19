def general(sent):

#variables
    freq={}
    letter_count=0
    word_count=0
    in_word=False

#loop for ecach charahter in the sentence
    for ch in sent:
      if ch.isalpha():
         letter_count += 1 
          
         if ch not in freq:
            freq[ch] = 1
         else:
            freq[ch] += 1

         if not in_word:
            word_count += 1
            in_word = True
         
      elif  ch in [" ",",",":","!"] :
           in_word = False


    print(f" Letter = {letter_count}")
    print(f" word = {word_count} ")
    return freq


def length(sent):
   l_dict = {}
   st = ""
   count = 0

   for i in sent:
      if i.isalpha(): 
         st += i
         count += 1 
      elif i in [" ",",",":","!"] :
        if count > 0:
         if st not in l_dict:
            l_dict[st]={"leng" : count , "freq" : 1}
         else:
            l_dict[st]['freq'] += 1
         st = ""
         count = 0

   if count > 0:
         if st not in l_dict:
            l_dict[st]={"leng" : count , "freq" : 1}
         else:
            l_dict[st]['freq'] += 1
        
   return l_dict

def top(freq):
  f = s = t = 0
  f_item = s_item = t_item = ""

  for i,k in freq.items():
     if k > f :
        f = k
        f_item = i

  for i,k in freq.items():
     if k > s and k < f :
        s = k
        s_item = i

  for i,k in freq.items():
     if k > t  and k < s:
        t = k
        t_item = i

  return (f_item, f), (s_item, s), (t_item, t)




def main():

   longest=0
   shortest=10**9
   repeated=[]

   print("Welcome to analysis system\n".capitalize())
   print("enter your sentance : ".capitalize())
   sentance=input()

   print()
   #first def for letter
   x_gneral=general(sentance)
   print("\n letter frequence : ")
   for i,k in x_gneral.items():
      print(f" '{i}':{k} ",end=",")

   #seocnd def for words
   x_length=length(sentance)
   print(" \n words length : ")
   for i,k in x_length.items():
      print(f" {i}  : {k['leng']} ",end=" ")

   #most repat

   for i,k in x_length.items():
      if k['freq'] > 1 :
         repeated.append(i)
   print(f"\n most repeated = {repeated}")

   #short and long words
  
   for i,k in x_length.items():
       if k['freq'] > longest:
          longest=k['freq']
          l_word=i
   print(f" longest word = {longest}({l_word})")

   for i,k in x_length.items():
       if k['freq'] < shortest:
          shortest=k['freq']
          s_word=i

   print(f" shortest word = {shortest}({s_word})")


   #third def for top3
   x_top=top(x_gneral)
   print(f" top 3 = {x_top} ")


main()




