print("hello world")



# comment

print("python", "is","awesome",sep="-");  # concat
print("naveen");
print ("is")
print ("awesome");
name = "naveen"
age = "25"
hight = "5"
print(type(name))
print (type(age))
print(type(hight))
# a =10;
# b= 20;
# c= 30;
# a =b=10
# a, b,c=10,20,30
a , b =10,20
temp = 0;
temp = a;
a= b;
b= temp;
print(a,b)
# print (a,b,c)
#x,y=20,40
#x=x+y;
#y = x-y;
#x=x-y;
# print(x,y)
# type casting

str1 = str("25");
# 25 -> string
# class = "25";
str1 = "25";
int1 = int (str1);
float1 = float (str1);
str2 = str(float1);
bool1 = bool (()); # 0,0,0,"",{},[],set()


# print(str1,int1,float1,str2,bool1)
# operators 
# *
# -
# +
# /
# //
#%
# * *
# print(10+10);
# print(10-10);
# print(20*20);
# print(1/2);
# print(1//2);
# print(3%2);
# print(3**3);
# ==
# !=
# >
# >=
# <
# <=

# print(10==10);
# print(10!=10);
# print(10>10);
# print(10>=10);
# print(10<10);
# print(10<=10);

# assigment operators
# =
# +=
# -=
# *=
# /=
# //=
# %=
# **=
x1 =10;
x1+=20;
x1-=5;
x1*=2;
x1/=2;
x1//=2;
x1%=2;
x1**=4;

print(x1)
# membership comparison
pet = "cat";
checkval = "c"
print(checkval in pet);
# ()
# **
# *,/,//,%,+.-


# print(10+5*2);

# print(20/5+3); 

# print((10+5)*2);

# print (2+3**2);

# x = (10==10);
# y =(12==12);
#print Method


s= ' hello world ';
NewStr = s.strip();
print(s);
print(s.strip().lower().upper()); #method chaining
print(s.lower());
print(s.title());
print(s.replace("world","java"));
print(s.split(','))
print(NewStr.find('world'));
print(NewStr.count('w'));
print(NewStr .startswith('h'));
print(NewStr.endswith('n'));
print(len(NewStr));


name,marks = "naveen",'48';
# print(name,marks);
print(f'(name) has scored (marks)');
print('{} scored {}'. format(name,marks));
# print ('%s scored %d' % (name,marks));


# escape charactors
#\n new line
str = 'naveen\\rawat'
# print(str)

# immutabitlity
# strl = 'cat';
# strl[0] ='n'
str2 = str1;
str1 ='cat123'
print(str1 ,str2)

print('naveen'[1:-4]);
print('school'[::-1])
str3 = '123'
# print(str3==str3[::-1]);

# how we can get input

# marks = int(input ('plz enter some thing'))
# print(marks)

# control flow

# age = int(input('plz enter your age : > '));

# if age >= 18 :
#     print('u r eligible for vote')
# else :
#     print('u r not eligible for vote');
# # 90 >=a
# # 75>=b
# # 50 >=C
# # fail


# if marks >= 90:
#     print("A");
# elif marks >=75:
#     print('B');
# elif marks >= 50:
#     print('C');
# else : 
#     print('fail')

    # ternary opeartor
# status = 'pass' if marks >= 40 else 'fail';
# print(status)
