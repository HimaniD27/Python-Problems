def replacing_by_rank(arr):
  sorted_arr=sorted(arr)        #sort() - in place sorting 
  for i in range(len(arr)):
    for j in range(len(sorted_arr)):
      if arr[i]==sorted_arr[j]:
        arr[i]=j+1
        break
  return arr

print(replacing_by_rank([8,6,9,3,5,1,2]))




# by creating a dictionary where each element is mapped to its rank
def rank_replace(arr):
    sorted_arr = sorted(arr)
    rank_dict = {v: i + 1 for i, v in enumerate(sorted_arr)}
    #print(rank_dict)
    ranked_arr = [rank_dict[x] for x in arr]
    return ranked_arr

print(rank_replace([8,6,9,3,5,1,2]))
 