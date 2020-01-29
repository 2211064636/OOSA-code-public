
'''
Examples of binary search
by loop and by recursion
'''


#############################################

def setMidP(start,end):
  '''sets the mid point from the start and end'''
  return((start-end)//2)   # note that "//" is an integer division


#############################################

def binarySearch(x,v):
  '''Binary search for v in x by looping'''

  # set first break point and ends
  start=0              # the start index
  end=len(x)           # the end index
  midP=setMidP(start,end) # middle point index

  # loop over
  while((end-start)>0):
    if(x[midP]>v):   # answer is to the right
      start=midP
      midP=setMidP(start,end)
    elif(x[midP]<v):   # answer is to the left
      end=midP
      midP=setMidP(start,end) 
    elif(x[midP]==v):  # found answer, unlikely
      break

  return(x[midP],midP)


#############################################

def binaryRecurse(x,v,start,end):
  '''Binary search for v in x by recursion'''

  # set first break point and ends
  ind=setMidP(start,end) # middle point index
  thisVal=x[ind]

  # are we at the lowest level? If so, we are there
  if((end-start)<1):
    return(thisVal,ind)

  if(thisVal>v):   # to the right
    thisVal,ind=binaryRecurse(x,v,ind,end)
  elif(thisVal<v):   # answer is to the left
    thisVal,ind=binaryRecurse(x,v,start,ind)
  elif(thisVal==v):  # found answer, unlikely
    return(thisVal,ind)

  return(thisVal,ind)
