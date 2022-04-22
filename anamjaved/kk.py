#!/usr/bin/python
import time
import random
import math
import sys


def instance():
    # create initial array
    instance = [None] * 100
    for i in range (0, 100):
        instance[i] = random.randint(1,1000000000000)
    #print instance[i]
    return instance



def randsolgen_binary(arr):
    arr=arr[:]
    randsol = [None] * len(arr)
    for i in range (0, len(arr)):
        probmin = random.uniform(0, 9)
        probplus = random.uniform(0,9)
        if (probmin > probplus):
            randsol[i] = -1
        else:
            randsol[i] = +1
    #print randsol[i]
    return randsol

def randsolgen(arr):
    arr=arr[:]
    randsol = [None] * len(arr)
    for i in range(0, len(arr)):
        randsol[i] = random.randint(0, 99)
    #print randsol[i]
    return randsol

#sorts list in place!
def karmKarp(arr):
    # sorts list in place

    #sorted_list = sorted(arr)
    arr_copy = arr[:]
    for i in range(len(arr_copy)-1,0,-1):
        #print "i= %solution" %(i)
        arr_copy.sort()
        s = arr_copy[i] - arr_copy[i-1]
        #print solution
        arr_copy.remove(arr_copy[i])
        arr_copy.remove((arr_copy[i-1]))
        arr_copy.append(s)
    #for x in range(0, len(arr)):
    #print arr[i]
    #print arr_copy[0]
    return arr_copy[0]

def randadj_bin(randsol):
    randsol=randsol[:]
    index = random.randint(0, len(randsol)-1)
    index_two = random.randint(0, len(randsol)-1)
    prob_one = random.uniform(0, 9)
    prob_two = random.uniform(0,9)
    if (prob_one > prob_two):
        randsol[index] = randsol[index]*-1
    prob_three = random.uniform(0,9)
    prob_four = random.uniform(0,9)
    if (prob_three > prob_four):
        randsol[index_two] = randsol[index_two]*-1
    #for i in range(0, len(randsol)):
    #	print randsol[i]
    return randsol;

def randadj(randsol):
    randsol=randsol[:]
    i = random.randint(0, len(randsol)-1)
    n = random.randint(0, len(randsol)-1)
    while (randsol[i] == n):
        i = random.randint(0, len(randsol)-1)
        n = random.randint(0, len(randsol)-1)
    randsol[i] = n
    #for x in range(0, len(randsol)):
    #print randsol[x]
    return randsol

#check indices!
def randtrans(arr, randsol):
    arr=arr[:]
    randsol=randsol[:]
    # for b in range (0, len(randsol)):
    # 	print "randsol[%solution] = " %(b)
    # 	print (randsol[b])
    aprime = [None] * len(arr)
    for i in range (0, len(arr)):
        aprime[i] = 0
    for j in range (0, len(arr)):
        pj = randsol[j]
        # print "pj= %solution" %(pj)
        # print "j= %solution" %(j)
        aprime[pj]+= arr[j]
    #for x in range(0,len(arr)):
    #print aprime[x]
    return aprime

def residue(instance, randsol):
    instance=instance[:]
    randsol=randsol[:]
    # residue for binary
    sol = 0
    for i in range (0, len(instance)):
        sol += instance[i]*randsol[i]
    if (sol < 0):
        return -1 * sol
    return sol

#check notation of copying arrays correct
def reprand_bin(arr, randsol):
    arr=arr[:]
    randsol=randsol[:]
    max_iter = 25000
    for i in range (0, max_iter):
        sprime=randsolgen_binary(arr)[:]
        if (residue(arr,sprime) < residue(arr, randsol)):
            randsol = sprime[:]
        # check notation correct
    return randsol

def hill_bin(arr, randsol):
    arr=arr[:]
    randsol=randsol[:]
    max_iter = 25000
    for i in range (0, max_iter):
        sprime = randadj_bin(randsol)[:]
        if (residue(arr, sprime) < residue(arr, randsol) ):
            randsol = sprime[:]

    return randsol

def sim_bin(arr, randsol):
    arr=arr[:]
    randsol=randsol[:]
    sprime2 = [None] * len(randsol)
    for i in range (0, len(randsol)):
        sprime2[i] = randsol[i]
    max_iter = 25000
    for i in range (0, max_iter):
        sprime=randadj_bin(randsol)[:]
        if (residue(arr, sprime) < residue(arr, randsol)):
            for j in range (0, len(randsol)):
                randsol[j]= sprime[j]
        else:
            karma = residue(arr, sprime) - residue(arr, randsol)
            it = math.pow(10,10)*math.pow(0.8, math.floor(i/300))
            prob = math.pow(math.exp(1), (-1)*karma/it)
            myprob=random.uniform(0,9)
            if (myprob < prob):
                randsol = sprime[:]

        if (residue(arr, randsol) < residue(arr,sprime2)):
            for k in range (0, len(sprime2)):
                sprime2[k]=sprime[k]

    return sprime2

def reprand(arr, randsol):
    arr=arr[:]
    randsol=randsol[:]
    max_iter = 25000
    for i in range (0, max_iter):
        #print "REACH REPRAND %solution" %i
        sprime = randtrans(arr, randsolgen(arr))[:]
        if (karmKarp(sprime) < karmKarp(randsol)):
            for j in range (0, len(randsol)):
                randsol[j]=sprime[j]
    return randsol

