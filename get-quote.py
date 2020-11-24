import random

def Isaac():


  f = open("quotes.txt", "a+")
  f.write("Be Nice\n")
  quotes = f.readlines()
  f.close()

  last = 17
  rnd = random.randint(0, last)
  print(quotes[rnd].rstrip())
  rnd = random.randint(0, last)
  print(quotes[rnd].rstrip())
  rnd = random.randint(0, last)
  print(quotes[rnd].rstrip())

if __name__== "__main__":
  Isaac()
