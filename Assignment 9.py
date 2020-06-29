
{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the size of the list:5\n",
      "Enter number at location 0 :\n",
      "10\n",
      "Enter number at location 1 :\n",
      "19\n",
      "Enter number at location 2 :\n",
      "23\n",
      "Enter number at location 3 :\n",
      "36\n",
      "Enter number at location 4 :\n",
      "48\n",
      "The list is= [10, 19, 23, 36, 48]\n",
      "Original List: [10, 19, 23, 36, 48]\n",
      "After Cloning: [10, 19, 23, 36, 48]\n"
     ]
    }
   ],
   "source": [
    "def Copy(List1): \n",
    "    li_copy=List1[:] \n",
    "    return li_copy \n",
    "List1=[]\n",
    "n=int(input(\"Enter the size of the list:\"))\n",
    "for i in range(0, n):\n",
    "    print(\"Enter number at location\", i, \":\")\n",
    "    item = int(input())\n",
    "    List1.append(item)\n",
    "print(\"The list is=\",List1)\n",
    "List2=Copy(List1) \n",
    "print(\"Original List:\",List1) \n",
    "print(\"After Cloning:\",List2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Output: ['Green', 'White', 'Black']\n"
     ]
    }
   ],
   "source": [
    "color=['Red','Green','White','Black','Pink','Yellow']\n",
    "color1=[x for (i,x) in enumerate(color) if i not in (0,4,5)]\n",
    "print(\"Output:\",color1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the size of the list:7\n",
      "Enter number at location 0 :\n",
      "1\n",
      "Enter number at location 1 :\n",
      "2\n",
      "Enter number at location 2 :\n",
      "3\n",
      "Enter number at location 3 :\n",
      "4\n",
      "Enter number at location 4 :\n",
      "5\n",
      "Enter number at location 5 :\n",
      "6\n",
      "Enter number at location 6 :\n",
      "7\n",
      "The list is= [1, 2, 3, 4, 5, 6, 7]\n",
      "The list after removing the even numbers= [1, 3, 5, 7]\n"
     ]
    }
   ],
   "source": [
    "List1=[]\n",
    "n=int(input(\"Enter the size of the list:\"))\n",
    "for i in range(0, n):\n",
    "    print(\"Enter number at location\", i, \":\")\n",
    "    item = int(input())\n",
    "    List1.append(item)\n",
    "print(\"The list is=\",List1)\n",
    "List1=[x for x in List1 if x%2!=0]\n",
    "print(\"The list after removing the even numbers=\",List1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['Red', 'Yellow', 'White', 'Pink', 'Green', 'Black']\n"
     ]
    }
   ],
   "source": [
    "from random import shuffle\n",
    "color=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']\n",
    "shuffle(color)\n",
    "print(color)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the size of the list1:5\n",
      "Enter number at location 0 :\n",
      "1\n",
      "Enter number at location 1 :\n",
      "3\n",
      "Enter number at location 2 :\n",
      "5\n",
      "Enter number at location 3 :\n",
      "7\n",
      "Enter number at location 4 :\n",
      "9\n",
      "Enter the size of the list2:6\n",
      "Enter number at location 0 :\n",
      "1\n",
      "Enter number at location 1 :\n",
      "2\n",
      "Enter number at location 2 :\n",
      "4\n",
      "Enter number at location 3 :\n",
      "6\n",
      "Enter number at location 4 :\n",
      "7\n",
      "Enter number at location 5 :\n",
      "8\n",
      "The difference of the two lists is= [9, 3, 5, 8, 2, 4, 6]\n"
     ]
    }
   ],
   "source": [
    "list1=[]\n",
    "n=int(input(\"Enter the size of the list1:\"))\n",
    "for i in range(0, n):\n",
    "    print(\"Enter number at location\", i, \":\")\n",
    "    item = int(input())\n",
    "    list1.append(item)\n",
    "list2=[]\n",
    "n=int(input(\"Enter the size of the list2:\"))\n",
    "for i in range(0, n):\n",
    "    print(\"Enter number at location\", i, \":\")\n",
    "    item = int(input())\n",
    "    list2.append(item)\n",
    "diff_list1_list2=list(set(list1)-set(list2))\n",
    "diff_list2_list1=list(set(list2)-set(list1))\n",
    "total_diff=diff_list1_list2+diff_list2_list1\n",
    "print(\"The difference of the two lists is=\",total_diff)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4