def hill(arr, randsol):
    arr=arr[:]
    randsol=randsol[:]
    max_iter = 25000
    for i in range (0, max_iter):
        trans_sol = randtrans(arr, randsol)[:]
        sprime = randadj(randsol)[:]
        sprime_trans = randtrans(arr,sprime)[:]
        if (karmKarp(sprime_trans) < karmKarp(trans_sol)):
            for j in range (0, len(randsol)):
                randsol[j]=sprime[j]
    return randsol


def sim(arr, randsol):
    arr=arr[:]
    randsol=randsol[:]
    sprime2 = [None] * len(randsol)
    for i in range (0, len(randsol)):
        sprime2[i]=randsol[i]
    max_iter = 25000
    for i in range (0, max_iter):
        sprime = randadj(randsol)[:]
        sprime_trans=randtrans(arr,sprime)[:]
        randsol_trans = randtrans(arr,randsol)[:]
        if (karmKarp(sprime_trans)<karmKarp(randsol_trans)):
            for j in range (0, len(randsol)):
                randsol[j]=sprime[j]
        else:
            karma = karmKarp(sprime) - karmKarp(randsol)
            it = math.pow(10,10)*math.pow(0.8, math.floor(i/300))
            prob = math.pow(math.exp(1), (-1)*karma/it)
            myprob= random.uniform(0,9)
            if (myprob < prob):
                for k in range (0, len(randsol)):
                    randsol[k] = sprime[k]
        randsol_trans_final = randtrans(arr, randsol)[:]
        sprime2_trans = randtrans(arr, sprime2)[:]

        if(karmKarp(randsol_trans_final) < karmKarp(sprime2_trans)):
            for l in range (0, len(sprime2)):
                sprime2[l]= sprime[l]

    return sprime2

#for t in range(0,100)
#print "instance %solution" %t



data = []
with open(sys.argv[1],'r') as myfile:
    for line in myfile:
        if line.strip():           # line contains eol character(solution)
            n = long(line)
            data.append(n)

myfile.close()
print(karmKarp(data))


# num_instances = 100

# time_karmKarp = [None]
# time_bin_rr = [None]
# time_bin_hill = [None]
# time_bin_sa = [None]
# time_rr = [None]
# time_hill = [None]
# time_sa = [None]

# residue_karmKarp = [None]
# residue_bin_rr = [None]
# residue_bin_hill = [None]
# residue_bin_sa = [None]
# residue_rr = [None]
# residue_hill = [None]
# residue_sa = [None]



# for i in range(0, num_instances):

# 	arr = instance()[:]

# 	start_time = time.time()
# 	residue_karmKarp.append(karmKarp(arr))
# 	time_karmKarp.append((time.time()-start_time))

# 	start_time = time.time()
# 	residue_bin_rr.append(residue(arr,reprand_bin(arr, randsolgen_binary(arr))))
# 	time_bin_rr.append((time.time()-start_time))

# 	start_time = time.time()
# 	residue_bin_hill.append(residue(arr,hill_bin(arr, randsolgen_binary(arr))))
# 	time_bin_hill.append((time.time()-start_time))

# 	start_time = time.time()
# 	residue_bin_sa.append(residue(arr,sim_bin(arr, randsolgen_binary(arr))))
# 	time_bin_sa.append((time.time()-start_time))

# 	start_time = time.time()
# 	residue_rr.append(karmKarp(reprand(arr,randtrans(arr,randsolgen(arr)))))
# 	time_rr.append((time.time()-start_time))

# 	start_time = time.time()
# 	residue_hill.append(karmKarp(randtrans(arr,(hill(arr, randsolgen(arr))))))
# 	time_hill.append((time.time()-start_time))

# 	start_time = time.time()
# 	residue_sa.append(karmKarp(randtrans(arr,(sim(arr, randsolgen(arr))))))
# 	time_sa.append((time.time()-start_time))


# print "Number of trials:"
# print num_instances

# num_instances =num_instances+1

# print "KK: residue"
# for x in range (0, num_instances):
# 	print residue_karmKarp[x]

# print "time:"
# for x in range (0, num_instances):
# 	print time_karmKarp[x]
# 	#print (residue_karmKarp/num_instancess)
# #time_karmKarp = time_karmKarp/num_instancess
# #print("--- %solution seconds ---" %time_karmKarp)

# print "Binary RR: residue"
# #for x in range (0,num_instancess):
# for x in range (0, num_instances):
# 	print residue_bin_rr[x]
# print "time:"
# for x in range (0, num_instances):
# #for x in range (0,num_instancess):
# 	print time_bin_rr[x]

# print "Binary Hill: residue"
# for x in range (0, num_instances):
# 	print residue_bin_hill[x]
# print "time"
# for x in range (0, num_instances):
# 	print time_bin_hill[x]

# print "Binary SA: residue"
# for x in range (0, num_instances):
# 	print residue_bin_sa[x]
# print "time"
# for x in range (0, num_instances):
# 	print time_bin_sa[x]


# print "Numbers RR: residue"
# for x in range (0, num_instances):
# 	print residue_rr[x]
# print "time"
# for x in range (0, num_instances):
# 	print time_rr[x]

# print "Numbers hill: residue"
# for x in range (0, num_instances):
# 	print residue_hill[x]
# print "time"
# for x in range (0, num_instances):
# 	print time_hill[x]


# print "Numbers SA: residue"
# for x in range (0, num_instances):
# 	print residue_sa[x]

# print "time"
# for x in range (0, num_instances):
# 	print time_sa[x]