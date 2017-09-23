import csv


dic = {}
dic_array = []

keys = ['Name', 'Email', 'Mobile', 'Uni', 'Major']



def user():



  while True:

       Name = input('Enter your name: ')
       if Name == "stop":
           break
       dic_array.append(Name)

       Email = input('Enter your email: ')
       if Email == "stop":
           break
       dic_array.append(Email)

       Mobile = input('Enter your mobile: ')
       if Mobile == "stop":
           break
       dic_array.append(Mobile)

       Uni = input('Enter your uni: ')
       if Uni == "stop":
           break

       dic_array.append(Uni)
       Major = input('Enter your major: ')
       if Major == "stop":
           break
       dic_array.append(Major)

  x = 0
  Headers()
  for i in range(len(dic_array)):
      dic[keys[x]] = dic_array[i]
      x += 1
      if dic_array[i] == "stop" and x < 5:
            append(dic)
            break

      if x == 5:
          x = 0
          append(dic)




def Headers():
    f = open('task7.csv', 'w')

    with f:
        headers = ['Name', 'Email', 'Mobile', 'Uni', 'Major']
        writer = csv.DictWriter(f, fieldnames=headers)


        writer.writeheader()



def append(dic):
    f = open('task7.csv', 'a')

    with f:
        headers = ['Name', 'Email', 'Mobile', 'Uni', 'Major']
        writer = csv.DictWriter(f, fieldnames=headers)


        writer.writerow(dic)







user()
print(dic_array)
