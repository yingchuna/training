"""
@time: 2021/9/24 16:45
@contact: yingchun.xia@nio.com
@description: 二叉树的前序/中序/后序遍历
@showdoc:
"""


# 创建二叉树参考链接：https://www.jb51.net/article/208606.htm
# 二叉树理论知识补充
'''
创建二叉树
'''
class TreeNode():
    def __init__(self, val, lchild = None,rchild = None):
        self.val = val
        self.lchild = lchild
        self.rchild = rchild

def create_tree(root,val):
    if len(vals) == 0:
        return root
    if val[0] != '#':
        # 前序遍历创建二叉树
        root = TreeNode(vals[0])
        vals.pop(0)
        root.lchild = create_tree(root.lchild, val)
        root.rchild = create_tree(root.rchild, val)
        return root
    else:
        root = None
        vals.pop(0)
        return root

'''
中序遍历二叉树
'''
def intermediateTraversal(now, result=[]):
    if now == None:
        return result
    intermediateTraversal(now.lchild, result)
    result.append(now.val)
    intermediateTraversal(now.rchild, result)
    return result

if __name__ == '__main__':
    root = None
    # 二叉树的扩展，'#'表示子节点为空
    strs="abc##d##e##"
    vals = list(strs)
    roots = create_tree(root, vals)
    print(intermediateTraversal(roots))
