class Node:
    def __init__(self,id):
        self.id=id
        self.left=None
        self.right=None

def solution(n, k, cmd):
    answer = ''
    nodes = []
    for i in range(n-1):
        if i==0:
            nodes.append(Node(i))
        node = nodes[i]
        nodes.append(Node(i+1))
        nxt = nodes[i+1]
        node.right = nxt
        nxt.left=node
        nodes[i]=node
        nodes[i+1]=nxt
        
    stack = []
    for c in cmd:
        i = c.split(" ")
        cnt = int(i[1]) if len(i)==2 else -1
        point_node = nodes[k]
        if i[0] in ['U','D']:
            for j in range(cnt):
                point_node = point_node.left if i[0]=='U' else point_node.right
                k=point_node.id
        elif i[0]=='C':
            left_node = point_node.left;
            right_node = point_node.right;
            stack.append(point_node);
            del_id = point_node.id;
            nodes[del_id] = None;
            if left_node :
                left_node.right = right_node;
            
            if right_node :
                right_node.left = left_node;
                k = right_node.id;
            elif not right_node:
                k = left_node.id;
        elif i[0]=='Z':
            z_node = stack.pop();
            z_node_id = z_node.id;
            nodes[z_node_id]=z_node;
            left_node = z_node.left;
            right_node = z_node.right;
            if left_node: 
                left_node.right = z_node;
            if right_node:
                right_node.left = z_node;
    
    return ''.join(['O' if node else 'X' for node in nodes])