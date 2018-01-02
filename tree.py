#solutions to some problems involving trees

import pdb
from util_tree import *
import random

#https://leetcode.com/problems/longest-univalue-path/description/
def longest_path(root):
    path_lens = {} 
    def traverse(prev_val,path_len,node,path_lens):
        if node != None:
            new_path_len = 0
            if node.val == prev_val:
                new_path_len = path_len + 1
            
            path_lens[node] = new_path_len
            traverse(node.val,new_path_len,node.left,path_lens)
            traverse(node.val,new_path_len,node.right,path_lens)

    traverse(-1,0,root,path_lens)
    return path_lens

#https://leetcode.com/problems/merge-two-binary-trees/description/
def merge_trees(T1,T2):
    if T1 and T2:
        root = node(T1.val+T2.val)
        root.left = merge_trees(T1.left,T2.left)
        root.right = merge_trees(T1.right,T2.right)
    elif T1:
        root = node(T1.val)
        root.left = merge_trees(T1.left,None)
        root.right = merge_trees(T1.right,None)
    elif T2:
        root = node(T2.val)
        root.left = merge_trees(None,T2.left)
        root.right = merge_trees(None,T2.right)
    else:
        root = None

    return root

#https://leetcode.com/problems/find-mode-in-binary-search-tree/description/
def mode_bst(T):
    count_dict = {}

    m_c = [(T.val,1)]
    if T.left:
        m_c.append(mode_bst(T.left))

    if T.right:
        m_c.append(mode_bst(T.right))

    for m,c in m_c:
        if m in count_dict:
            count_dict[m] += c
        else:
            count_dict[m] = c

    max_mode = None
    max_count = None

    for m in count_dict:
        if max_mode == None:
            max_mode = m
            max_count = count_dict[m]
        else:
            if count_dict[m] > max_count:
                max_count = count_dict[m]
                max_mode = m

    return max_mode,max_count


def check_subtree(T,S):
    q = [T]
    while len(q) > 0:
        root = q.pop(0)
        if subtree(root,S) == True:
            return True
        if root.left:
            q.append(root.left)
        if root.right:
            q.append(root.right)

    return False

#https://leetcode.com/problems/subtree-of-another-tree/description/
def subtree(T,S):
    if T and S:
        return (T.val == S.val) and subtree(T.left,S.left) and subtree(T.right,S.right)
    elif T:
        return True
    elif S:
        return False
    else:
        return True

def npaths(src,target):
    if src:
        paths = (1 if src.val == target else 0) + npaths(src.left,target-src.val) + npaths(src.right,target-src.val)
        return paths
    else:
        return 0

#https://leetcode.com/problems/path-sum/description/
def path_sum(src,target):
    if src.left != None and src.right != None:
        return path_sum(src.left,target-src.val) or path_sum(src.right,target-src.val)
    elif src.left:
        return path_sum(src.left,target-src.val)
    elif src.right:
        return path_sum(src.right,target-src.val)
    else:
        if src.val == target:
            return True
        else:
            return False

def mirror(T1,T2):
    if T1 != None and T2 != None:
        return (T1.val == T2.val) and mirror(T1.left,T2.right) and mirror(T1.right,T2.left) 
    elif T1:
        return False
    elif T2:
        return False
    else:
        return True

#https://leetcode.com/problems/symmetric-tree/description/
def symmetric_tree(root):
    return mirror(root.left,root.right)

#https://leetcode.com/problems/sum-of-left-leaves/description/
def sum_left_leaves(root,isleft=False):
    if root:
        if root.left == None and root.right == None and isleft == True: #if root is a left leaf node
            return root.val
        else:
            return sum_left_leaves(root.left,True) + sum_left_leaves(root.right,False)
    else:
        return 0

def height(root):
    if root:
        return 1 + max(height(root.left),height(root.right))
    else:
        return 0

#https://leetcode.com/problems/balanced-binary-tree/description/
def balanced(root):
    return abs(height(root.left) - height(root.right)) <= 1 

if __name__ == '__main__':
    values = [4]*13
    T = construct_tree(values)
    print "npaths: " + str(npaths(T,1))
    print "pathsum: " + str(path_sum(T,4))
    print "mirror: " + str(symmetric_tree(T))    
    print "sum left leaves: " + str(sum_left_leaves(T))
    print "balanced: " + str(balanced(T))
    print mode_bst(T)
    pdb.set_trace()
